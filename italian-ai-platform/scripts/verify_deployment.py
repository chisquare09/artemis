#!/usr/bin/env python3
"""Post-deployment verification script for Italian AI Learning Platform."""
import sys
import requests

def test(desc, method, url, expected, json_data=None):
    try:
        if method == "GET":
            r = requests.get(url, timeout=10)
        else:
            r = requests.post(url, json=json_data or {}, timeout=10)
        if r.status_code == expected:
            print(f"✓ {desc}")
            return True, r
        else:
            print(f"✗ {desc} - got {r.status_code}, expected {expected}")
            return False, r
    except Exception as e:
        print(f"✗ {desc} - ERROR: {e}")
        return False, None

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_deployment.py <BACKEND_URL> [FRONTEND_URL]")
        print("Example: python verify_deployment.py https://api.example.com https://app.example.com")
        sys.exit(1)
    
    backend = sys.argv[1].rstrip("/")
    frontend = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else None
    
    print(f"\n=== Verifying Backend: {backend} ===\n")
    results = []
    
    # Health
    ok, _ = test("Health check", "GET", f"{backend}/health", 200)
    results.append(ok)
    
    # Root
    ok, _ = test("Root endpoint", "GET", f"{backend}/", 200)
    results.append(ok)
    
    # Curriculum
    ok, r = test("Get levels", "GET", f"{backend}/api/levels", 200)
    results.append(ok)
    if ok and r:
        levels = r.json()
        level_codes = [l.get("code") for l in levels]
        if set(["A1", "A2", "B1", "B2"]).issubset(set(level_codes)):
            print(f"  ✓ All 4 levels present: {level_codes}")
        else:
            print(f"  ✗ Missing levels. Found: {level_codes}")
            results.append(False)
    
    ok, _ = test("Get A1.5 unit", "GET", f"{backend}/api/units/A1.5", 200)
    results.append(ok)
    
    ok, _ = test("Get A1.5 lesson", "GET", f"{backend}/api/lessons/A1.5", 200)
    results.append(ok)
    
    # AI
    ok, _ = test("AI explain lesson", "POST", f"{backend}/api/ai/explain-lesson", 200, {"unit_code": "A1.5"})
    results.append(ok)
    
    ok, _ = test("AI answer question", "POST", f"{backend}/api/ai/answer-question", 200, {"unit_code": "A1.5", "question": "How do I order coffee?"})
    results.append(ok)
    
    # Exercises
    ok, r = test("Generate exercises", "POST", f"{backend}/api/exercises/generate", 200, {"unit_code": "A1.5", "count": 2})
    results.append(ok)
    if ok and r:
        data = r.json()
        exercise_id = data.get("exercise_id")
        items = data.get("items", [])
        if items:
            answers = [{"item_id": items[0]["item_id"], "answer": items[0].get("options", ["a"])[0]}]
            ok, _ = test("Submit exercises", "POST", f"{backend}/api/exercises/submit", 200, {"unit_code": "A1.5", "exercise_id": exercise_id, "answers": answers})
            results.append(ok)
    
    # Progress
    ok, _ = test("Progress overview", "GET", f"{backend}/api/progress/overview", 200)
    results.append(ok)
    
    # Listening
    ok, _ = test("Listening activity", "GET", f"{backend}/api/listening/units/A1.5", 200)
    results.append(ok)
    
    # Speaking
    ok, r = test("Speaking start", "POST", f"{backend}/api/speaking/roleplay/start", 200, {"unit_code": "A1.5"})
    results.append(ok)
    if ok and r:
        session_id = r.json().get("session_id")
        ok, _ = test("Speaking respond", "POST", f"{backend}/api/speaking/roleplay/respond", 200, {"session_id": session_id, "message": "Vorrei un caffè"})
        results.append(ok)
    
    # Materials
    ok, _ = test("Get materials", "GET", f"{backend}/api/materials/units/A1.5", 200)
    results.append(ok)
    
    # RAG
    ok, _ = test("RAG retrieve", "POST", f"{backend}/api/rag/retrieve", 200, {"query": "bill", "unit_code": "A1.5"})
    results.append(ok)
    
    # Auth
    ok, _ = test("Auth me", "GET", f"{backend}/api/auth/me", 200)
    results.append(ok)
    
    # Summary
    passed = sum(results)
    total = len(results)
    print(f"\n{'='*50}")
    print(f"Backend: {passed}/{total} checks passed")
    
    if frontend:
        print(f"\n=== Frontend: {frontend} ===")
        print("Manual verification required:")
        print("  [ ] Homepage loads")
        print("  [ ] /login page loads")
        print("  [ ] /units/A1.5 loads")
        print("  [ ] No console errors")
        print("  [ ] API calls succeed (check Network tab)")
    
    print(f"\n{'='*50}")
    if passed == total:
        print("✓ Deployment verification PASSED")
        return 0
    else:
        print(f"✗ Deployment verification FAILED ({total - passed} issues)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
