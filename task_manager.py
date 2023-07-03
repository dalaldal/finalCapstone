import os
from datetime import datetime
import sys                                              


DATETIME_STRING_FORMAT = "%Y-%m-%d"

def login():
    while True:
        # Prompt the user to enter their username and password
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        # Open the "user.txt" file for reading
        with open("user.txt", "r") as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line by the ";" delimiter and strip leading/trailing whitespace
                user_info = line.strip().split(";")

                # Check if the line contains at least two elements (username and password)
                # and if the entered username and password match the current line
                if len(user_info) >= 2 and user_info[0] == username and user_info[1] == password:
                    # Print a welcome message with the username and return the username
                    print(f"Welcome, {username}!")
                    return username
        # If no match is found, display an error message and continue to the next iteration
        print("Invalid username or password. Please register first")


def reg_user():
    # Prompt the user to enter their username to check if they are eligible to register users
    print("Enter your name if you are eligible to register users")
    username = input("Enter your username: ")

    # Check if the entered username is "admin" to determine eligibility
    if username == "admin":
        # Prompt the admin user to enter the username and password for the new user
        reg_username = input("Enter the username you want to register: ")
        reg_password = input("Enter the password you want to assign to the user: ")
        confirm = input("Confirm the password: ")

        # Read the contents of the "user.txt" file
        with open("user.txt", "r") as file:

            # Create a list of existing usernames by extracting the first element of each line
            users = file.readlines()
            user_list = [user.strip().split(";")[0] for user in users]
            if reg_username in user_list:
                print("Username already exists. Please try again with a different username.")
                return
            
        # Check if the desired username is already in use
        if reg_password == confirm:
            # Open the "user.txt" file in append mode and add the new username and password
            with open("user.txt", "a") as file:
                file.write(f"\n{reg_username};{reg_password}")
            print("User registration successful.")
        else:
            print("Passwords do not match. Please try again.")
    else:
        print("You are not eligible to register users. Goodbye.")


def add_task():
    # Prompt the user to enter the username of the person the task is assigned to
    assigned_to = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the task title: ")
    description = input("Enter a description of the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD) of the task: ")
    
    # Read the contents of the "user.txt" file
    with open("user.txt", "r") as file:
        users = file.readlines()

        # Create a list of existing usernames by extracting the first element of each line
        user_list = [user.strip().split(";")[0] for user in users]

        # Check if the assigned username is not registered
        if assigned_to not in user_list:
            print("User is not registered. Goodbye.")
            return
        
    # Validate the due date format
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the due date in the format YYYY-MM-DD.")
        return
    
    # Get the current date as the date assigned to the task
    date_assigned = datetime.today().strftime("%Y-%m-%d")
    
    # Open the "tasks.txt" file in append mode and add the new task details
    with open("tasks.txt", "a") as file:
        file.write(f"\n{assigned_to};{title};{description};{date_assigned};{due_date};No")
    
    # Print the details of the newly added task
    print("\nNew task has been added")
    print("----------------------------------------------------")
    print("Username:\t" + assigned_to)
    print("Task Title:\t" + title)
    print("Description:\t" + description)
    print("Date Assigned:\t" + date_assigned)
    print("Due Date:\t" + due_date)
    print("Completed:\tNo")
    print("----------------------------------------------------")



def view_all():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    # Check if there are no tasks
    if not tasks:
        print("No tasks found.")
    else:
        print("All Tasks:")
        # Iterate over each task
        for task in tasks:
            line = task.strip().split(";")
            if len(line) >= 6:
                # Print the details of the task
                print("----------------------------------------------------")
                print("Username:\t" + line[0])
                print("Task Title:\t" + line[1])
                print("Description:\t" + line[2])
                print("Date Assigned:\t" + line[3])
                print("Due Date:\t" + line[4])
                print("Completed:\t" + line[5])
            else:
                print("Invalid task format.")

