from core.tracker import ExpenseTracker
from reports.summary import SummaryReport
from core.utils import request_date, request_amount

def show_menu():
    title = "Expense Tracker Application"
    separator = "=" * len(title)
    print(separator)
    print(title)
    print(separator)
    print("[1] Add Expense")
    print("[2] View All Expenses")
    print("[3] Total by Category")
    print("[4] Total by Date")
    print("[5] Total by Month")
    print("[6] Exit")

def main():
    tracker = ExpenseTracker()
    summary = SummaryReport(tracker)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            date = request_date()
            category = input("Category (e.g., Food, Transport, etc.): ")
            description = input("Description: ")
            amount = request_amount()

            try:
                amount = int(amount)
                tracker.add_expense(date, category, description, amount)
                print("✅ Expense added successfully!")
            except ValueError:
                print("❌ Amount must be a number!")

        elif choice == "2":
            tracker.show_all()

        elif choice == "3":
            summary.total_by_category()

        elif choice == "4":
            summary.total_by_date()

        elif choice == "5":
            summary.total_by_month()

        elif choice == "6":
            tracker.save_data()
            print("👋 Program ended. Data has been saved.")
            break

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
