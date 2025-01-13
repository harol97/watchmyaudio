import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function converFormDatatoObject(formData: FormData) {
  const object: Record<string, any> = {}
  formData.forEach((value, key) => {
    object[key] = value
  })
  return object
}