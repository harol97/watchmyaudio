"use client";
import { Button } from "@/components/ui/button";
import Advertisement from "@/entities/Advertisement";
import { deleteAdvertisement } from "@/services/advertisement";
import { useRouter } from "next/navigation";

type Props = {
  advertisement: Advertisement;
};

export default function ButtonDelete({ advertisement }: Props) {
  const { refresh } = useRouter();
  return (
    <Button type="button" onClick={() => deleteAdvertisement(advertisement.id).then((result) => result && refresh())}>
      Delete
    </Button>
  );
}
