#!/usr/bin/env python3
"""Backend API smoke tests for MVP acceptance."""
import requests
import sys

BASE = "http://localhost:8000"

def test(method, path, expected_status, json_data=None, desc=None):
    url = f"{BASE}{path}"
    desc = desc or f"{method} {path}"
    try:
        if method == "GET":
            r = requests.get(url, timeout=5)
        else:
            r = requests.post(url, json=json_data or {}, timeout=5)
        if r.status_code == expected_status:
            print(f"✓ {desc} -> {r.status_code}")
            return True
        else:
            print(f"✗ {desc} -> {r.status_code} (expected {expected_status})")
            return False
    except Exception as e:
        print(f"✗ {desc} -> ERROR: {e}")
        return False

def main():
    results = []
    
    # Health and root
    results.append(test("GET", "/health", 200))
    results.append(test("GET", "/", 200))
    
    # Curriculum
    results.append(test("GET", "/api/curriculum", 200))
    results.append(test("GET", "/api/levels", 200))
    results.append(test("GET", "/api/levels/A1", 200))
    results.append(test("GET", "/api/levels/A1/units", 200))
    results.append(test("GET", "/api/units/A1.5", 200))
    results.append(test("GET", "/api/units/INVALID", 404, desc="GET /api/units/INVALID (404)"))
    
    # Lessons
    results.append(test("GET", "/api/lessons/A1.5", 200))
    results.append(test("GET", "/api/lessons/A1.5?study_mode=academic_purpose", 200))
    
    # AI
    results.append(test("POST", "/api/ai/explain-lesson", 200, {"unit_code": "A1.5"}))
    results.append(test("POST", "/api/ai/answer-question", 200, {"unit_code": "A1.5", "question": "How do I order coffee?"}))
    
    # Exercises - need to generate first to get valid exercise_id
    gen_resp = requests.post(f"{BASE}/api/exercises/generate", json={"unit_code": "A1.5", "count": 2}, timeout=5)
    results.append(gen_resp.status_code == 200)
    print(f"{'✓' if gen_resp.status_code == 200 else '✗'} POST /api/exercises/generate -> {gen_resp.status_code}")
    if gen_resp.status_code == 200:
        exercise_id = gen_resp.json().get("exercise_id", "test")
        items = gen_resp.json().get("items", [])
        answers = [{"item_id": item["item_id"], "answer": item["options"][0] if item.get("options") else "a"} for item in items[:1]] if items else [{"item_id": "q1", "answer": "a"}]
        results.append(test("POST", "/api/exercises/submit", 200, {"unit_code": "A1.5", "exercise_id": exercise_id, "answers": answers}))
    else:
        results.append(test("POST", "/api/exercises/submit", 404, {"unit_code": "A1.5", "exercise_id": "invalid", "answers": []}))
    
    # Progress
    results.append(test("GET", "/api/progress/overview", 200))
    results.append(test("GET", "/api/progress/units/A1.5", 200))
    results.append(test("POST", "/api/progress/exercise-result", 200, {"unit_code": "A1.5", "exercise_id": "test", "score": 80, "total": 100, "weak_points": []}))
    
    # Listening
    results.append(test("GET", "/api/listening/units/A1.5", 200))
    results.append(test("POST", "/api/listening/submit", 200, {"unit_code": "A1.5", "answers": [{"question_id": "q1", "answer": "a"}]}))
    
    # Speaking - start returns session_id, use it for respond/finish
    start_resp = requests.post(f"{BASE}/api/speaking/roleplay/start", json={"unit_code": "A1.5"}, timeout=5)
    if start_resp.status_code == 200:
        session_id = start_resp.json().get("session_id", "")
        results.append(True)
        print(f"✓ POST /api/speaking/roleplay/start -> 200")
        results.append(test("POST", "/api/speaking/roleplay/respond", 200, {"session_id": session_id, "message": "Vorrei un caffè"}))
        results.append(test("POST", "/api/speaking/roleplay/finish", 200, {"session_id": session_id}))
    else:
        results.append(False)
        print(f"✗ POST /api/speaking/roleplay/start -> {start_resp.status_code}")
        results.append(test("POST", "/api/speaking/roleplay/respond", 404, {"session_id": "invalid", "message": "test"}, desc="POST /api/speaking/roleplay/respond (no session)"))
        results.append(test("POST", "/api/speaking/roleplay/finish", 404, {"session_id": "invalid"}, desc="POST /api/speaking/roleplay/finish (no session)"))
    
    # Materials
    results.append(test("POST", "/api/materials", 200, {"unit_code": "A1.5", "source_type": "manual_text", "title": "Smoke Test Material", "raw_text": "Il conto, per favore means please bring the bill"}))
    results.append(test("GET", "/api/materials/units/A1.5", 200))
    
    # RAG
    results.append(test("POST", "/api/rag/retrieve", 200, {"query": "How do I ask for the bill?", "unit_code": "A1.5"}))
    
    # Auth
    results.append(test("GET", "/api/auth/me", 200))
    
    passed = sum(results)
    total = len(results)
    print(f"\n{'='*40}\nSmoke test: {passed}/{total} passed")
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
