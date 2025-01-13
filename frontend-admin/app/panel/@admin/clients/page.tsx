import CustomGridClient from "@/components/custom/custom-grid-client"
import getClients from "@/services/client"

export default async function Clients() {
  const clients = await getClients()
  return (
    <CustomGridClient clients={clients} />
  )
}