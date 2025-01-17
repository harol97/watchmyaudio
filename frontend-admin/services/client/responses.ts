import Client from "@/entities/client";

export interface ClientResponse {
  id: number;
  name: string;
  email: string;
  kind: "UNDEFINED" | "SCHEDULE";
}

export type GetAllResponse = Client[];
