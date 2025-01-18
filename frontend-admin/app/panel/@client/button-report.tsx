"use client";

import { Button } from "@/components/ui/button";
import { usePathname } from "next/navigation";

export default function ButtonReport() {
  const pathname = usePathname();

  return (
    <Button type="submit">
      <a href={pathname + "/api"} download={"report.csv"}>
        Download
      </a>
    </Button>
  );
}
