from argparse import ArgumentParser

from commands.add import add_expense
from commands.delete import delete_expense
from commands.list import list_expenses
from commands.summary import summary_of_expenses

parser = ArgumentParser(
    prog="expense-tracker",
    description="A cli app that helps users manage their expenses",
)
subparser = parser.add_subparsers(help="sub-command help")

add_parser = subparser.add_parser(
    "add",
    help="add a new expense",
    usage="add <--amount amount> <--description description> <--category category>",
)
add_parser.add_argument(
    "--amount", type=float, required=True, help="amount of the expense"
)
add_parser.add_argument(
    "--description", type=str, required=True, help="description of the expense"
)
add_parser.add_argument(
    "--category", type=str, required=True, help="category of the expense"
)
add_parser.set_defaults(func=add_expense)

delete_parser = subparser.add_parser(
    name="delete", help="deletes an expense", usage="delete <--id id>"
)
delete_parser.add_argument("--id", type=int, required=True, help="id of the expense")
delete_parser.set_defaults(func=delete_expense)

list_parser = subparser.add_parser(
    name="list",
    help="list all expenses or list expenses accoring to category",
    usage="list [--category category]",
)
list_parser.add_argument("--category", type=str, help="category of the expense(s)")
list_parser.set_defaults(func=list_expenses)

summary_parser = subparser.add_parser(
    "summary",
    help="shows the total expenses or the total expenses of the month",
    usage="summary [--month month]",
)
summary_parser.add_argument(
    "--month", type=int, choices=range(1, 13), help="month to display summary for"
)
summary_parser.set_defaults(func=summary_of_expenses)

args = parser.parse_args()
args.func(args)
