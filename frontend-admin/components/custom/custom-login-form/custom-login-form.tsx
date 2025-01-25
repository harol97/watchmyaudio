"use client";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { login, loginAdmin } from "@/services/auth";
import { ClientFormState } from "@/services/client/validators";
import { motion } from "framer-motion";
import { ArrowLeft, Eye, EyeOff } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useActionState, useState } from "react";

export type Props = {
  type: "admin" | "client";
};

export default function CustomLoginForm({ type }: Props) {
  const [showPassword, setShowPassword] = useState(false);
  const title = type === "admin" ? "Administrator" : "Client";
  const { refresh } = useRouter();

  const action = async (state: ClientFormState, formData: FormData) => {
    const result = type === "admin" ? await loginAdmin(state, formData) : await login(state, formData);
    if (!result.errors) refresh();
    return result;
  };

  const [state, formAction, pending] = useActionState(action, undefined);

  return (
    <>
      <div className="hidden">{state?.message}</div>
      <div className="absolute inset-0 bg-white bg-opacity-70"></div>
      <div className="relative z-10 w-full max-w-md">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.3 }}
          className="absolute top-0 left-0 mt-4 ml-4 sm:mt-6 sm:ml-6"
        >
          <Link href="/login" className="inline-flex items-center text-gray-600 hover:text-gray-800 transition-colors">
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back
          </Link>
        </motion.div>
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
          <Card className="bg-white/50 backdrop-blur-sm shadow-lg mt-12 sm:mt-16">
            <CardContent className="p-6">
              <h2 className="text-2xl font-light text-center text-gray-800 mb-6">Log In {title} </h2>
              <form action={formAction} className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="username" className="text-gray-700">
                    username
                  </Label>
                  <Input
                    id="username"
                    name="username"
                    type="text"
                    required
                    className="bg-white/70 border-gray-300 text-gray-800 placeholder-gray-400"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="password" className="text-gray-700">
                    Password
                  </Label>
                  <div className="relative">
                    <Input
                      id="password"
                      name="password"
                      type={showPassword ? "text" : "password"}
                      required
                      className="bg-white/70 border-gray-300 text-gray-800"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-500 dark:text-gray-300 dark:hover:text-gray-400"
                    >
                      {showPassword ? (
                        <EyeOff className="h-5 w-5" aria-hidden="true" />
                      ) : (
                        <Eye className="h-5 w-5" aria-hidden="true" />
                      )}
                    </button>
                  </div>
                </div>
                <Button type="submit" className="w-full text-white hover:bg-gray-700" disabled={pending}>
                  Enter
                </Button>
              </form>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </>
  );
}
