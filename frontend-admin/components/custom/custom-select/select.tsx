import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { SelectGroup } from "@radix-ui/react-select";

type SelectItemProps = {
  value: string;
  label: string;
};

type Props = {
  items: SelectItemProps[];
  placeholder?: string;
  disabled?: boolean;
  onChange?: (value: string) => void;
  defaultValue?: string;
  value?: string;
};

export function CustomSelect({ value, defaultValue, disabled, onChange, items, placeholder }: Props) {
  return (
    <Select value={value} disabled={disabled} defaultValue={defaultValue} onValueChange={onChange}>
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder={placeholder ?? "Select a Client"} />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          {items.map((item) => (
            <SelectItem key={item.value} value={item.value}>
              {item.label}
            </SelectItem>
          ))}
        </SelectGroup>
      </SelectContent>
    </Select>
  );
}
