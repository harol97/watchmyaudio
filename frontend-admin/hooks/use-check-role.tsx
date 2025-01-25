import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function getRole() {
  const result = await cookies();
  const role = result.get("role");
  if (!role) redirect("/login");
  return role.value;
}
