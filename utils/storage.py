import json
from pathlib import Path

file_path = Path("expenses.json")


def save_expenses(expenses):
    if not file_path.exists():
        file_path.touch()

    with open(file_path, "w") as f:
        json.dump(expenses, f, indent=2)


def load_expenses() -> list[dict]:
    try:
        with open(file_path, "r") as f:
            expenses = json.load(f)
        return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []
