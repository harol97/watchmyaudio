import { redirect } from "next/navigation";

type Props = {
  searchParams: Promise<{
    logout?: string;
  }>;
};

export default async function RootPage(params: Props) {
  if ((await params.searchParams).logout) return redirect("login");
  return redirect("/panel");
}

