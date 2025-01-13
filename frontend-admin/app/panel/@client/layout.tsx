import CustomSidebar from "@/components/custom/custom-sidebar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";

export default function AdminLayout({
    children,
  }: Readonly<{
    children: React.ReactNode;
  }>) {
    return (
        <SidebarProvider>
            <CustomSidebar items={[]}/>
            <SidebarTrigger />
            {children}
        </SidebarProvider>
    );
  }
  