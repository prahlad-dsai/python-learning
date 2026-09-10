import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = {}

while True:
    print("\n---EXPENSE TRACKER---")
    print("1. Add an expense")
    print("2. View expenses ")
    print("3. Show total")
    print("4. Quit")

    choice = input("Please select a choice: ")

    if choice == "1":
        name = input("Please name the expense: ")
        cost = float(input("Please enter the expense: "))
        expenses[name] = cost

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added!")
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet. Yay!")
        else:
            print("\nYour expenses")
            for name,cost in expenses.items():
                print(name, "-", cost)
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses yet. Yay!")
        else:
            total = sum(expenses.values())
            print("Your total expense is : ", total)
    elif choice == "4":
        print("Thank you. Please visit again.Goodbye")
        break
    else:
        print("Invalid choice.Please choose from 1 to 4")

