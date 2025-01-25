"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { usePathname } from "next/navigation";
import { useState } from "react";
import Row from "./row";

export default function ReportSection() {
  const pathname = usePathname();
  const [startDate, setStartDate] = useState<string | null>(null);
  const [endDate, setEndDate] = useState<string | null>(null);

  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  return (
    <div className="flex flex-col items-start gap-5 justify-start ">
      <label className="font-bold w-full text-left">View Report</label>
      <Row>
        <Label htmlFor="startDate" className="w-20">
          From:
        </Label>
        <Input onChange={(event) => setStartDate(event.currentTarget.value)} id="startDate" type="datetime-local" />
      </Row>
      <Row>
        <Label htmlFor="endDate" className="w-20">
          To:
        </Label>
        <Input onChange={(event) => setEndDate(event.currentTarget.value)} id="endDate" type="datetime-local" />
      </Row>
      <Button disabled={!startDate || !endDate} type="submit">
        <a
          aria-disabled={!startDate || !endDate}
          href={`${pathname}/api?startDate=${startDate}&endDate=${endDate}&timezone=${timezone}`}
          download={"report.pdf"}
        >
          Export
        </a>
      </Button>
    </div>
  );
}
