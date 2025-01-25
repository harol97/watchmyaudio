import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function converFormDatatoObject(formData: FormData) {
  /* eslint-disable  @typescript-eslint/no-explicit-any */
  const object: Record<string, any> = {};
  formData.forEach((value, key) => {
    object[key] = value;
  });
  return object;
}
