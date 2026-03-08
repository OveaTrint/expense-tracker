# Expense Tracker CLI
This is a CLI project designed to help users track their expenses.

Project Details: [roadmap.sh](https://roadmap.sh/projects/expense-tracker)

## Features
- Add expenses through the `add` command
- List all expenses or list by category with the `list` command
- Delete expenses with the delete command
- Get a summary of all expenses or expenses for the month with the `summary` command

## How to Run
Clone the Repository and change to project directory
```bash
git clone https://github.com/OveaTrint/expense-tracker.git
cd expense_tracker
```
Create a virtual environment and install dependencies
```bash
  python3 -m venv .venv
  source .venv/Scripts/activate
  pip install -r requirements.txt
```

Set an Alias for the main program
```bash
alias expense-tracker="python3 main.py"
```

### Usage
- Add an expense
```bash
  expense-tracker add --amount 20 --description "Lunch" --category "Food
```

- Delete an Expense
```bash
  expense-tracker delete --id 1
```

- List all expenses
```bash
  expense-tracker list
```
  
- List expenses by category
```bash
  expense-tracker list --category "Food"
``` 

- Get a summary of all expenses
```bash
  expense-tracker summary
```

- Get a monthly summary of expenses
```bash
  expense-tracker summary --month 3
```

- Display all commands and how to use them
```bash
  expense-tracker --help
```

  