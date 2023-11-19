# A simple To-Do List application in Python

tasks = []

def add_task():
    task_description = input("Enter task description: ")
    tasks.append(task_description)
    print("Task added successfully!")

def list_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_number < len(tasks):
            new_description = input("Enter the new task description: ")
            tasks[task_number] = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
