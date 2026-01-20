from datetime import date, timedelta 
import os
todo_list = []
complete = []
uncomplete = []
weekly_tasks=[]
important_tasks=[]
todays_task=[]
tasks=[]
def main_main():
    option = int(input("Choose 1 for daily and 2 for weekly planner."))
    if option == 1:
        daily_todo()
    elif option == 2:
        weekly_todo()
    else:
        print("Input not found!")
        
def daily_todo():
    mainn()
    
def weekly_todo():
    mainn()
    
def mainn():    
    print("=== TO-DO LIST ===")
    print(todo_list)
    
    print("=== Completed tasks ===")
    print(complete)
    
    print("=== Uncompleted tasks ===")
    print(uncomplete)
    
    print("=== MAIN MENU ===")
    print("1. Add New Task")
    print("2. Remove Task")
    print("3. Edit Task")
    print("4. Mark Task as Completed")
    print("5. Mark Task as Uncomplete")
    print("6. Prioritize task")
    print("7. Edit todays task")
    print("8. Enter task with due date")
    print("9. Exit")
    choice = int(input("Enter your choice (1-9): "))
    if choice == 1:
        addd()
    elif choice == 2:
        removee()
    elif choice == 3:
        edit()
    elif choice == 4:
        completed()
    elif choice == 5:
        uncompleted()
    elif choice == 6:
        prioritized_tasks()
    elif choice == 7:
        priority()   
    elif choice == 8:
        tasks()
    elif choice == 9:
        os._exit(0)
    else:
        print("Invalid input.")
        
def addd():
    taask = input("Enter new task: ")
    todo_list.append(taask)
    print("Task added.")
def removee():
    taskkk = input("Enter the task to remove: ")
    if taskkk in todo_list:
        todo_list.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")
        
def completed():
    tassk = input ("Enter to comp 1: ")
    if tassk in todo_list:
        todo_list.remove(task)
        complete.append (task)
        print("Mark as done.")
    else:
        print("Task not found.")
        
def uncompleted():
    ttask = input ("Enter to uncomp 1: ")
    if ttask in complete:
        complete.remove(task)
        todo_list.append(task)
        print("Mark as uncomplete.")
    else:
        print("Task not found.")
        
def edit():
    task1 = input("Enter the task to edit: ")
    if task1 in todo_list:
        task2 = input("Enter the name of the task: ")
        index = todo_list.index(task1)
        todo_list[index] = task2
        print("Edit done.")
    else:
        print("Error, try again.")
today = date.today()
def priority():
    for t in tasks:
        if t[1] == today:
            todays_task.append(t) 
        elif t[1] < today:
            print("missed task")
        else :
            print("we will send a notification when it is the due date")
def prioritized_tasks():
    important_tasks.insert(input(0,"enter task to prioratize"))
def tasks():
    taskk== input("Enter task")
    date_str = input("Enter due date in the dd/m/yyyy format: ")
    for x in taskk:
        tasks.append([taskk, date_str])
        for i in range(7):
            weekly_tasks.append(today+timedelta(days=i))

while True:
    main_main()
