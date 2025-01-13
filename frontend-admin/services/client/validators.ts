import { z } from "zod";

export const CreateClientFormSchema = z.object({
    name: z.string().nonempty(),
    email: z.string().email(),
    kind: z.enum(["UNDEFINED", "SCHEDULE"]),
    password: z.string().nonempty(),
});

export const EditClientFormSchema = z.object({
    name: z.string().nonempty(),
    email: z.string().email(),
    kind: z.enum(["UNDEFINED", "SCHEDULE"]),
    password: z.string().optional(),
});

export type ClientFormState = | {
    errors?:{
        name?:string[],
        email?:string[],
        kind?:string[],
        password?:string[],

    }
    message?:string
} | undefined
