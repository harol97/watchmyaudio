"use server";

import Advertisement from "@/entities/Advertisement";
import Client from "@/entities/client";
import RadioStation from "@/entities/radio-station";
import { FetchException } from "@/lib/exceptions-fetch";
import fetchWithToken from "@/lib/fetch-with-token";
import { converFormDatatoObject } from "@/lib/utils";
import { revalidatePath } from "next/cache";
import { ClientResponse, GetAllResponse } from "./responses";
import { ClientFormState, CreateClientFormSchema, EditClientFormSchema } from "./validators";

export async function me(): Promise<Client> {
  const response = await fetchWithToken<Client>("/public/clients/me", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") throw new FetchException(response.message, response.statusCode);
  return response.data;
}

export default async function getClients() {
  const response = await fetchWithToken<ClientResponse[]>("/admins/clients", { method: "GET" });
  if (response.status !== "success") throw new FetchException(response.message, response.statusCode);
  return response.data;
}

export async function createClient(formData: FormData): Promise<ClientFormState> {
  const entries = Object.fromEntries(formData.entries());
  Object.entries(entries).forEach(([key, value]) => {
    if (value.toString().length === 0) formData.delete(key);
  });
  const validateFields = CreateClientFormSchema.safeParse({
    name: formData.get("name"),
    email: formData.get("email"),
    password: formData.get("password"),
    kind: formData.get("kind"),
    phone: formData.get("phone"),
    web: formData.get("web"),
    language: formData.get("language"),
    passwordConfirm: formData.get("passwordConfirm"),
  });
  if (!validateFields.success) {
    return {
      message: validateFields.error.errors[0].message ?? "",
      errors: validateFields.error.flatten().fieldErrors,
    };
  }
  formData.delete("passwordConfirm");
  const toSend = converFormDatatoObject(formData);
  toSend["radioStationIds"] = formData.getAll("radioStationIds") as any;
  const response = await fetchWithToken<ClientResponse>("/admins/clients", {
    method: "POST",
    body: JSON.stringify(toSend),
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success")
    return {
      message: response.message,
      errors: {},
    };
  revalidatePath("/panel");
  return {
    message: "User has been created Successfully",
  };
}

export async function updateClient(formData: FormData): Promise<ClientFormState> {
  const entries = Object.fromEntries(formData.entries());
  Object.entries(entries).forEach(([key, value]) => {
    if (value.toString().length === 0) formData.delete(key);
  });
  const validateFields = EditClientFormSchema.safeParse({
    name: formData.get("name"),
    email: formData.get("email"),
    password: formData.get("password"),
    kind: formData.get("kind"),
    phone: formData.get("phone"),
    web: formData.get("web"),
    language: formData.get("language"),
  });
  if (!validateFields.success) {
    return {
      message: validateFields.error.errors[0].message ?? "",
      errors: validateFields.error.flatten().fieldErrors,
    };
  }
  if (!formData.get("id")) {
    return {
      message: "Error al actualizar",
    };
  }
  const id = formData.get("id");
  formData.delete("id");
  const toSend = converFormDatatoObject(formData);
  toSend["radioStationIds"] = formData.getAll("radioStationIds") as any;
  const response = await fetchWithToken<ClientResponse>(`/admins/clients/${id}`, {
    method: "PATCH",
    body: JSON.stringify(toSend),
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success")
    return {
      message: response.message,
    };
  revalidatePath("/panel/clients");
  return {
    message: "Client has been update successfully",
  };
}

export async function getAdminAdvetisements(clientId: number) {
  const response = await fetchWithToken<Advertisement[]>("/admins/clients/" + clientId + "/advertisements", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return [];
  return response.data;
}

export async function deleteClient(clientId: number) {
  const response = await fetchWithToken<string>("/admins/clients/" + clientId, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  return response.status === "success";
}

export async function getAll() {
  const response = await fetchWithToken<GetAllResponse>("/admins/clients", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return [];
  return response.data;
}

export async function getMyRadioStations(clientId: number) {
  const response = await fetchWithToken<RadioStation[]>("/admins/clients/" + clientId + "/radio-stations", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status === "success") return response.data;
  return [];
}
