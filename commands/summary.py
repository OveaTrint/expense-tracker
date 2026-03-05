import calendar
from datetime import datetime

from utils.display import print_error, print_info
from utils.storage import load_expenses

def summary(args):
    expenses = load_expenses()

    if len(expenses) == 0:
        print_error("No expense found.")
        return

    total_expenses = 0
    if args.month:
        month_name = calendar.month_name[args.month]
        filtered_expenses = []

        for expense in expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
            if expense_date.month == args.month:
                filtered_expenses.append(expense)

        if len(filtered_expenses) == 0:
            print_error(f"No expense found for {month_name}")
            return

        for expense in filtered_expenses:
            total_expenses += expense["Amount"]

        print_info(f"Total expenses for {month_name}: ${total_expenses:.2f}")
    else:
        for expense in expenses:
            total_expenses += expense["Amount"]

        print_info(f"Total expenses: ${total_expenses:.2f}")
