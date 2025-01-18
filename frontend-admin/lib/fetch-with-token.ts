import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import baseFetch from "./base-fetch";

export default async function fetchWithToken<T>(endpoint: string, options: RequestInit = {}) {
  const cookiesStore = await cookies();
  const token = cookiesStore.get("token");
  if (!token) {
    redirect("/login");
  }
  const defaultHeaders: HeadersInit = {
    Authorization: "Bearer " + token.value,
    token: token.value,
  };
  options.headers = {
    ...defaultHeaders,
    ...options.headers,
  };
  const response = await baseFetch<T>(endpoint, options);
  if (response.status === "error" && response.statusCode === 401) {
    redirect("/login");
  }
  return response;
}
