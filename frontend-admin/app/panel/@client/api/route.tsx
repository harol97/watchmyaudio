import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const base = process.env.BASE_URL;
  const cookiesStore = await cookies();
  const token = cookiesStore.get("token");
  if (!token) return Response.redirect("/login");
  const headersInit = new Headers();
  headersInit.set("token", token.value);
  const searchParams = request.nextUrl.searchParams;
  const data = await fetch(
    base +
      `/public/detections/reports?startDate=${searchParams.get("startDate")}&endDate=${searchParams.get(
        "endDate"
      )}&timezone=${searchParams.get("timezone")}`,
    { headers: headersInit }
  );
  const response = new NextResponse(await data.blob(), { headers: data.headers });
  return response;
}
