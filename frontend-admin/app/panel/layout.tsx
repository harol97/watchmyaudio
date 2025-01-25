import getRole from "@/hooks/use-check-role";

export default async function HomeLayout({
  admin,
  client,
}: Readonly<{
  admin: React.ReactNode;
  client: React.ReactNode;
}>) {
  const role = await getRole();
  if (role === "2") return client;
  if (role === "1") return admin;
}
