"use client";

import CustomFormClient from "@/components/custom/custom-form-client";
import { ClientComplete } from "@/components/custom/custom-form-client/custom-form-client";
import { CustomSectionChild } from "@/components/custom/custom-section";
import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import Client from "@/entities/client";
import RadioStation from "@/entities/radio-station";
import { deleteClient, getMyRadioStations } from "@/services/client";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Props = {
  clients: Client[];
  radioStations: RadioStation[];
};

export default function ClientSecion({ radioStations, clients }: Props) {
  const [disabled, setDisabled] = useState<boolean>(true);
  const [client, setClient] = useState<ClientComplete>();
  const { refresh } = useRouter();
  return (
    <CustomSectionChild>
      <p>Manage Client</p>
      <div className="flex flex-row gap-x-5">
        <CustomSelect
          value={String(client?.id)}
          onChange={async (value) => {
            const client = clients.find((cli) => cli.id === Number(value));
            if (client) {
              const myRadioStations = await getMyRadioStations(client.id);
              setClient({ ...client, radioStations: myRadioStations });
            } else setClient(undefined);
          }}
          items={clients.map((client) => ({ label: client.name, value: String(client.id) }))}
        />
        <Button
          onClick={() => {
            setDisabled(false);
          }}
        >
          Update
        </Button>
        <Button
          onClick={() => {
            if (!client) return;
            deleteClient(client.id).then((success) => {
              if (!success) return;
              refresh();
              setClient(undefined);
            });
          }}
        >
          Desactive
        </Button>
      </div>
      <CustomFormClient
        onSubmitOk={() => {
          setDisabled(true);
          setClient(undefined);
        }}
        client={client}
        disabled={disabled}
        onCancel={() => setDisabled(true)}
        type="edit"
        radioStations={radioStations}
      />
    </CustomSectionChild>
  );
}
