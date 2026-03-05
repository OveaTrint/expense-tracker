from utils.storage import load_expenses, save_expenses
from utils.display import print_info, print_error

def delete(args):
    expenses = load_expenses()
   
    for expense in expenses:
        if args.id == expense["id"]:
            expenses.remove(expense)
            save_expenses(expenses)
            print_info(f"Expense deleted successfully (ID: {args.id})")
            break
    else:
        print_error(f"Expense not found (ID: {args.id})")
        
