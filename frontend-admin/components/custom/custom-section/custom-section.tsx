import { ReactNode } from "react";

type SectionProps = {
  children: ReactNode | ReactNode[];
  className?: string;
};

export default function CustomSection({ children, className }: SectionProps) {
  return (
    <section className={"flex flex-col gap-5 lg:flex-row lg:gap-0 lg:gap-x-5 lg:w-[70%] " + className}>
      {children}
    </section>
  );
}
