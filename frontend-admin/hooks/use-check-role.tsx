import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function useCheckRole() {
    const cookieStore = await cookies();
    const role = cookieStore.get('role');
    if (!role) {
        redirect('/login');
    }
    return role.value;
}