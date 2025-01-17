import { ReactNode } from "react";

type CustomSectionChildProps = {
  children: ReactNode | ReactNode[];
  className?: string;
};

export default function CustomSectionChild({ children, className }: CustomSectionChildProps) {
  return <section className={"flex flex-col gap-5  w-full " + className}>{children}</section>;
}
