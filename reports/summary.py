from collections import defaultdict
from core.utils import format_rupiah
import calendar
from tabulate import tabulate

class SummaryReport:
    def __init__(self, tracker):
        self.tracker = tracker

    def total_by_category(self):
        if not self.tracker.expenses:
            print("No expense data available.")
            return

        total_by_cat = defaultdict(int)
        # print(self.tracker.expenses)

        for item in self.tracker.expenses:
            # print(item["category"])
            total_by_cat[item["category"]] += item["amount"]

        # print(total_by_cat)
        print("\nTotal Expenses by Category:")

        formatted_data = []
        for cat, amount in total_by_cat.items():
            formatted_data.append((cat, format_rupiah(amount)))

        print(tabulate(formatted_data, headers=["Category", "Total Expenses"], tablefmt="rounded_outline"))

    def total_by_date(self):
        if not self.tracker.expenses:
            print("No expense data available.")
            return

        total_by_date = defaultdict(int)

        for item in self.tracker.expenses:
            total_by_date[item["date"]] += item["amount"]

        print("\nTotal Expenses by Date:")

        formatted_data = []
        for date, amount in total_by_date.items():
            formatted_data.append((date, format_rupiah(amount)))

        print(tabulate(formatted_data, headers=["Date", "Total Expenses"], tablefmt="rounded_outline"))

    def total_by_month(self):
        if not self.tracker.expenses:
            print("No expense data available.")
            return

        total_by_month = defaultdict(int)
        for item in self.tracker.expenses:
            month = calendar.month_name[int(item["date"].split("-")[1])]
            total_by_month[month] += item["amount"]

        print("\nTotal Expenses by Month:")
        formatted_data = []
        for month, amount in total_by_month.items():
            formatted_data.append((month, format_rupiah(amount)))

        print(tabulate(formatted_data, headers=["Month", "Total Expenses"], tablefmt="rounded_outline"))
