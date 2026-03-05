import json
import random
from pathlib import Path

QUESTIONS_DIR = Path(__file__).resolve().parent / "questions"

_question_pool = []


def _extract_questions_from_data(data):
    if isinstance(data, dict):
        if "quiz" in data and isinstance(data["quiz"], list):
            return data["quiz"]
        return []
    if isinstance(data, list):
        return data
    return []


def questionLoader():
    all_questions = []
    for json_file in QUESTIONS_DIR.glob("*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            questions = _extract_questions_from_data(data)
            all_questions.extend(q for q in questions if isinstance(q, dict) and q.get("question"))
        except (OSError, json.JSONDecodeError):
            continue
    return all_questions


def reset_question_pool():
    global _question_pool
    _question_pool = questionLoader()
    random.shuffle(_question_pool)


def get_random_question():
    global _question_pool
    if not _question_pool:
        reset_question_pool()
    if not _question_pool:
        return None
    return _question_pool.pop()