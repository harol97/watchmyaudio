import { Button } from "@/components/ui/button";
import { logout } from "@/services/auth";
import { ReactNode } from "react";

type Props = {
  children?: ReactNode | ReactNode[];
  title: string;
  className?: string;
};

export default function BasePage({ children, className, title }: Props) {
  return (
    <>
      <header className="flex flex-row w-full p-5 shadow-2xl">
        <h1 className="font-bold text-left text-3xl grow">{title}</h1>
        <div>
          <Button onClick={logout}>Log Out</Button>
        </div>
      </header>
      <div className="h-full w-full p-5">
        <div
          className={
            "flex w-full p-3  justify-center items-center flex-col gap-5 bg-[#cfd0d5]  bg-opacity-10 shadow-2xl " +
            className
          }
        >
          {children}
        </div>
      </div>
    </>
  );
}
