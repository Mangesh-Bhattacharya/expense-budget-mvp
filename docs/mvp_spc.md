# Expense & Budgeting App – MVP Specification

## Objective

Design a minimal first version of an expense and budgeting app that can:
- Record income and expense transactions
- Track spending by category
- Compare actual spending against monthly budget goals
- Provide a simple progress view for quick decision‑making

## Core Features (MVP)

1. **Transaction Management**
   - Fields: id, date, type (income/expense), category, amount, notes
   - Support basic operations:
     - Load transactions from `data/sample_transactions.csv`
     - Distinguish income vs. expenses
     - Aggregate totals per category

2. **Budget & Goals**
   - Monthly budget defined per category
   - Stored in `data/sample_goals.csv`
   - For each category:
     - Show budget amount
     - Show actual spending
     - Calculate remaining budget and percentage used

3. **Progress Visualization (Console)**
   - Text summary:
     - Total income
     - Total expenses
     - Net balance
   - Per‑category overview with:
     - Amount spent vs. budget
     - Simple ASCII progress bar
     - Percentage of budget used

## Data Model

### Transactions

Source: `data/sample_transactions.csv`

Fields:
- `id`: unique transaction identifier
- `date`: transaction date (YYYY‑MM‑DD)
- `type`: `income` or `expense`
- `category`: e.g., Groceries, Transport, Entertainment
- `amount`: numeric value in base currency
- `notes`: optional free‑text description

### Budget Goals

Source: `data/sample_goals.csv`

Fields:
- `category`: matching transaction categories
- `monthly_budget`: numeric budget value for that category

## Technical Scope

- Language: Python 3
- Storage: CSV files for sample data
- Interface: Command‑line output (no UI in MVP)
- Entry point: `src/app.py`

## Out of Scope (Future Extensions)

- User authentication and multi‑user support
- Receipt image upload and OCR
- Web or mobile front‑end
- Persistent database (PostgreSQL, MongoDB, etc.)
- Multi‑currency support and advanced analytics

## Usage Notes

This MVP is designed to:
- Demonstrate understanding of expense/budget logic
- Provide a clear structure that can be extended into a full product
- Serve as a work sample for project discussions and refinement
