"use client";
import Client from "@/entities/client";
import { useEffect, useState } from "react";
import { io } from "socket.io-client";

type Props = {
  client: Client;
  url: string;
};

type Message = {
  message: string;
  radioStationName: string;
  advertisement: string;
};

export default function Monitor({ client, url }: Props) {
  const [messages, setMessages] = useState<Message[]>([]);

  useEffect(() => {
    const socketConnection = io(url);
    socketConnection.on("connection", () => {
      socketConnection.emit("join_room", { id: client.id });
    });
    socketConnection.emit("join_room", { id: client.id });
    socketConnection.on("receive_data", (data) => {
      setMessages((prev) => [
        ...prev,
        { message: data.message, advertisement: data.advertisement, radioStationName: data.radio_station },
      ]);
    });
    return () => {
      socketConnection.emit("leave_room", { id: client.id });
    };
  }, [client, url]);

  return (
    <div className="grow  border-[#2d4bac] border-[1px] rounded-2xl h-80 max-h-80 shadow-2xl p-5 overflow-y-scroll  lg:min-h-0 lg:max-h-full">
      <p className="pb-5">Welcome</p>
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
