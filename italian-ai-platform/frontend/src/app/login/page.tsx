import { LoginForm } from "@/features/auth";

export default function LoginPage() {
  return (
    <div className="max-w-md mx-auto mt-16">
      <h1 className="text-2xl font-bold text-gray-900 mb-2">Italian AI Learning Platform</h1>
      <p className="text-gray-600 mb-6">This is your personal Italian AI learning platform.</p>
      <LoginForm />
    </div>
  );
}
