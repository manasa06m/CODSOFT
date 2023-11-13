import os

def display_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    else:
        print("No to-do list found. Create a new task.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the to-do list.")

def del_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if 1 <= index <= len(tasks):
            deleted_task = tasks.pop(index - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{deleted_task.strip()}' deleted from the to-do list.")
        else:
            print("Invalid task index. Please provide a valid index.")
    else:
        print("No to-do list found. Create a new task.")

# Main menu
while True:
    print("\n1. Display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        new_task = input("Enter the task: ")
        add_task(new_task)
    elif choice == "3":
        task_index= int(input("Enter the task index to delete: "))
        del_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
