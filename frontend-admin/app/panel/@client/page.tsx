import BasePage from "@/components/custom/base-page";
import CustomSection, { CustomSectionChild } from "@/components/custom/custom-section";
import { CustomSelect } from "@/components/custom/custom-select/select";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { getAllRadioStationClient } from "@/services/radio-station";
import { ReactNode } from "react";

export default async function HomeClientPage() {

  const radioStations = await getAllRadioStationClient(); 

  return (
    <BasePage title="DASHBOARD User" className="h-full">
      <CustomSection>
        <CustomSectionChild className="shadow-2xl p-5 rounded-2xl">
          <h2 className="font-bold">Selected Radio Stations</h2>
          <Row>
            <label>Add</label>
            <CustomSelect items={new Array()}></CustomSelect>
            <Button>Ok</Button>
          </Row>
          <h2 className="font-bold">Selected Files:</h2>
          <Row>
            <label>Add</label>
            <Input type="file" />
            <Button>Save</Button>
          </Row>

          <Row>
            <label className="font-bold">View Report</label>
            <Button>Download</Button>
          </Row>
        </CustomSectionChild>
        <CustomSectionChild>
          <label className="font-bold">Live Monitor</label>
          <div className="grow h-80 max-h-80 shadow-2xl p-5 overflow-y-scroll  lg:min-h-0 lg:max-h-full"></div>
        </CustomSectionChild>
      </CustomSection>
    </BasePage>
  );
}

type Props = {
  children?: ReactNode | ReactNode[];
};

function Row({ children }: Props) {
  return <div className="flex flex-row items-center gap-x-5">{children}</div>;
}
