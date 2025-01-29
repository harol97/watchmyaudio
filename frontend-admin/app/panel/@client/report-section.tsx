"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { getDataChart } from "@/services/detection";
import Chart from "chart.js/auto";
import { usePathname } from "next/navigation";
import { useRef, useState } from "react";
import Row from "./row";

const months = [
  "Januay",
  "Frebruary",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "November",
  "December",
];

export default function ReportSection() {
  const [startDate, setStartDate] = useState<string | null>(null);
  const [endDate, setEndDate] = useState<string | null>(null);
  const canvaElement = useRef<HTMLCanvasElement | null>(null);
  const [chartElement, setChartElement] = useState<Chart | null>(null);

  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  const pathname = usePathname();

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
      <div className="flex flex-row gap-x-5">
        <Button disabled={!startDate || !endDate}>
          <a
            aria-disabled={!startDate || !endDate}
            target="_blank"
            href={`${pathname}/api?startDate=${startDate}&endDate=${endDate}&timezone=${timezone}`}
            download="report.pdf"
          >
            Export
          </a>
        </Button>
        <Button
          disabled={!startDate || !endDate}
          onClick={async () => {
            const element = canvaElement.current;
            if (!element) return;
            if (chartElement) chartElement.destroy();
            if (!startDate || !endDate) return;
            const data = await getDataChart(startDate, endDate, timezone);
            setChartElement(
              new Chart(element, {
                type: "line",
                data: {
                  labels: months,
                  datasets: data.map((item) => ({
                    label: item.song,
                    data: item.dataPerMonth,
                    fill: false,
                    borderColor: item.color,
                    backgroundColor: item.color,
                    tension: 0.1,
                  })),
                },
              })
            );
          }}
          type="button"
        >
          View Graph
        </Button>
      </div>
      <canvas className="w-full h-500" ref={canvaElement}></canvas>
    </div>
  );
}
