import { z } from "zod";

export const LoginFormSchema = z.object({
    username: z.string().nonempty(),
    password: z.string().nonempty(),
});

export type loginFormState = | {
    errors?:{
        username?:string[],
        password?:string[],
    }
    message?:string
} | undefined
