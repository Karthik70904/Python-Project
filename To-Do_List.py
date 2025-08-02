tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"✅ '{task}' added to your list.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter the task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"❌ '{removed}' has been removed.")
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("Please enter a valid option (1-4).")
