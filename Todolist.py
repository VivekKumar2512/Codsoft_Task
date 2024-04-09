import json
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.name} - Due: {task.due_date} - Priority: {task.priority}")

def add_task(tasks):
    name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append(Task(name, due_date, priority))
    save_tasks([task.__dict__ for task in tasks])
    print("Task added successfully!")

def remove_task(tasks):
    display_tasks(tasks)
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks([task.__dict__ for task in tasks])
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

def main():
    print("VIVEK to DO LIST")
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()