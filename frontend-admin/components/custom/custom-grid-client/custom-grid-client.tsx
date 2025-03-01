"use client";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import Client from "@/entities/client";
import { Mail } from "lucide-react";
import { useState } from "react";
import CustomFormClient from "../custom-form-client/custom-form-client";

interface Props {
  clients: Client[];
}

export default function CustomGridClient({ clients }: Props) {
  const [searchTerm, setSearchTerm] = useState("");

  const filteredClients = clients.filter((client) => {
    const searchLower = searchTerm.toLowerCase();
    return Object.values(client).some((value) => String(value).toLowerCase().includes(searchLower));
  });

  const getKindColor = (kind: string) => {
    switch (kind) {
      case "UNDEFINED":
        return "bg-green-100 text-green-800 hover:bg-green-200";
      case "SCHEDULE":
        return "bg-red-100 text-red-800 hover:bg-red-200";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row gap-4 mb-6">
        <div className="flex-grow flex gap-5">
          <Input
            placeholder="Buscar clientes..."
            className="flex-grow"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <CustomFormClient radioStations={[]} type="create" />
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredClients.map((client) => (
          <div key={client.id}>
            <Card className="overflow-hidden hover:shadow-lg transition-shadow duration-300">
              <CardHeader className="pb-2">
                <div className="flex justify-between items-start">
                  <CardTitle className="text-lg flex items-center">
                    <span className="mr-2">👤</span>
                    {client.name}
                  </CardTitle>
                  <Badge className={`${getKindColor(client.kind)}`}>{client.kind}</Badge>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  <p className="text-sm text-gray-600 flex items-center">
                    <Mail className="mr-2 h-4 w-4" />
                    {client.email}
                  </p>
                </div>
                <div className="mt-4 flex justify-end"></div>
              </CardContent>
            </Card>
          </div>
        ))}
      </div>
    </div>
  );
}
