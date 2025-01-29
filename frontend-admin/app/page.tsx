import { redirect } from "next/navigation";

type Props = {
  searchParams: {
    logout?: string;
  };
};

export default function RootPage(params: Props) {
  if (params.searchParams.logout) return redirect("login");
  return redirect("/panel");
}

