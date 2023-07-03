Program README
This program is a task management system that allows users to perform various operations such as login, user registration, adding tasks, viewing tasks, marking tasks as complete, generating reports, and displaying statistics. The program uses two text files, "user.txt" and "tasks.txt", to store user information and task details, respectively.

Functions
login()
This function prompts the user to enter their username and password. It reads the "user.txt" file and checks if the entered username and password match any existing user. If a match is found, it returns the username and prints a welcome message. If no match is found, it displays an error message and prompts the user to try again.

reg_user()
This function allows an eligible user with the username "admin" to register new users. It prompts the admin user to enter the username and password for the new user. It checks if the desired username is already in use and if the entered password matches the confirmation. If the conditions are met, it adds the new user to the "user.txt" file. Otherwise, it displays appropriate error messages.

add_task()
This function allows a user to add a new task. It prompts the user to enter the username of the person the task is assigned to, the task title, description, and due date. It checks if the assigned username is registered in the "user.txt" file and validates the due date format. If the validations pass, it adds the task details to the "tasks.txt" file and prints the details of the newly added task.

view_all()
This function displays all the tasks stored in the "tasks.txt" file. It reads the file and prints the details of each task, including the username, task title, description, date assigned, due date, and completion status.

view_mine(username)
This function displays the tasks assigned to a specific user. It takes the username as an argument and searches for tasks assigned to that user in the "tasks.txt" file. If any tasks are found, it prints the details of each task, including the task number, username, task title, description, date assigned, due date, and completion status.

mark_complete(username)
This function allows a user to mark their assigned tasks as complete. It takes the username as an argument and searches for incomplete tasks assigned to that user in the "tasks.txt" file. If any incomplete tasks are found, it displays them with corresponding task numbers and prompts the user to enter the task number they want to mark as complete. It updates the task details and marks the selected task as complete in the "tasks.txt" file.

generate_reports()
This function generates two reports: "task_overview.txt" and "user_overview.txt". It reads the "tasks.txt" and "user.txt" files to obtain task and user information, respectively. It calculates statistics such as total tasks, completed tasks, uncompleted tasks, overdue tasks, percentages of incomplete tasks, and percentages of overdue tasks. It then writes the statistics to the corresponding report files.

display_statistics()
This function displays the generated reports. It tries to open and read the "task_overview.txt" and "user_overview.txt" files. If the files are found, it prints the report headings followed by the report contents. If any of the files are not found, appropriate error messages are displayed.


File Structure:
               user.txt: This file stores user information in the format: 
               username;password.

               tasks.txt: This file stores task details in the format: assigned_to;title;description;date_assigned;due_date;completed.

               The task_overview.txt file will contain the generated task overview report, which includes statistics such as total tasks, completed tasks, uncompleted tasks, and overdue tasks. And you will get when you run the program.

               The user_overview.txt file will contain the generated user overview report, which includes statistics such as total users, total tasks assigned to each user, and percentage of completed tasks for each user.  And you will get when you run the program.