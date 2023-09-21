#!/usr/bin/env python

# Create an empty list to store tasks
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to remove a task from the list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' has been removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the current to-do list
def show_tasks():
    if to_do_list:
        print("\nTo-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
