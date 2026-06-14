import type { Metadata } from "next";
import "./globals.css";
import { AppShell } from "@/components/layout/AppShell";

export const metadata: Metadata = {
  title: "Italian AI Learning Platform",
  description: "Learn Italian with AI-powered tutoring",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="antialiased">
      <body><AppShell>{children}</AppShell></body>
    </html>
  );
}
