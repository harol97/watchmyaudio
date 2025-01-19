import clsx from "clsx";
import { ReactNode } from "react";

type Props = {
  children?: ReactNode | ReactNode[];
  className?: string;
};

export default function Row({ children, className }: Props) {
  return <div className={clsx("flex flex-row items-center  gap-x-5", className)}>{children}</div>;
}
