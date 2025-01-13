"use server"

import fetchWithToken from "@/lib/fetch-with-token"
import {  ClientResponse } from "./responses";
import { FetchException } from "@/lib/exceptions-fetch";
import { ClientFormState, CreateClientFormSchema, EditClientFormSchema } from "./validators";
import { revalidatePath } from "next/cache";
import { converFormDatatoObject } from "@/lib/utils";

export default async function getClients() {
    const response = await fetchWithToken<ClientResponse[]>('/admins/clients',{method:'GET'});
    if(response.status !== 'success')throw new FetchException(response.message,response.statusCode);
    return response.data;
}

export async function createClient(state: ClientFormState, formData: FormData) {
    const validateFields = CreateClientFormSchema.safeParse({
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password'), 
        kind: formData.get('kind'),
    });

    if (!validateFields.success) {
        return {
            errors: validateFields.error.flatten().fieldErrors
        }
    }        
    const response = await fetchWithToken<ClientResponse>('/admins/clients',{method:'POST',
        body: JSON.stringify(converFormDatatoObject(formData)),
        headers:{'Content-Type':'application/json'}});
    if(response.status !== 'success') return {
        message: response.message
    }
    revalidatePath('/panel/clients');
}   

export async function updateClient(state:ClientFormState,formData: FormData) {
    const validateFields = EditClientFormSchema.safeParse({
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password'), 
        kind: formData.get('kind'),
    });
    
    if (!validateFields.success) {
        return {
            errors: validateFields.error.flatten().fieldErrors
        }
    }        
    console.log("---->",formData)
    if (!formData.get('id')) {
        return {
            message: 'Error al actualizar'
        }
    }

    const id = formData.get('id');
    formData.delete('id');
    console.log("---->")
    const response = await fetchWithToken<ClientResponse>(`/admins/clients/${id}`,{method:'PATCH',
        body: JSON.stringify(converFormDatatoObject(formData)),
        headers:{'Content-Type':'application/json'}});
    console.log("--->",response);
    if(response.status !== 'success') return {
        message: response.message
    }
    revalidatePath('/panel/clients');
}