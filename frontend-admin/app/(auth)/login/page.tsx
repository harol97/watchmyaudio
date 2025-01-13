"use client"
import {Button} from "@/components/ui/button";
import {Card, CardContent} from "@/components/ui/card";
import {motion} from 'framer-motion';
import Link from "next/link";

export default function Welcome() {
  return (
    <>
      <div className="absolute inset-0 bg-white bg-opacity-70"></div>
      <div className="relative z-10 w-full max-w-md px-4">
        <motion.div
          initial={{opacity: 0, y: 20}}
          animate={{opacity: 1, y: 0}}
          transition={{duration: 0.5}}
          className="w-full max-w-md"
        >
          <Card className="bg-white/50 backdrop-blur-sm shadow-lg">
            <CardContent className="flex flex-col space-y-4 p-6">
              <h2 className="text-xl font-light text-center text-gray-800 mb-4">Welcome to WhatchMyAudio</h2>
              <Link href="login/client" >
                <Button variant="outline" className="w-full bg-white/50 text-gray-800 border-gray-300 hover:bg-gray-100">
                  Client
                </Button>
              </Link>
              <Link href='login/admin'>
                <Button variant="outline" className="w-full bg-white/50 text-gray-800 border-gray-300 hover:bg-gray-100">
                  Administrator
                </Button>
              </Link>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </>
  );
}
