from datetime import datetime

def validate_date(date_str):
    """
    Validate whether the input is in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def format_rupiah(amount):
    """
    Format a number into Indonesian Rupiah format.
    Example: 15000 → Rp15.000
    """
    return f"Rp{amount:,.0f}".replace(",", ".")

def current_date():
    """
    Return today's date in YYYY-MM-DD format.
    """
    return datetime.today().strftime("%Y-%m-%d")

def request_date():
    while True:
        use_today = input("Use today's date? [y/n]: ").strip().lower()
        if use_today == "y":
            return current_date()
        elif use_today == "n":
            while True:
                date = input("Enter date (YYYY-MM-DD): ")
                if validate_date(date):
                    return date
                print("❌ Invalid date format! Use YYYY-MM-DD.")
        else:
            print("❌ Answer must be 'y' or 'n'.")

def request_amount():
    while True:
        amount = input("Amount (numbers only): ")
        if amount.isdigit():
            return int(amount)
        print("❌ Amount must be a number!")
