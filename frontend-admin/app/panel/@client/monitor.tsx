"use client";
import Client from "@/entities/client";
import { useEffect, useState } from "react";
import { io } from "socket.io-client";

type Props = {
  client: Client;
};

export default function Monitor({ client }: Props) {
  const [message, setMessage] = useState<string>("");

  useEffect(() => {
    const socketConnection = io("http://localhost:8000");
    socketConnection.emit("join_room", { id: client.id });
    socketConnection.on("receive_data", (data) => {
      setMessage((message) => message + "separate" + JSON.stringify(data));
    });
    return () => {
      socketConnection.emit("leave_room", { id: client.id });
    };
  }, [client]);

  return (
    <div className="grow h-80 max-h-80 shadow-2xl p-5 overflow-y-scroll  lg:min-h-0 lg:max-h-full">
      {message.split("separate").map((mssg, index) => (
        <p className="pb-7" key={index}>
          {mssg}
        </p>
      ))}
    </div>
  );
}
