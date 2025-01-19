import BasePage from "@/components/custom/base-page";
import CustomFormClient from "@/components/custom/custom-form-client/custom-form-client";
import CustomSection, { CustomSectionChild } from "@/components/custom/custom-section";
import { getAll } from "@/services/client";
import { getAllRadioStation } from "@/services/radio-station";
import AdvertisementComponent from "./client-advertisement";
import ClientSecion from "./client-section";
import RadioStationForm from "./form-radio-station";
import RadioStationSection from "./radio-station-section";

export default async function HomeAdminPage() {
  const clients = await getAll();
  const radioStations = await getAllRadioStation();

  return (
    <BasePage title="DASHBOARD WatchMyAudio">
      <CustomSection>
        <CustomSectionChild>
          <p>Create Client</p>
          <CustomFormClient type="create" />
        </CustomSectionChild>
        <CustomSectionChild>
          <AdvertisementComponent clients={clients} />
        </CustomSectionChild>
      </CustomSection>
      <CustomSection>
        <ClientSecion clients={clients} />
        <CustomSectionChild>
          <div>
            <p>Load Stream Radio Stations</p>
            <RadioStationForm />
          </div>
          <div className=" flex flex-col gap-5">
            <p>Manage Radio Stations</p>
            <RadioStationSection radioStations={radioStations} />
          </div>
        </CustomSectionChild>
      </CustomSection>
    </BasePage>
  );
}
