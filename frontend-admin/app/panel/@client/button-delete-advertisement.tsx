import { Button } from "@/components/ui/button";
import Advertisement from "@/entities/Advertisement";
import { desactiveAdvertisement } from "@/services/advertisement";
import { Dispatch, SetStateAction } from "react";

type Props = {
  advertisement: Advertisement;
  onClick: Dispatch<SetStateAction<Advertisement[]>>;
};

export default function ButtonDelete({ advertisement, onClick }: Props) {
  return (
    <Button
      type="button"
      onClick={() =>
        desactiveAdvertisement(advertisement.id).then(
          (result) => result && onClick((prev) => prev.filter((adv) => adv.id !== advertisement.id))
        )
      }
    >
      Disable
    </Button>
  );
}
