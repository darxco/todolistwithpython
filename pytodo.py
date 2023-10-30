import os

def welcome():
    print("Welcome to your to-do list!")
    print('To view your tasks, please write "Tasks"')
    print('To add a task to your list, please write "Add"')
    print('To exit the app, please write "Exit"')


def show_tasks():
    with open("tasks.txt", "r") as file:
        tasks_list = file.read()
        if tasks_list:
            print("This is your list:\n" + tasks_list)
            action = input('To add a task, type "A"; to remove a task, type "R"; to reset the list, type "Reset"; to exit, type "E": ').lower()
            if action == "a":
                add_tasks()
                
            elif action == "r":
                remove_tasks()
                
            elif action == "reset":
                reset_list()
                
        else:
            print("Your list is empty.")
            action = input('To add a task, type "A"; to reset the list, type "Reset"; to exit, type "E": ').lower()
            if action == "a":
                add_tasks()
                
            elif action == "reset":
                reset_list()
                

def reset_list():
    with open("tasks.txt", "w") as file:
        file.truncate(0)
    print("Your to-do list has been reset.")
    show_tasks()

def add_tasks():
    new_task = input("What is the task you want to add? - ")

    with open("tasks.txt", "a") as file:
        file.write(f"Task {len(open('tasks.txt', 'r').readlines()) + 1}: {new_task}\n")

    print("Added, this is your new list:")
    show_tasks()

def remove_tasks():
    with open("tasks.txt", "r") as file:
        tasks_list = file.readlines()
        if tasks_list:
            print("This is your list:")
            for index, task in enumerate(tasks_list, 1):
                print(f"Task {index}: {task.strip()}")

            try:
                task_to_remove = int(input("Which task do you want to remove? (Enter the task number):"))
                if 1 <= task_to_remove <= len(tasks_list):
                    task_index = task_to_remove - 1
                    deleted_task = tasks_list.pop(task_index)

                    with open("tasks.txt", "w") as file:
                        file.writelines(tasks_list)

                    print(f"Deleted task: {deleted_task.strip()}")
                    print("This is your new list:")
                    show_tasks()
                else:
                    print("Select a valid task number.")
            except ValueError:
                print("Please enter a valid task number.")

        else:
            print("Your list is empty.")
            show_tasks()
welcome()
def main():
    valid_actions = ["add", "tasks" , "exit"]
    user_input = input("").lower()

    if user_input not in valid_actions:
        print("Please select one of the options above.")
        main()
    else:
        if user_input == "add":
            add_tasks()
        elif user_input == "tasks":
            show_tasks()
        elif user_input == "exit":
            pass

if os.path.exists("tasks.txt"):
    main()
else:
        print("Task file not found. Creating it ...")
        open("tasks.txt" , "x")