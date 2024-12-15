# --------------------------------------------------------------------------- #
# Title:  Assignment 08
# Main.py
# Description: This script will collect information from a
# person. The user will be able to
#  display a message about an Employee's rating.
# We are implementing Unit Testing and use of modules.
# Three module files include: data_classes.py, presentation_classes.py and
# processing_classes.py.
#
# Change Log:
# 11/28/2024: Beginning script outline by coping over A07.
# 11/29/2024: Making a list of needed updates to make this A08
# 11/30/2024: Added Employee class, adding additional input questions
# with formating to check for date. Split into modules and updated as needed.
# 12/01/2024:
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #

from processing_classes import FileProcessor
from data_classes import Employee
from presentation_classes import IO


# Define constants:
MENU: str = '''
 ----Employee Ratings----------
 Please select from the following menu:
 1. Show current employee rating data. 
 2. Enter new employee rating data.
 3. Save data to a file.  
 4. Exit the program.
 -------------------------------
 '''
FILE_NAME: str = "EmployeeRatings.json"

# Define variables
menu_choice: str = ''
all_employee_list: list = []  # A table of Employee Rating data.
exit_statement: str = "'Thank you. Goodbye.'"
#fileprocessor.read.employee_data_from_file
#where it all happens
all_employee_list: list[Employee] = FileProcessor.load_employee_data(FILE_NAME)
IO.welcome_str_menu()  # Provides a greeting and menu for input
while True:
    menu_choice = IO.input_menu_choice()
    if menu_choice == str(1):
        IO.output_employee_ratings(all_employee_list)
    elif menu_choice == str(2):
        next_employee_data = IO.input_employee_data()
        all_employee_list.append(next_employee_data)
        #print(all_employee_list)
    elif menu_choice == str(3):
        FileProcessor.write_data_to_file(all_employee_list, FILE_NAME)
        print(f"Your data was saved to the {FILE_NAME} file.")
    elif menu_choice == str(4):
        print(exit_statement)
        quit()
    else:
        print ("That was not a correct entry. Please enter 1, 2, 3, or 4")
