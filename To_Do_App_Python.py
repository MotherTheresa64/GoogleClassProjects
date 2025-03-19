# To_Do_App_Python
# Noah Ragan 2/24/2025

def main():
    # Create a list to store tasks
    tasks = []
    
    # Display a welcome message to the user
    print("Welcome to the To Do App!")
    
    # Display the menu and loop until the user chooses to Quit
    while True:
        print("\nTo-Do Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break  # Exits the loop and ends the program
        else:
            print("Invalid choice. Please try again.")

def add_task(tasks):
    # Get the task from the user
    task = input("Enter the task: ")
    # Add the task to the list
    tasks.append(task)
    # Display a message to the user
    print("Task added!")

def view_tasks(tasks):
    # Check if there are any tasks
    if len(tasks) == 0:
        print("No tasks to do!")
    else:
        # Loop through the task list and display all of them
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    print("\n-------------END OF LIST-----------------")

def delete_task(tasks):
    # Check if there are any tasks
    if len(tasks) == 0:
        print("There are no tasks to delete!")
    else:
        # Display all the tasks
        view_tasks(tasks)
        # Get the task number to delete
        task_number = int(input("Enter the task number to delete: "))
        # Check if the task number is valid
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
        else:
            # Delete the task
            del tasks[task_number - 1]
            # Display a message to the user
            print("Task deleted!")
# Call the main function to run the program to run soley in this program
if __name__ == '__main__':
    main()