"use client";

import CustomSelect from "@/components/custom/custom-select";
import Advertisement from "@/entities/Advertisement";
import Client from "@/entities/client";
import { getAdminAdvetisements } from "@/services/client";
import { useState } from "react";

type Props = {
  clients: Client[];
};

export default function AdvertisementComponent({ clients }: Props) {
  const [advertisements, setAdvertisements] = useState<Advertisement[]>([]);

  return (
    <>
      <div className="flex flex-row gap-x-5 items-center ">
        <span>Client</span>
        <CustomSelect
          onChange={(value) => {
            getAdminAdvetisements(Number(value)).then((advs) => setAdvertisements(advs));
          }}
          items={clients.map((client) => ({ label: client.name, value: String(client.id) }))}
        />
      </div>
      <div className="shadow-xl flex-grow overflow-y-scroll bg-white border-[#2d4bac] border-solid border-[1px] min-h-56 rounded-2xl">
        {advertisements.map(({ id, filename }) => (
          <p key={id}>{filename}</p>
        ))}
      </div>
    </>
  );
}
