import BasePage from "@/components/custom/base-page";
import CustomSection, { CustomSectionChild } from "@/components/custom/custom-section";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { getMyAdvertisements } from "@/services/advertisement";
import { me } from "@/services/client";
import { getAllRadioStationClient } from "@/services/radio-station";
import ButtonDelete from "./button-delete-advertisement";
import ButtonReport from "./button-report";
import Monitor from "./monitor";
import RadioStationSection from "./radio-station-section";
import Row from "./row";

export default async function HomeClientPage() {
  const radioStations = await getAllRadioStationClient();
  const client = await me();
  const advertisements = await getMyAdvertisements();

  return (
    <BasePage title="DASHBOARD User" className="h-full">
      <CustomSection>
        <CustomSectionChild className="shadow-2xl p-5 rounded-2xl">
          <RadioStationSection client={client} radioStations={radioStations}>
            <h2 className="font-bold">Selected Files:</h2>
            <div className="flex flex-col gap-5">
              {advertisements.map((adv) => (
                <div key={adv.id} className="flex flex-row gap-x-5">
                  <Label>{adv.filename}</Label>
                  <ButtonDelete advertisement={adv} />
                </div>
              ))}
            </div>
            {client.kind === "SCHEDULE" && (
              <Row className="flex-col gap-5 lg:flex-row">
                <Input type="datetime-local" name="start_date" required />
                <Input type="datetime-local" name="end_date" required />
              </Row>
            )}
            <Row>
              <label>Add</label>
              <Input name="file" type="file" required />
              <Button type="submit">Save</Button>
            </Row>
          </RadioStationSection>
          <Row>
            <label className="font-bold">View Report</label>
            <ButtonReport />
          </Row>
        </CustomSectionChild>
        <CustomSectionChild>
          <label className="font-bold">Live Monitor</label>
          <Monitor client={client} />
        </CustomSectionChild>
      </CustomSection>
    </BasePage>
  );
}