def view_mine(username):
    # Initialize variables
    user_found = False
    my_tasks = []
    print("\nView My Tasks")
    
    # Read the contents of the "tasks.txt" file
    with open("tasks.txt", "r") as file:
        for line in file:
            # Split the line into individual task details using the ";" delimiter
            task = line.strip().split(";")
            if username == task[0]:
                my_tasks.append(task)
                user_found = True

    # If the user is found, print each task assigned to the current
    # user and add a task number to each task.
    if user_found:
        count = 0
        for i, task in enumerate(my_tasks):
            count += 1
            print(f"\nTask {count}")
            print("----------------------------------------------------")
            print("Username:\t" + task[0])
            print("Task Title:\t" + task[1])
            print("Description:\t" + task[2])
            print("Date Assigned:\t" + task[3])
            print("Due Date:\t" + task[4])
            print("Completed:\t" + task[5])
            print("----------------------------------------------------")


def mark_complete(username):
    user_tasks = []
    task_indices = []

 # Read the contents of the "tasks.txt" file
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # Iterate through the tasks to find the incomplete tasks assigned to the user
    for i, task in enumerate(tasks):
        if task.startswith(username) and task.strip().split(";")[-1] == "No":
            user_tasks.append(task.strip().split(";"))
            task_indices.append(i)

    # Check if the user has any incomplete tasks
    if len(user_tasks) == 0:
        print("User does not have any incomplete tasks.")
        return
    
    # Print the incomplete tasks with corresponding task numbers
    print("My Incomplete Tasks:")
    for i, task in enumerate(user_tasks, 1):
        print(f"{i}. {task[1]}")

    # Prompt the user to enter the task number to mark as complete
    task_number = int(input(f"Enter the number of the task you want to mark as complete (1 to {len(user_tasks)}): "))
    
    # Check if the entered task number is valid
    if task_number < 1 or task_number > len(user_tasks):
        print("Invalid task number")
        return
    
     # Mark the selected task as complete by updating the task details
    task_index = task_indices[task_number - 1]
    tasks[task_index] = ";".join(user_tasks[task_number - 1]) + "\n"
    tasks[task_index] = tasks[task_index].replace(";No", ";Yes")

    # Write the modified task list back to the "tasks.txt" file
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

    print("Task marked as complete.")

# This line defines a function named generate_reports.
def generate_reports():

    #This code block opens a file named "tasks.txt" 
    # in read mode and reads its contents into a list called tasks.
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # This code block opens a file named "user.txt" 
    # in read mode and reads its contents into a list called users.
    with open("user.txt", "r") as file:
        users = file.readlines()
 
    """
    These lines initialize variables to keep track of 
    the total number of tasks, completed tasks, uncompleted tasks, 
    and overdue tasks.
    """
    total_tasks = len(tasks)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    """
    This loop iterates over each task in the tasks list.
    It splits each task into individual pieces of information using the 
    semicolon (;) as the delimiter and stores them.
    if the sixth element of task_info is equal to "Yes", the task is 
    considered completed, and the completed_tasks count is incremented.
    f the sixth element is not "Yes", the task is considered 
    uncompleted. The code increments the uncompleted_tasks
    """
    for task in tasks:
        task_info = task.strip().split(";")
        if task_info[5] == "Yes":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            due_date = datetime.strptime(task_info[4], "%Y-%m-%d").date()

            if due_date < datetime.today().date():
                overdue_tasks += 1

    """
    These lines calculate the percentages of incomplete tasks and 
    overdue tasks based on the counts obtained earlier.
    """
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

    """
    This code block opens a file named "task_overview.txt" in write 
    mode and writes the task-related statistics to it.
    """
    with open("task_overview.txt", "w") as file:
        file.write("Task Overview\n")
        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed_tasks}\n")
        file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue tasks: {overdue_tasks}\n")
        file.write(f"Percentage of incomplete tasks: {incomplete_percentage:.2f}%\n")
        file.write(f"Percentage of overdue tasks: {overdue_percentage:.2f}%\n")

    # This code counts the number of unique users from the tasks.
    # The total number of unique users is calculated based on the count of elements in the unique_users set
    unique_users = set(task.strip().split(";")[0] for task in tasks)
    total_users = len(unique_users)


    """
    This code block opens a file named "user_overview.txt" in write mode and writes 
    the header information for the user overview section, 
    """
    with open("user_overview.txt", "w") as file:
        file.write("User Overview\n")
        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n")

        """
        This block iterates over each unique user in the unique_users
        For each user, it extracts user information, splits it using a semicolon as the delimiter
        It filters the tasks list to find the tasks assigned to the current user 
        T
        """
        for user in unique_users:
            user_info = user.strip().split(";")
            user_tasks = [task for task in tasks if task.startswith(user)]
            user_task_count = len(user_tasks)
            user_task_percentage = (user_task_count / total_tasks) * 100 if total_tasks > 0 else 0
            
            """
            the number of tasks assigned to the user (user_task_count) is
            calculated based on the count of elements in user_tasks.
            The overdue tasks assigned to the user are calculated 
            The percentage of overdue tasks out of the assigned tasks 
            """
            completed_user_tasks = [task for task in user_tasks if task.strip().split(";")[5] == "Yes"]
            completed_user_task_percentage = (len(completed_user_tasks) / user_task_count) * 100 if user_task_count > 0 else 0
            uncompleted_user_tasks = [task for task in user_tasks if task.strip().split(";")[5] == "No"]
            overdue_user_tasks = sum(1 for task in uncompleted_user_tasks if datetime.strptime(task.strip().split(";")[3], "%Y-%m-%d").date() < datetime.today().date())
            overdue_user_task_percentage = (overdue_user_tasks / user_task_count) * 100 if user_task_count > 0 else 0

            file.write("\n")
            file.write(f"User: {user}\n")
            file.write(f"Total tasks assigned: {user_task_count}\n")
            file.write(f"Percentage of total tasks assigned: {user_task_percentage:.2f}%\n")
            file.write(f"Percentage of completed tasks: {completed_user_task_percentage:.2f}%\n")
            file.write(f"Percentage of tasks to be completed: {(100 - completed_user_task_percentage):.2f}%\n")
            file.write(f"Percentage of overdue tasks: {overdue_user_task_percentage:.2f}%\n")

    print("Reports generated successfully.")



