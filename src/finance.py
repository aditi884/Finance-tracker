import json
from datetime import datetime
from collections import defaultdict

transactions = []

def add_transaction():
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    desc = input("Description: ")
    income = input("Income? (y/n): ").lower() == 'y'
    transactions.append({
        "date": date,
        "amount": amount,
        "category": category,
        "desc": desc,
        "income": income
    })

def list_transactions():
    for t in transactions:
        print(f"{t['date']} | {'Income' if t['income'] else 'Expense'} | ${t['amount']:.2f} | {t['category']} | {t['desc']}")

def save_data():
    with open("data.json", "w") as f:
        json.dump(transactions, f)
    print("Saved.")

def load_data():
    global transactions
    try:
        with open("data.json") as f:
            transactions = json.load(f)
    except:
        print("No saved data.")

def filter_expenses_over(amount=100):
    for t in transactions:
        if not t['income'] and t['amount'] > amount:
            print(f"{t['date']} | ${t['amount']} | {t['category']} | {t['desc']}")

def monthly_chart():
    spend = defaultdict(float)
    for t in transactions:
        if not t['income']:
            month = t['date'][:7]
            spend[month] += t['amount']
    for m in sorted(spend):
        print(f"{m}: ${spend[m]:.2f} | {'#' * int(spend[m] // 10)}")

def menu():
    load_data()
    while True:
        print("\n1.Add 2.List 3.Filter >$100 4.Chart 5.Save 6.Exit")
        c = input("Choice: ")
        if c == "1": add_transaction()
        elif c == "2": list_transactions()
        elif c == "3": filter_expenses_over()
        elif c == "4": monthly_chart()
        elif c == "5": save_data()
        elif c == "6": break
        else: print("Invalid.")

if __name__ == "__main__":
    menu()
