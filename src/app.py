import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Base directory of the project (root of the repo)
BASE_DIR = Path(__file__).resolve().parent.parent
# Folder where sample CSV data is stored
DATA_DIR = BASE_DIR / "data"

# Paths to the sample data files
TRANSACTIONS_FILE = DATA_DIR / "sample_transactions.csv"
GOALS_FILE = DATA_DIR / "sample_goals.csv"

def load_transactions(path=TRANSACTIONS_FILE):
    """
    Load all transactions from CSV.
    Each row contains: id, date, type (income/expense), category, amount, notes.
    Dates and amounts are converted to proper Python types.
    """
    transactions = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert amount to float for calculations
            row["amount"] = float(row["amount"])
            # Convert string date (YYYY-MM-DD) to a date object
            row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
            transactions.append(row)
    return transactions

def load_goals(path=GOALS_FILE):
    """
    Load monthly budget goals per category from CSV.
    Returns a dict like: {"Groceries": 400.0, "Transport": 150.0, ...}
    """
    goals = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            goals[row["category"]] = float(row["monthly_budget"])
    return goals

def summarize_transactions(transactions):
    """
    Calculate:
    - total income
    - total expenses
    - expenses grouped by category

    Returns:
        income_total (float),
        expense_total (float),
        expenses_by_category (dict)
    """
    income_total = 0.0
    expense_total = 0.0
    expenses_by_category = defaultdict(float)

    for t in transactions:
        if t["type"] == "income":
            income_total += t["amount"]
        else:
            expense_total += t["amount"]
            expenses_by_category[t["category"]] += t["amount"]

    return income_total, expense_total, expenses_by_category

def show_budget_progress(expenses_by_category, goals):
    """
    Print a simple text-based dashboard showing:
    - how much was spent in each category
    - the budget for that category
    - a small progress bar and percentage of budget used
    """
    print("\nBudget Progress by Category")
    print("-" * 32)

    for category, spent in expenses_by_category.items():
        budget = goals.get(category, 0.0)
        if budget <= 0:
            # If no budget is defined, just show the amount spent
            print(f"{category}: no budget set (spent {spent:.2f})")
            continue

        # Percentage of the budget that has been used
        pct = min(spent / budget * 100, 999)
        # Build a bar with up to 20 blocks to visualize progress
        filled_blocks = int(min(pct, 100) // 5)  # 20 blocks max
        bar = "█" * filled_blocks + "·" * (20 - filled_blocks)

        print(f"{category:15} {spent:7.2f} / {budget:7.2f}  [{bar}] {pct:6.1f}%")

def main():
    """
    Entry point for the MVP:
    - Load transactions and goals
    - Compute totals and net balance
    - Display a simple console summary and budget progress
    """
    transactions = load_transactions()
    goals = load_goals()

    income_total, expense_total, expenses_by_category = summarize_transactions(transactions)
    net = income_total - expense_total

    print("Expense & Budgeting App – MVP Summary")
    print("--------------------------------------")
    print(f"Total income : {income_total:.2f}")
    print(f"Total expense: {expense_total:.2f}")
    print(f"Net balance  : {net:.2f}")

    show_budget_progress(expenses_by_category, goals)

if __name__ == "__main__":
    # Run the MVP summary when the script is executed directly
    main()

# End of app.py