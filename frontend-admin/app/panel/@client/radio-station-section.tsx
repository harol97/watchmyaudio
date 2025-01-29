"use client";
import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import Advertisement from "@/entities/Advertisement";
import Client from "@/entities/client";
import RadioStation from "@/entities/radio-station";
import { saveAdvertisement } from "@/services/advertisement";
import { addMinutes, compareDesc, format, isBefore } from "date-fns";
import { useEffect, useRef, useState } from "react";
import ButtonDelete from "./button-delete-advertisement";
import Row from "./row";

type Props = {
  radioStations: RadioStation[];
  client: Client;
  advertisements: Advertisement[];
};

type Message = {
  message: string;
  isError?: boolean;
};

export default function RadioStationSection({ advertisements, client, radioStations }: Props) {
  const [radioStationstoSend, setRadioStations] = useState<RadioStation[]>([]);
  const inputFile = useRef<HTMLInputElement>(null);
  const [radioSelected, setRadioSelected] = useState<RadioStation>();
  const [message, setMessage] = useState<Message | null>(null);
  const [advertisementsAux, setAdvertisements] = useState<Advertisement[]>(advertisements);
  const [currentDateTime, setCurrentDateTime] = useState<string>("");
  useEffect(() => {
    const current = new Date();
    setCurrentDateTime(format(addMinutes(current, 5), "yyyy-MM-dd'T'HH:mm"));
  }, []);
  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (radioStationstoSend.length === 0) return;
        const myForm = event.currentTarget;
        const formData = new FormData(myForm);
        if (client.kind === "SCHEDULE") {
          const startDate = String(formData.get("start_date"));
          const endDate = String(formData.get("end_date"));
          const currentDateTime = addMinutes(new Date(), 5);
          if (isBefore(startDate, currentDateTime)) {
            setMessage({ message: "Start Date must be greather than " + currentDateTime, isError: true });
            return;
          }

          if (compareDesc(startDate, endDate) !== 1) {
            setMessage({ message: "Second Date must be greater than first Date", isError: true });
            return;
          }
        }

        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        formData.set("timezone", timezone);
        saveAdvertisement(formData).then((advertisement) => {
          if (!advertisement) {
            setMessage({ message: "Error to save", isError: true });
            return;
          }
          myForm.reset();
          setAdvertisements((prev) => [...prev, advertisement]);
          setMessage({ message: "File has been save sucessfully" });
        });
      }}
      className=" flex flex-col gap-5 grow "
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
        />
        <Button
          type="button"
          onClick={() =>
            setRadioStations((radios) => {
              if (!radioSelected || radios.map((r) => r.id).includes(radioSelected.id)) return radios;
              return [...radios, radioSelected];
            })
          }
        >
          Load Radio Stream
        </Button>
      </Row>
      <h2 className="font-bold">Selected Files:</h2>
      <div className="flex flex-col gap-5">
        {advertisementsAux.map((adv) => (
          <div key={adv.id} className="flex flex-row gap-x-5 items-center">
            <Label>{adv.filename}</Label>
            <ButtonDelete onClick={setAdvertisements} advertisement={adv} />
          </div>
        ))}
      </div>
      {client.kind === "SCHEDULE" && (
        <Row className="flex-col gap-5 lg:flex-row">
          <div className="flex flex-col w-full">
            <Label>From:</Label>
            <Input type="datetime-local" name="start_date" min={currentDateTime} required />
          </div>
          <div className="flex flex-col w-full">
            <Label>To:</Label>
            <Input type="datetime-local" min={currentDateTime} name="end_date" required />
          </div>
        </Row>
      )}
      <Row>
        <label>Add</label>
        <Input ref={inputFile} name="file" accept=".mp3" type="file" required />
      </Row>
      <Row className="justify-center">
        <Button className="w-40" disabled={radioStationstoSend.length === 0} type="submit">
          Load MP3
        </Button>
      </Row>
      {message && (
        <p className={`w-full ${message.isError ? "text-red-600" : "text-green-600"} text-center`}>{message.message}</p>
      )}
    </form>
  );
}
