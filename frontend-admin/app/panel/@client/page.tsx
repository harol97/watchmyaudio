import BasePage from "@/components/custom/base-page";
import CustomSection, { CustomSectionChild } from "@/components/custom/custom-section";
import { getMyAdvertisements } from "@/services/advertisement";
import { me } from "@/services/client";
import { getAllRadioStationClient } from "@/services/radio-station";
import Monitor from "./monitor";
import RadioStationSection from "./radio-station-section";
import ReportSection from "./report-section";

export default async function HomeClientPage() {
  const radioStations = await getAllRadioStationClient();
  const client = await me();
  const advertisements = await getMyAdvertisements();

  return (
    <BasePage title="DASHBOARD User" className="h-full">
      <CustomSection>
        <CustomSectionChild className=" border-solid border-[1px] border-[#2d4bac] shadow-2xl p-5 rounded-2xl">
          <RadioStationSection advertisements={advertisements} client={client} radioStations={radioStations} />
          <ReportSection />
        </CustomSectionChild>
        <CustomSectionChild className="border-[0]">
          <label className="font-bold">Live Monitor</label>
          <Monitor client={client} url={process.env.SOCKET_URL ?? ""} />
        </CustomSectionChild>
      </CustomSection>
    </BasePage>
  );
}
