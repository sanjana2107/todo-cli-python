import json
import os

FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                tasks.pop(index)
                save_tasks(tasks)
                print("Task deleted!")
            except:
                print("Invalid choice!")

        elif choice == "4":
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
    
