from datetime import datetime
from collections import defaultdict
from file_handler import load_expenses, save_expense


def add_expense():
    try:
        amount = float(input("Enter Amount: ₹"))
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        datetime.strptime(date, "%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        save_expense(expense)
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid input.\n")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    print("\n{:<12} {:<15} {:<25} {:<10}".format(
        "Date", "Category", "Description", "Amount"
    ))
    print("-" * 65)

    for exp in expenses:
        print("{:<12} {:<15} {:<25} ₹{:<10}".format(
            exp["date"],
            exp["category"],
            exp["description"],
            exp["amount"]
        ))

    print()


def filter_by_category():
    category = input("Enter Category: ").lower()

    expenses = load_expenses()

    results = [
        exp for exp in expenses
        if exp["category"].lower() == category
    ]

    if not results:
        print("No matching records.\n")
        return

    for exp in results:
        print(exp)

    print()


def filter_by_date_range():
    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")

    expenses = load_expenses()

    results = []

    for exp in expenses:
        if start <= exp["date"] <= end:
            results.append(exp)

    if not results:
        print("No records found.\n")
        return

    for exp in results:
        print(exp)

    print()


def monthly_summary():
    expenses = load_expenses()

    summary = defaultdict(float)

    for exp in expenses:
        month = exp["date"][:7]
        summary[month] += float(exp["amount"])

    print("\nMonthly Summary")
    print("-" * 30)

    for month, total in summary.items():
        print(f"{month} : ₹{total:.2f}")

    print()


def category_breakdown():
    expenses = load_expenses()

    totals = defaultdict(float)
    overall = 0

    for exp in expenses:
        totals[exp["category"]] += float(exp["amount"])
        overall += float(exp["amount"])

    print("\nCategory Breakdown")
    print("-" * 40)

    for category, amount in totals.items():
        percentage = (amount / overall) * 100
        print(f"{category:<15} ₹{amount:<10.2f} {percentage:.2f}%")

    print(f"\nTotal Spending: ₹{overall:.2f}\n")


def menu():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date Range")
        print("5. Monthly Summary")
        print("6. Category Breakdown")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            filter_by_date_range()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            category_breakdown()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()