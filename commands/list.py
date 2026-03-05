from tabulate import tabulate
from utils.storage import load_expenses
from utils.display import print_error


def list(args):
    expenses = load_expenses()
    
    if len(expenses) == 0:
        print_error(msg="No expense found.")
        return 
    
    if args.category:
        filtered_expenses = []
        for expense in expenses:
            if expense["category"] == args.category:
                filtered_expenses.append(expense)
            
        if len(filtered_expenses) == 0:
           print_error(f"No expense found for category {args.category}") 
           return
           
        print(tabulate(tabular_data=filtered_expenses, headers="keys"))   
    else:
        print(tabulate(tabular_data=expenses, headers="keys"))