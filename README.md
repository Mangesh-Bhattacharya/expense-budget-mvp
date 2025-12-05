# Expense \& Budgeting App – MVP

Lightweight MVP for an expense and income tracking app with budgeting and simple progress visualization. This project demonstrates how to structure core features for adding transactions, setting goals, and viewing progress over time.

***

## Core Features

- Add income and expense entries (amount, type, category, date, note)
- Import transactions from a CSV file (simulating photos/files upload parsing)
- Dashboard-style summary of totals by type and category
- Monthly budget goals and progress calculation
- Simple charts for spending vs. income and goal completion (text/CLI-level in this MVP)

***

## Project Overview

This MVP focuses on the backend logic and data model:

1. **Transaction Management**
    - Create income and expense records
    - Store category, date, and notes
    - Load example data from `data/sample_transactions.csv`
2. **Budget \& Goal Tracking**
    - Define monthly budget goals per category
    - Track actual spending vs. goals using `data/sample_goals.csv`
    - Compute remaining budget and completion percentage
3. **Progress Visualization (MVP)**
    - Generate text-based summaries (totals and percentages)
    - Output simple ASCII-style bar indicators in the console

***

## Project Tree

```text
expense-budget-mvp/
├─ README.md
├─ src/
│  └─ app.py
├─ data/
│  ├─ sample_transactions.csv
│  └─ sample_goals.csv
└─ docs/
   └─ mvp_spec.md
```


***

## Usage

Create and activate a virtual environment if desired, then:

```bash
cd expense-budget-mvp
python src/app.py
```

The script will:

- Load sample transactions and goals
- Calculate income, expenses, and net balance
- Show spending vs. budget per category

***

## Example Console Output

```text
Expense & Budgeting App – MVP Summary
--------------------------------------
Total income : 3100.00
Total expense: 512.24
Net balance  : 2587.76

Budget Progress by Category
--------------------------------
Groceries        181.25 /  400.00  [█████████···········]   45.3%
Transport         55.00 /  150.00  [███████·············]   36.7%
Entertainment     45.99 /  200.00  [████················]   23.0%
Utilities        150.00 /  300.00  [██████████··········]   50.0%
Health            80.00 /  100.00  [████████████████····]   80.0%
```


***

## Tech Stack

- Python 3
- CSV files as lightweight storage
- Simple console output for MVP visualization

***

## Notes

This repository is intended as a minimal first version (MVP) to demonstrate the app’s core logic and structure. It can be extended with:

- Database integration
- File/photo OCR pipeline for receipt parsing
- Web or mobile UI for data entry and dashboard views

