# tracker.py

def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks yet.")
    except FileNotFoundError:
        print("No tasks yet.")

def update_task(task_num, new_task):
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1] = new_task + "\n"
            with open("tasks.txt", "w") as f:
                f.writelines(tasks)
            print(f"Updated task {task_num} to: {new_task}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to update.")

def delete_task(task_num):
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if 0 < task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as f:
                f.writelines(tasks)
            print(f"Deleted task: {deleted.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")

def main():
    print("Task Tracker v1.0")
    print("Available commands: add, view, update, delete, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "view":
            view_tasks()
        elif command == "update":
            view_tasks()
            task_num = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            update_task(task_num, new_task)
        elif command == "delete":
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Command '{command}' not implemented yet.")

if __name__ == "__main__":
    main()