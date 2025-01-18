"use client";
import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import Client from "@/entities/client";
import RadioStation from "@/entities/radio-station";
import { saveAdvertisement } from "@/services/advertisement";
import { ReactNode, useState } from "react";
import Row from "./row";

type Props = {
  radioStations: RadioStation[];
  children?: ReactNode | ReactNode[];
  client: Client;
};

export default function RadioStationSection({ client, radioStations, children }: Props) {
  const [radioStationstoSend, setRadioStations] = useState<RadioStation[]>([]);
  const [radioSelected, setRadioSelected] = useState<RadioStation>();
  const [messageError, setMessageError] = useState<string>();
  const [messageSuccess, setMessageSucces] = useState<string>();
  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (radioStationstoSend.length === 0) return;
        saveAdvertisement(new FormData(event.currentTarget)).then((advertisement) => {
          if (!advertisement) {
            setMessageError("Error to save");
            setMessageSucces(undefined);
            return;
          }
          setMessageError(undefined);
          setMessageSucces("File has been save sucessfully");
        });
      }}
      className=" flex flex-col gap-5 grow"
    >
      <h2 className="font-bold">Selected Radio Stations</h2>
      <Row className="flex-col gap-5">
        {radioStationstoSend.map((radioStation) => (
          <div key={radioStation.id} className="flex flex-row justify-start w-full  gap-x-5 items-center">
            <label>{radioStation.name}</label>
            <input className="hidden" name="radio_station_id" defaultValue={radioStation.id} />
            <Button
              type="button"
              onClick={() => setRadioStations((radios) => radios.filter((radio) => radio.id !== radioStation.id))}
            >
              Delete
            </Button>
          </div>
        ))}
      </Row>
      <Row>
        <label>Add</label>
        <CustomSelect
          onChange={(value) => setRadioSelected(radioStations.find((r) => r.id === Number(value)))}
          placeholder=""
          items={radioStations.map((radio) => ({ label: radio.name, value: String(radio.id) }))}
        ></CustomSelect>
        <Button
          type="button"
          onClick={() =>
            setRadioStations((radios) => {
              if (!radioSelected || radios.map((r) => r.id).includes(radioSelected.id)) return radios;
              return [...radios, radioSelected];
            })
          }
        >
          Ok
        </Button>
      </Row>
      {children}
      {messageError && <p className="w-full text-red-600 text-center">{messageError}</p>}
      {messageSuccess && <p className="w-full text-green-600 text-center">{messageSuccess}</p>}
    </form>
  );
}
