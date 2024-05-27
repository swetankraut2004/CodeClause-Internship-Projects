"""
Project ID - #CC9877
Project Title - Simple To-Do List App
Internship Domain - Python Development Intern
Project Level - Entry Level
Assigned By- CodeClause Internship
Assigned To - Swetank Kalyan Raut
Technology used - Python Development
Project Aim - Create a basic to-do list application that allows users to add, edit, and delete tasks.
"""

tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} [{status}]")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

def markTaskAsCompleted():
    listTasks()
    try:
        taskToMark = int(input("Enter the # to mark as completed: "))
        if taskToMark >= 0 and taskToMark < len(tasks):
            tasks[taskToMark]["completed"] = True
            print(f"Task {taskToMark} has been marked as completed.")
        else:
            print(f"Task #{taskToMark} was not found.")
    except:
        print("Invalid input.")

def removeCompletedTasks():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]
    print("All completed tasks have been removed.")

def editTask():
    listTasks()
    try:
        taskToEdit = int(input("Enter the # to edit: "))
        if taskToEdit >= 0 and taskToEdit < len(tasks):
            newTaskDescription = input("Enter the new description: ")
            tasks[taskToEdit]["task"] = newTaskDescription
            print(f"Task {taskToEdit} has been updated.")
        else:
            print(f"Task #{taskToEdit} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Mark a task as completed")
        print("5. Remove all completed tasks")
        print("6. Edit a task")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            markTaskAsCompleted()
        elif choice == "5":
            removeCompletedTasks()
        elif choice == "6":
            editTask()
        elif choice == "7":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
