# 💸 Expense Tracker CLI (Python)

A simple terminal-based application to track your daily expenses — fully written in Python using the standard library!

---

## 📌 Features

- ✅ Add expenses with date, category, description, and amount
- 📅 View all expense history
- 📂 View total spending grouped by category
- 📊 View total spending grouped by date
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
[5] Exit
```

---

## 📂 Project Structure

```
expense-tracker/
├── core/
│   ├── tracker.py          # Main logic for managing expenses
│   └── utils.py            # Helper functions (validation, input, formatting)
├── reports/
│   └── summary.py          # Summary reports by category/date
├── data/
│   └── expenses.json       # Local JSON data storage
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

### 2. Run the app

```bash
python main.py
```

> No external libraries required. Uses Python's standard library only.

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
- Works on Windows, macOS, or Linux

---

## 📄 License

MIT License — Free to use, modify, and share.

---

> Made with ❤️ by Zaki Andriansa — feel free to fork or contribute!
