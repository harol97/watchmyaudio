type Props = {
  children: React.ReactNode;
};

export default function CustomBackgroundImage({ children }: Props) {
  return (
    <div className="flex flex-col w-full items-center justify-center min-h-screen bg-cover bg-center bg-custom-image">
      {children}
    </div>
  );
}

