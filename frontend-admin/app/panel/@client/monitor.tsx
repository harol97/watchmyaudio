"use client";
import Client from "@/entities/client";
import { useEffect, useState } from "react";
import { io } from "socket.io-client";

type Props = {
  client: Client;
};

type Message = {
  message: string;
  radioStationName: string;
  advertisement: string;
};

export default function Monitor({ client }: Props) {
  const [messages, setMessages] = useState<Message[]>([
    { message: "starting..", radioStationName: "", advertisement: "" },
  ]);

  useEffect(() => {
    const socketConnection = io("http://localhost:8000");
    socketConnection.on("connection", () => {
      socketConnection.emit("join_room", { id: client.id });
    });
    socketConnection.emit("join_room", { id: client.id });
    socketConnection.on("receive_data", (data) => {
      console.log(data);
      setMessages((prev) => [
        ...prev,
        { message: data.message, advertisement: data.advertisement, radioStationName: data.radio_station },
      ]);
    });
    return () => {
      socketConnection.emit("leave_room", { id: client.id });
    };
  }, [client]);

  return (
    <div className="grow h-80 max-h-80 shadow-2xl p-5 overflow-y-scroll  lg:min-h-0 lg:max-h-full">
      {messages.map((mssg, index) => (
        <div className="pb-5" key={index}>
          <p>Message: {mssg.message}</p>
          <p>Radio Station:{mssg.radioStationName}</p>
          <p>Advertisement: {mssg.advertisement}</p>
        </div>
      ))}
    </div>
  );
}
