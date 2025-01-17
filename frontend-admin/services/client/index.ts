"use server";

import Advertisement from "@/entities/Advertisement";
import { FetchException } from "@/lib/exceptions-fetch";
import fetchWithToken from "@/lib/fetch-with-token";
import { converFormDatatoObject } from "@/lib/utils";
import { revalidatePath } from "next/cache";
import { ClientResponse, GetAllResponse } from "./responses";
import { ClientFormState, CreateClientFormSchema, EditClientFormSchema } from "./validators";

export default async function getClients() {
  const response = await fetchWithToken<ClientResponse[]>("/admins/clients", { method: "GET" });
  if (response.status !== "success") throw new FetchException(response.message, response.statusCode);
  return response.data;
}

export async function createClient(formData: FormData): Promise<ClientFormState> {
  const validateFields = CreateClientFormSchema.safeParse({
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
  const response = await fetchWithToken<ClientResponse>("/admins/clients", {
    method: "POST",
    body: JSON.stringify(converFormDatatoObject(formData)),
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success")
    return {
      message: response.message,
    };
  revalidatePath("/panel");
  return {
    message: "User has been created Successfully",
  };
}

export async function updateClient(formData: FormData): Promise<ClientFormState> {
  const password = formData.get("password") as string;
  const kind = formData.get("kind") as string;
  if (password.length === 0) formData.delete("password");
  if (kind.length === 0) formData.delete("kind");
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
  const response = await fetchWithToken<ClientResponse>(`/admins/clients/${id}`, {
    method: "PATCH",
    body: JSON.stringify(converFormDatatoObject(formData)),
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

