import useCheckRole from "@/hooks/use-check-role";

export default async function HomeLayout({
    admin,
    client,
  }: Readonly<{
    admin: React.ReactNode;
    client:React.ReactNode
  }>) {

    const role = await useCheckRole();
    if (role === '2') {
      return client
    }else if (role === '1') {
      return admin
    }
  }
  