user_choice = -1
tasks = []


def show_tasks():
    task_index = 0
    for task in tasks:
        print("[" + str(task_index) + "]" + task)
        task_index += 1

def add_task():
    task = input("Write your task: ")
    tasks.append(task)
    print("Task added!")

def del_task():
    task_index = int(input("Write index of task to delete: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("There is no task with that index")
        return
    tasks.pop(task_index)
    print("Task deleted")


def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
        file.close()

def load_tasks_from_file():
    try:   
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()

while user_choice != 5:

    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        del_task()

    if user_choice == 4:
        save_tasks_to_file()
        
    print()
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save to file")
    print("5. Exit")

    user_choice = int(input("Choose number: "))