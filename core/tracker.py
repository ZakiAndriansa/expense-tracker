import json
import os
from core.utils import format_rupiah
from tabulate import tabulate

class ExpenseTracker:
    def __init__(self):
        self.filepath = "data/expenses.json"
        self.expenses = []
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                try:
                    self.expenses = json.load(file)
                except json.JSONDecodeError:
                    self.expenses = []
        else:
            self.expenses = []

    def save_data(self):
        with open(self.filepath, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, date, category, description, amount):
        data = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        self.expenses.append(data)

    def show_all(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("\nAll Expenses:")
        # print("-" * 50)
        # print("Date | Category | Description | Amount")
        # for item in self.expenses:
        #     print(f"{item['date']} | {item['category']} | {item['description']} | {format_rupiah(item['amount'])}")
        # print("-" * 50)

        formatted_data = []
        for item in self.expenses:
            formatted_data.append((item['date'], item['category'], item['description'], format_rupiah(item['amount'])))

        print(tabulate(formatted_data, headers=["Date", "Category", "Description", "Total Expenses"], tablefmt="rounded_outline"))
