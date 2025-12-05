import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

TRANSACTIONS_FILE = DATA_DIR / "sample_transactions.csv"
GOALS_FILE = DATA_DIR / "sample_goals.csv"


def load_transactions(path=TRANSACTIONS_FILE):
    transactions = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
            transactions.append(row)
    return transactions


def load_goals(path=GOALS_FILE):
    goals = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            goals[row["category"]] = float(row["monthly_budget"])
    return goals


def summarize_transactions(transactions):
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
    print("\nBudget Progress by Category")
    print("-" * 32)

    for category, spent in expenses_by_category.items():
        budget = goals.get(category, 0.0)
        if budget <= 0:
            print(f"{category}: no budget set (spent {spent:.2f})")
            continue

        pct = min(spent / budget * 100, 999)
        filled_blocks = int(min(pct, 100) // 5)  # 20 blocks max
        bar = "█" * filled_blocks + "·" * (20 - filled_blocks)

        print(f"{category:15} {spent:7.2f} / {budget:7.2f}  [{bar}] {pct:6.1f}%")


def main():
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
    main()
