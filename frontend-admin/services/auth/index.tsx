"use server";
import baseFetch from "@/lib/base-fetch";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { LoginResponse } from "./responses";
import { LoginFormSchema, loginFormState } from "./validators";

export async function loginAdmin(state: loginFormState, formData: FormData) {
  return loginUser(state, formData, "/admins/auth/login", "1");
}

export async function login(state: loginFormState, formData: FormData) {
  return loginUser(state, formData, "/public/auth/login", "2");
}

async function loginUser(state: loginFormState, formData: FormData, path: string, role: string) {
  const validateFields = LoginFormSchema.safeParse({
    username: formData.get("username"),
    password: formData.get("password"),
  });

  if (!validateFields.success) {
    return {
      errors: validateFields.error.flatten().fieldErrors,
    };
  }
  const response = await baseFetch<LoginResponse>(path, {
    method: "POST",
    body: formData,
  });
  if (response.status !== "success") {
    return {
      message: response.message,
    };
  }
  const cookieStore = await cookies();
  cookieStore.set("token", response.data.accesToken, {
    httpOnly: true,
    sameSite: "strict",
  });
  cookieStore.set("role", role, {
    httpOnly: true,
    sameSite: "strict",
  });
  redirect("/panel");
}

export async function logout() {
  const cookieStore = await cookies();
  const token = cookieStore.get("token");
  const role = cookieStore.get("role");
  if (token) {
    cookieStore.delete("token");
  }
  if (role) {
    cookieStore.delete("role");
  }
  redirect("/?logout=true");
}
