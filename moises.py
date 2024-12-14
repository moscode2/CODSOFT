# File: moises.py

import json

class ToDoList:
    def __init__(self, file_name="tasks.json"):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()
    
    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\nYour To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{idx}. {task['description']} [{status}]")
    
    def update_task(self, task_number, new_description=None, completed=None):
        if 0 < task_number <= len(self.tasks):
            if new_description:
                self.tasks[task_number - 1]["description"] = new_description
            if completed is not None:
                self.tasks[task_number - 1]["completed"] = completed
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed['description']}")
        else:
            print("Invalid task number.")
    
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def main():
    todo = ToDoList()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            try:
                task_num = int(input("Enter task number to update: "))
                desc = input("Enter new description (or leave blank): ").strip()
                completed = input("Mark as completed? (y/n): ").strip().lower() == "y"
                todo.update_task(task_num, desc if desc else None, completed)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                task_num = int(input("Enter task number to delete: "))
                todo.delete_task(task_num)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            todo.save_tasks()
        elif choice == "6":
            todo.load_tasks()
        elif choice == "7":
            todo.save_tasks()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
