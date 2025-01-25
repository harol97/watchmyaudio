"use client";
import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import RadioStation from "@/entities/radio-station";
import { deleteRadioStation } from "@/services/radio-station";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Props = {
  radioStations: RadioStation[];
};

export default function RadioStationSection({ radioStations }: Props) {
  const router = useRouter();
  const [selectedRadioStation, setSelectedRadioStation] = useState<string | null>(null);

  const handleDelete = async () => {
    if (!selectedRadioStation) return;
    const deleted = await deleteRadioStation(selectedRadioStation);
    if (deleted) {
      router.refresh();
    }
  };

  return (
    <>
      <div className="flex flex-row gap-x-5 ">
        <CustomSelect
          placeholder="Select Radio Station"
          items={radioStations.map((radio) => ({ label: radio.name, value: String(radio.id) }))}
          onChange={(value) => setSelectedRadioStation(value)}
        />
        <Button onClick={handleDelete} disabled={!selectedRadioStation}>
          Delete
        </Button>
      </div>
    </>
  );
}
