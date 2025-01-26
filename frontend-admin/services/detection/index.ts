"use server";

import fetchWithToken from "@/lib/fetch-with-token";

type Response = {
  song: string;
  dataPerMonth: number[];
  color: string;
};

export async function getDataChart(startDate: string, endDate: string, timezone: string): Promise<Response[]> {
  const response = await fetchWithToken<Response[]>(
    `/public/detections/data?startDate=${startDate}&endDate=${endDate}&timezone=${timezone}`,
    {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    }
  );
  if (response.status !== "success") return [];
  return response.data;
}
