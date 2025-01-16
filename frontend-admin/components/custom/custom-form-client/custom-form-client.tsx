"use client";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

import { Label } from "@/components/ui/label";
import Client from "@/entities/client";
import { createClient, updateClient } from "@/services/client";
import { Pencil, PlusCircle } from "lucide-react";
import { useActionState } from "react";

interface Props {
  type: "edit" | "create";
  client?: Client;
}

export default function CustomFormClient({ type, client }: Props) {
  const isEdit = type === "edit";
  const action = isEdit ? updateClient : createClient;
  const [state, formAction, pending] = useActionState(action, undefined);
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant={isEdit ? "outline" : "default"} size={isEdit ? "sm" : "default"}>
          {isEdit ? (
            <>
              <Pencil className="mr-2 h-4 w-4" />
              Editar
            </>
          ) : (
            <>
              <PlusCircle className="mr-2 h-4 w-4" />
              Nuevo
            </>
          )}
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>{isEdit ? "Actualizar" : "Crear"} Client</DialogTitle>
        </DialogHeader>
        <form className="space-y-4" action={formAction}>
          {isEdit && <input type="hidden" name="id" defaultValue={client?.id} />}
          <div className="space-y-2">
            <Label htmlFor="name">Nombre</Label>
            <Input id="name" defaultValue={client?.name} name="name" />
          </div>
          <div className="space-y-2">
            <Label htmlFor="email">Email</Label>
            <Input id="email" defaultValue={client?.email} readOnly={isEdit} name="email" type="email" />
          </div>
          <div className="space-y-2">
            <Label htmlFor="email">Tipo</Label>
            <Select name="kind" defaultValue={client?.kind}>
              <SelectTrigger>
                <SelectValue placeholder="Ingrese el Tipo" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="UNDEFINED">UNDEFINED</SelectItem>
                <SelectItem value="SCHEDULE">SCHEDULE</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div className="space-y-2">
            <Label htmlFor="email">Contraseña</Label>
            <Input id="password" name="password" type="password" />
          </div>
          <Button type="submit" disabled={pending}>
            {isEdit ? "Actualizar" : "Crear"}
          </Button>
        </form>
      </DialogContent>
    </Dialog>
  );
}
