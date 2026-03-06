from datetime import datetime

from utils.display import print_error, print_info
from utils.storage import load_expenses, save_expenses


def add_expense(args):
    expenses = load_expenses()

    if args.amount < 0:
        print_error("amount cannot be less than 0")
        return

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]["id"] + 1

    expense = {
        "id": expense_id,
        "date": datetime.strftime(datetime.now(), "%Y-%m-%d"),
        "description": args.description,
        "amount": args.amount,
        "category": args.category,
    }
    expenses.append(expense)
    save_expenses(expenses)

    print_info(f"Task Successfully Added ID: {expense_id}")
