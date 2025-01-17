import CustomBackgroundImage from "@/components/custom/custom-background-image";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return <CustomBackgroundImage>{children}</CustomBackgroundImage>;
}

