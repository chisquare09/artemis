"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { AuthStatus } from "@/features/auth";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/modes", label: "Modes" },
  { href: "/progress", label: "Progress" },
  { href: "/review", label: "Review" },
  { href: "/settings", label: "Settings" },
];

export function MainNav() {
  const pathname = usePathname();
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-6xl mx-auto px-4 flex items-center h-14 gap-6">
        <Link href="/" className="font-semibold text-gray-900">Italian AI</Link>
        {links.map((l) => (
          <Link key={l.href} href={l.href} className={`text-sm ${pathname === l.href ? "text-blue-600" : "text-gray-600 hover:text-gray-900"}`}>
            {l.label}
          </Link>
        ))}
        <div className="ml-auto">
          <AuthStatus />
        </div>
      </div>
    </nav>
  );
}
