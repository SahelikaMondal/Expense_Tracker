import csv
import os

file_name = 'expenses.csv'

if not os.path.exists(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Description', 'Amount'])

def add_expense():
    date = input("Enter date(DD-MM-YYYY):")
    category = input("Enter category:")
    description = input("Enter description:")
    amount = float(input("Enter amount:"))
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

def view_expenses():
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expenses():
    total = 0
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['Amount'])
    print(f"Total expenses: Rs{total:.2f}")

def delete_expense():
    with open(file_name, 'r') as file:
        lines = file.readlines()
    if len(lines) <= 1:
        print("No expenses to found.")
        return
    print("Expenses:")
    for i in range(1, len(lines)):
        print(f"{i}. {lines[i].strip()}")
    choice = int(input("Enter the number of the expense to delete:"))
    if choice < 1 or choice >= len(lines):
        print("Invalid choice!")
        return
    lines.pop(choice)
    with open(file_name, 'w', newline='') as file:
        file.writelines(lines)
    print("Expense deleted successfully!")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Enter your choice number:")        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()