//middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { cookies } from "next/headers";

export async function middleware(request: NextRequest) {
    const cookiesStore = await cookies()
    const token = cookiesStore.get('token');
    const role = cookiesStore.get('role');
    if(!token || !role) {
        return NextResponse.redirect(new URL('/login',request.url));
    }
    return NextResponse.next();
}

export const config = {
    matcher: '/panel/:path*'
  };