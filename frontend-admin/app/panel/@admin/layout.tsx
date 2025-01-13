import CustomSidebar from "@/components/custom/custom-sidebar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { UserPen } from "lucide-react";

const items = [
  {
    title: "Clients",
    url: "/panel/clients",
    icon: UserPen,
  },
];

export default function AdminLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <SidebarProvider>
      <CustomSidebar items={items} />
      <main className="flex-1 overflow-auto bg-gray-50">
        <SidebarTrigger />
        <div className="mx-auto py-6 sm:px-6 lg:px-8">{children}</div>
      </main>
    </SidebarProvider>
  );
}

