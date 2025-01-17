type Client = {
  id: number;
  name: string;
  email: string;
  kind: "UNDEFINED" | "SCHEDULE";
  web: string;
  phone: string;
  language: string;
};

export default Client;

