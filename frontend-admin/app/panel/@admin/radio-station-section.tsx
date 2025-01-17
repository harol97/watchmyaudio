import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import RadioStation from "@/entities/radio-station";
import RadioStationForm from "./form-radio-station";

type Props = {
  radioStations: RadioStation[];
};

export default function RadioStationSection({ radioStations }: Props) {
  return (
    <>
      <div className="flex flex-row gap-x-5">
        <CustomSelect
          placeholder="Select Radio Station"
          items={radioStations.map((radio) => ({ label: radio.name, value: String(radio.id) }))}
        />
        <Button>Update</Button>
        <Button>Delete</Button>
      </div>
      <RadioStationForm />
    </>
  );
}
