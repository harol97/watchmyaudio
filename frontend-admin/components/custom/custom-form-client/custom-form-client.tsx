"use client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import ReactSelect from "react-select";

import { Label } from "@/components/ui/label";
import Client from "@/entities/client";
import RadioStation from "@/entities/radio-station";
import { createClient, updateClient } from "@/services/client";
import { ClientFormState } from "@/services/client/validators";
import { useRouter } from "next/navigation";
import { useActionState, useCallback, useId, useRef } from "react";

export type ClientComplete = Client & { radioStations: RadioStation[] };

interface Props {
  type: "edit" | "create";
  client?: ClientComplete;
  disabled?: boolean;
  onCancel?: () => void;
  onSubmitOk?: () => void;
  radioStations: RadioStation[];
}

export default function CustomFormClient({ radioStations, onSubmitOk, disabled, onCancel, type, client }: Props) {
  const isEdit = type === "edit";
  const formRef = useRef<HTMLFormElement>(null);
  const { refresh } = useRouter();
  const action = useCallback(
    async (_: ClientFormState, formData: FormData) => {
      const result = isEdit ? await updateClient(formData) : await createClient(formData);
      if (result && !result.errors) {
        refresh();
        onSubmitOk?.();
      }
      return result;
    },
    [isEdit, onSubmitOk, refresh]
  );
  const instanceId = useId();
  const id = useId();
  const [state, formAction, pending] = useActionState(action, undefined);
  const stateColor = state?.errors ? "text-red-500" : "text-green-500";
  return (
    <form
      key={String(client?.id)}
      ref={formRef}
      className="grid grid-cols-2 rounded-xl p-5 shadow-2xl gap-2 bg-white border-[#2d4bac] border-solid border-[1px]"
      action={formAction}
    >
      <p className={`col-span-full text-center ${stateColor}`}>{state?.message}</p>
      {isEdit && <input type="hidden" name="id" defaultValue={client?.id} />}
      <Label htmlFor="name">Name (*)</Label>
      <Input disabled={disabled} defaultValue={client?.name} name="name" />
      <Label htmlFor="email">Email (*)</Label>
      <Input disabled={disabled} defaultValue={client?.email} name="email" type="email" />
      <Label htmlFor="email">Kind (*)</Label>
      <Select disabled={disabled} name="kind" defaultValue={client?.kind}>
        <SelectTrigger>
          <SelectValue placeholder="" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="UNDEFINED">UNDEFINED</SelectItem>
          <SelectItem value="SCHEDULE">SCHEDULE</SelectItem>
        </SelectContent>
      </Select>
      <Label htmlFor="phone">Phone</Label>
      <Input disabled={disabled} defaultValue={client?.phone} name="phone" type="text" />
      <Label htmlFor="web">Web</Label>
      <Input disabled={disabled} name="web" type="url" defaultValue={client?.web} />
      <Label htmlFor="language">Language (*)</Label>
      <Select disabled={disabled} name="language" defaultValue={client?.language}>
        <SelectTrigger>
          <SelectValue placeholder="" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="NEPALI">NEPALI</SelectItem>
          <SelectItem value="ENGLISH">ENGLISH</SelectItem>
        </SelectContent>
      </Select>
      <Label>Radio Stations</Label>
      <ReactSelect
        isDisabled={disabled}
        defaultValue={client?.radioStations.map((rs) => ({ label: rs.name, value: rs.id }))}
        name="radioStationIds"
        isMulti={true}
        isSearchable={false}
        instanceId={instanceId}
        id={id}
        options={radioStations.map((rS) => ({ label: rS.name, value: rS.id }))}
      />
      <Label htmlFor="password">Password {!isEdit && "(*)"}</Label>
      <Input disabled={disabled} name="password" type="password" />
      {type === "create" && (
        <>
          <Label htmlFor="passwordConfirm">Confirm Password (*)</Label>
          <Input disabled={disabled} name="passwordConfirm" type="password" required />
        </>
      )}
      <Button type="submit" disabled={pending || disabled}>
        {isEdit ? "Save" : "Create"}
      </Button>
      <Button
        disabled={disabled}
        type="button"
        onClick={() => {
          onCancel?.();
        }}
      >
        Cancel
      </Button>
    </form>
  );
}
