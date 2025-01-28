"use server";

import Advertisement from "@/entities/Advertisement";
import fetchWithToken from "@/lib/fetch-with-token";

export async function saveAdvertisement(form: FormData): Promise<Advertisement | null> {
  const response = await fetchWithToken<Advertisement>("/public/advertisements", {
    method: "POST",
    body: form,
  });
  if (response.status !== "success") return null;
  return response.data;
}

export async function deleteAdvertisement(advertisementId: number): Promise<boolean> {
  const response = await fetchWithToken<Advertisement>("/public/advertisements/" + advertisementId, {
    method: "DELETE",
  });
  if (response.status !== "success") return false;
  return true;
}

export async function desactiveAdvertisement(advertisementId: number): Promise<boolean> {
  const response = await fetchWithToken<Advertisement>("/public/advertisements/" + advertisementId + "?active=false", {
    method: "PATCH",
  });
  if (response.status !== "success") return false;
  return true;
}

export async function getMyAdvertisements(): Promise<Advertisement[]> {
  const response = await fetchWithToken<Advertisement[]>("/public/advertisements?active=true", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (response.status !== "success") return [];
  return response.data;
}
