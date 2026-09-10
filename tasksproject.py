tasks = []
while True:
    print("---TO - DO -LIST ---")
    print("1.Add a task.")
    print("2.View all tasks")
    print("3.Remove a task")
    print("4.Quit")

    choice = int(input("Enter a number from 1 to 4:"))

    if choice == 1:
        task = input("Enter a task:")
        tasks.append(task)
        print("Task added!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            print("\nYour tasks")
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks")
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

            task_number = int(input("Enter the number of the task to be removed:"))
            removed_task = tasks.pop(task_number - 1)
            print("Removed:", removed_task)
    elif choice == 4:
        print("Goodbye! Please visit again.")
        break
    else:
        print("Please enter a number from 1 to 4.")

