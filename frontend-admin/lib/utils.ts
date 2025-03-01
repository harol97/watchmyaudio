import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function converFormDatatoObject(formData: FormData) {
  return Object.fromEntries(formData.entries());
}
