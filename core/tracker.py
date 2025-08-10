import json
import os
from core.utils import format_rupiah
from tabulate import tabulate
import csv

class ExpenseTracker:
    FIELDNAMES = ["date", "category", "description", "amount"]
    HEADERS = [field.capitalize() for field in FIELDNAMES]

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
        data = dict(zip(self.FIELDNAMES, [date, category, description, amount]))
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

        print(tabulate(formatted_data, headers=self.HEADERS, tablefmt="rounded_outline"))

    def export_to_csv(self, output_file):
        if not self.expenses:
            print("No expenses to export.")
            return
        else:
            fieldnames = list(self.expenses[0].keys())

        try:
            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"✅ Data exported to {output_file}")

        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def import_from_csv(self, input_file):
        try:
            with open(input_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data = {
                        field: int(row[field]) if field == "amount" else row[field]
                        for field in self.FIELDNAMES
                    }
                    self.expenses.append(data)
            print(f"✅ Data imported from {input_file}")
        except FileNotFoundError:
            print(f"❌ File {input_file} not found.")

