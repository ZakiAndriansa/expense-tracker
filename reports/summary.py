from collections import defaultdict
from core.utils import format_rupiah

class SummaryReport:
    def __init__(self, tracker):
        self.tracker = tracker

    def total_by_category(self):
        if not self.tracker.expenses:
            print("No expense data available.")
            return

        total_by_cat = defaultdict(int)

        for item in self.tracker.expenses:
            total_by_cat[item["category"]] += item["amount"]

        print("\nTotal Expenses by Category:")
        print("-" * 40)
        for category, total in total_by_cat.items():
            print(f"{category}: {format_rupiah(total)}")
        print("-" * 40)

    def total_by_date(self):
        if not self.tracker.expenses:
            print("No expense data available.")
            return

        total_by_date = defaultdict(int)

        for item in self.tracker.expenses:
            total_by_date[item["date"]] += item["amount"]

        print("\nTotal Expenses by Date:")
        print("-" * 40)
        for date, total in total_by_date.items():
            print(f"{date}: {format_rupiah(total)}")
        print("-" * 40)
