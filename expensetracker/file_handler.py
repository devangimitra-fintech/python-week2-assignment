import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses


def save_expense(expense):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        fieldnames = ["amount", "category", "description", "date"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(expense)