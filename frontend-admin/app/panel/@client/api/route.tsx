import { cookies } from "next/headers";
import { NextResponse } from "next/server";

export async function GET() {
  const base = process.env.BASE_URL;
  const cookiesStore = await cookies();
  const token = cookiesStore.get("token");
  if (!token) return Response.redirect("/login");
  const headersInit = new Headers();
  headersInit.set("token", token.value);
  const data = await fetch(base + "/public/detections/reports", { headers: headersInit });
  const response = new NextResponse(await data.blob(), { headers: data.headers });
  return response;
}
