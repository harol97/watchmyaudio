"use client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { saveRadioStation } from "@/services/radio-station";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Props = {
  isEdit?: boolean;
};

export default function RadioStationForm({}: Props) {
  const [pending, setPending] = useState<boolean>(false);
  const [messageError, setMessageError] = useState<string>();
  const [messageSuccess, setMessageSuccess] = useState<string>();
  const { refresh } = useRouter();
  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        const form = event.currentTarget;
        const formData = new FormData(event.currentTarget);
        setPending(true);
        saveRadioStation(formData).then((radioStation) => {
          setPending(false);
          if (radioStation) {
            refresh();
            form.reset();
            setMessageError(undefined);
            setMessageSuccess("Radio Station has been created successfully.");
            return;
          }
          setMessageSuccess(undefined);
          setMessageError("Error. Try later.");
        });
      }}
      className="shadow-2xl p-5 grid grid-cols-2 gap-2 bg-white rounded-xl border-solid border-[1px] border-[#2d4bac]"
    >
      {messageError && <p className="text-red-500 text-center w-full col-span-full">{messageError}</p>}
      {messageSuccess && <p className="text-green-500 text-center w-full col-span-full">{messageSuccess}</p>}
      <Label>URL Radio Station</Label>
      <Input type="url" name="url" />
      <Label>Name</Label>
      <Input type="text" name="name" />
      <Button disabled={pending} type="submit">
        Load
      </Button>
    </form>
  );
}
