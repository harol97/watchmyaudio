"use client";

import CustomFormClient from "@/components/custom/custom-form-client";
import { CustomSectionChild } from "@/components/custom/custom-section";
import CustomSelect from "@/components/custom/custom-select";
import { Button } from "@/components/ui/button";
import Client from "@/entities/client";
import { deleteClient } from "@/services/client";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Props = {
  clients: Client[];
};

export default function ClientSecion({ clients }: Props) {
  const [disabled, setDisabled] = useState<boolean>(true);
  const [client, setClient] = useState<Client>();
  const { refresh } = useRouter();
  return (
    <CustomSectionChild>
      <p>Manage Client</p>
      <div className="flex flex-row gap-x-5">
        <CustomSelect
          value={String(client?.id)}
          onChange={(value) => setClient(clients.find((cli) => cli.id === Number(value)))}
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
      />
    </CustomSectionChild>
  );
}
