import json
import os


file_name = "tasks.json"


if os.path.exists(file_name):
    with open(file_name, "r") as f:
        tasks = json.load(f)
else:
    tasks = []


def save_tasks():
    with open(file_name, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    task_name = input("Enter task name: ")
    status = "Pending"
    task = {"Task": task_name, "Status": status}
    tasks.append(task)
    save_tasks()
    print(f" Task '{task_name}' added successfully!")


def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['Task']} — {task['Status']}")


def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            print("1. Change Task Name\n2. Change Status")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_name = input("Enter new task name: ")
                tasks[task_no - 1]["Task"] = new_name
            elif choice == "2":
                new_status = input("Enter new status (Pending/Completed): ")
                tasks[task_no - 1]["Status"] = new_status
            else:
                print("Invalid choice.")
                return
            save_tasks()
            print(" Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted_task = tasks.pop(task_no - 1)
            save_tasks()
            print(f"Task '{deleted_task['Task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print(" Exiting To-Do List. Have a productive day!")
        break
    else:
        print("Invalid choice! Please try again.")
