# 💸 Expense Tracker CLI (Python)

A simple terminal-based application to track your daily expenses — fully written in Python using the standard library!

---

## 📌 Features

- ✅ Add expenses with date, category, description, and amount
- 📅 View all expense history
- 📂 View total spending grouped by category
- 📊 View total spending grouped by date
- 📊 View total spending grouped by month
- 📝 Export expenses to CSV
- 📝 Import expenses from CSV
- 💾 All data saved locally in a JSON file (`data/expenses.json`)
- 🧠 Easy to understand and extend — great for beginners!

---

## 🖼️ Preview

```bash
===============================
Expense Tracker Application
===============================
[1] Add Expense
[2] View All Expenses
[3] Total by Category
[4] Total by Date
[5] Total by Month
[6] Export data to csv
[7] Import data from csv
[8] Exit
```

---
## 🎥 Short Demo
```bash
[Version 1.2.1 (Latest)] https://drive.google.com/file/d/1MJwLyISM1jsFVyb15SWiLfy2SyWi5Wqa/view?usp=drive_link
[Version 1.2.0] https://drive.google.com/file/d/1wIbNfqCD71YRQUUgh729FbAfCU9VuqSl/view?usp=drive_link
[Version 1.1.1] https://drive.google.com/file/d/1IUfg_a2Iqyw9vhoxgpgyJBMzVjVE92w_/view?usp=drive_link
[Version 1.1.0] https://drive.google.com/file/d/1cUwGf6cJMwqGfypLMn4n0ueuI9dCI69E/view?usp=drive_link
[Version 1.0.0] https://drive.google.com/file/d/1h5dWleLJUOxuOcLQRH_4PuxO4sgmGZcH/view?usp=drive_link
```
---

## 📖 Changelog

### v1.2.1 (2025-08-10)
- 🛠 Added validation check before saving expense data

---

### v1.2.0 (2025-08-10)
- ➕ Added feature: Export expenses to CSV
- ➕ Added feature: Import expenses from CSV

---

### v1.1.1 (2025-08-05)
- 📅 Sorted monthly report from January to December for clearer chronological order

---

### v1.1.0 (2025-08-05)
- ➕ Added feature: Total by Month
- 🎨 Improved CLI layout for better readability and cleaner appearance with tabulate library

---

### v1.0.0 (2025-08-05)
- 🚀 Initial release with features:
    - Add Expense 
    - View All Expenses 
    - Total by Category 
    - Total by Date


## 📂 Project Structure

```
expense-tracker/
├── core/
│   ├── tracker.py          # Main logic for managing expenses
│   └── utils.py            # Helper functions (validation, input, formatting)
├── reports/
│   └── summary.py          # Summary reports by category/date
├── data/
│   ├── expenses.json       # Local JSON data storage
│   └── backup_expense.csv  # CSV for import
├── main.py                 # CLI interface entry point
├── requirements.txt        # List of dependencies (if needed)
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/ZakiAndriansa/expense-tracker.git
cd expense-tracker
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python main.py
```

---

## 🧪 Example Data (`data/expenses.json`)

```json
[
  {
    "date": "2025-08-04",
    "category": "Food",
    "description": "Padang Satay",
    "amount": 15000
  },
  {
    "date": "2025-02-14",
    "category": "Food",
    "description": "Birthday Cake",
    "amount": 90000
  },
  {
    "date": "2025-08-04",
    "category": "Transport",
    "description": "Biskita Bus",
    "amount": 3000
  }
]
```

---

## 🛠 Requirements

- Python 3.13 or newer
- Everything in requirements.txt
- Works on Windows, macOS, or Linux

---

## 📄 License

MIT License — Free to use, modify, and share.

---

> Made with ❤️ by Zaki Andriansa — feel free to fork or contribute!