"""
This code responsible for reading and displaying the generated reports.
It tries to open and read the "task_overview.txt" file, 
which contains the task overview report. If the file is found, 
it reads its contents and prints the report heading 
followed by the report content.
If the "task_overview.txt" file is not found, 
it catches the FileNotFoundError 
Similarly, it tries to open and read the "user_overview.txt" file, 
If the file is found, it reads its contents.
If the "user_overview.txt" file is not found, 
 
"""
def display_statistics():
    try:
        with open("task_overview.txt", "r") as file:
            task_report = file.read()
            print("Task Overview:")
            print(task_report)
    except FileNotFoundError:
        print("Task overview report not found.")

    try:
        with open("user_overview.txt", "r") as file:
            user_report = file.read()
            print("\nUser Overview:")
            print(user_report)
    except FileNotFoundError:
        print("User overview report not found.")



# Main program loop
def main():

    # initializes the username variable to None
    username = None  # Initialize the username variable
    
    # The code enters an infinite loop, 
    # displaying a menu of options for the user to choose from.
    while True:
        print("\n===== Task Manager =====")
        print("log. Login")
        print("r. Register User")
        print("a. Add Task")
        print("va. View All Tasks")
        print("vm. View My Tasks")
        print("mc. Mark Task as Complete")
        print("gr. Generate Reports")
        print("ds. Display Reports")
        print("e. Exit")
        # Based on the user's choice, different functions are called.
        #he username variable is updated with the result of the login function 
        # if the user chooses to log in.
        #Conditional checks are used to enforce certain conditions
        choice = input("Enter your choice (1-10): ")
        if choice == "log":
            username = login()  # Assign the username after successful login
        elif choice == "r":
            reg_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all()
        elif choice == "vm":
            if username:
                view_mine(username)
            else:
                print("Please login first.")
        elif choice == "mc":
            if username:
                mark_complete(username)
            else:
                print("Please login first.")
        
        elif choice == "gr":
            if username == "admin":
                generate_reports()
            else:
                print("You do not have admin rights. Goodbye.")
        elif choice == "ds":
            if username == "admin":
                display_statistics()
            else:
                print("You do not have admin rights.")
        elif choice == "e":
            print("Exiting the program. ")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
     

## Run the main program

if __name__ == '__main__':
    main()