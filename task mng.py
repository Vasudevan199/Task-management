import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Display the menu
def display_menu():
    print("\nTask Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"id": len(tasks) + 1, "name": task_name})
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Name: {task['name']}")

# Update an existing task
def update_task(tasks):
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task['id'] == task_id:
            new_name = input("Enter the new task name: ")
            task['name'] = new_name
            print("Task updated successfully!")
            return
    print("Task not found!")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found!")

# Main function to run the task management system
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
