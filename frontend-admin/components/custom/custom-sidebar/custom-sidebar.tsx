import { Sidebar, SidebarContent, SidebarGroup, SidebarGroupContent, SidebarGroupLabel, SidebarMenu, SidebarMenuButton, SidebarMenuItem,SidebarFooter } from "@/components/ui/sidebar";
import CustomNavUser from "../custom-nav-user";

interface Item {
  title: string
  url: string
  icon: React.ElementType
}

interface Props {
  items: Item[]
}

const user = {
  name: "John Doe",
  email: "vland",
  avatar: "",
}

export default function CustomSidebar({items}: Props) {
  return (
    <Sidebar collapsible="icon">
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Panel Administrativo</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <CustomNavUser user={user}/>
      </SidebarFooter>
    </Sidebar>
  )
}