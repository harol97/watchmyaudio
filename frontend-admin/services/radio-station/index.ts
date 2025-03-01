"use server";

import RadioStation from "@/entities/radio-station";
import fetchWithToken from "@/lib/fetch-with-token";
import { SaveRadioStationResponse } from "./responses";

export async function saveRadioStation(form: FormData): Promise<RadioStation | null> {
  const body = Object.fromEntries(form.entries());

  const response = await fetchWithToken<SaveRadioStationResponse>("/admins/radio-stations", {
    method: "POST",
    body: JSON.stringify(body),
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return null;
  return response.data;
}

export async function getAllRadioStation(): Promise<RadioStation[]> {
  const response = await fetchWithToken<RadioStation[]>("/admins/radio-stations", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return [];
  return response.data;
}

export async function deleteRadioStation(id: string): Promise<boolean> {
  const response = await fetchWithToken<string>(`/admins/radio-stations/${id}`, {
    method: "DELETE",
  });
  return response.status === "success";
}

export async function getAllRadioStationClient(): Promise<RadioStation[]> {
  const response = await fetchWithToken<RadioStation[]>("/public/clients/radio-stations", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return [];
  return response.data;
}
