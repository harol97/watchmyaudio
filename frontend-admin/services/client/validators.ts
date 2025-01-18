import { z } from "zod";

export const CreateClientFormSchema = z.object({
  name: z.string().nonempty("Name is empty"),
  email: z.string().email("Incorrect Email"),
  kind: z.enum(["UNDEFINED", "SCHEDULE"], { message: "Incorrect Kind" }),
  password: z.string().nonempty("Password is empty"),
  phone: z.string().nonempty("Incorrect phone"),
  web: z.string().url("Incorrect Url"),
  language: z.enum(["NEPALI", "ENGLISH"], { message: "Incorrect Language" }),
});

export const EditClientFormSchema = z.object({
  name: z.string().nonempty(),
  email: z.string().email(),
  kind: z.enum(["UNDEFINED", "SCHEDULE"]).nullable(),
  password: z.string().nullable(),
  phone: z.string().nonempty("Incorrect phone"),
  web: z.string().url("Incorrect Url"),
  language: z.enum(["NEPALI", "ENGLISH"], { message: "Incorrect Language" }),
});

export type ClientFormState =
  | {
      errors?: {
        name?: string[];
        email?: string[];
        kind?: string[];
        password?: string[];
        web?: string[];
        language?: string[];
        phone?: string[];
      };
      message?: string;
    }
  | undefined;
