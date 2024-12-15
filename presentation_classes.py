# --------------------------------------------------------------------------- #
# Title:  Assignment 08 - Presentation Classes
# Description: This file contains input and output class IO.
##
# Change Log:
# 12/01/2024: Establish file by breakout from main.py
#12/10/2024: Checking for Test development
# 12/12/2024: Last review and prep for submission
#
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #
from processing_classes import FileProcessor
from data_classes import Employee



# Define Constants:
MENU: str = '''
 ----Employee Ratings----------
 Please select from the following menu:
 1. Show current employee rating data. 
 2. Enter new employee rating data.
 3. Save data to a file.  
 4. Exit the program.
 -------------------------------
 '''

#variables
exit_statement: str = "'Thank you. Goodbye.'"

class IO:
    """
        A collection of functions that manage user input and output.
   """

    @staticmethod
    def input_employee_data( ) -> Employee:
        """Accepts information entered by user as string and formats as a dictionary
        Appends it to an employee_file.
        """

        while True:
            try:
                employee_first_name = input("What is your first name? ").strip().title()
                employee_last_name = input("What is your last name? ").strip().title()
                employee_review_date = input("Please enter date of review (YYYY-MM-DD): ").strip()
                employee_review_rating = int(input("Please enter the Employee Rating. Possible ratings are 1 through 5:  "))
                return Employee(employee_first_name, employee_last_name, employee_review_date, employee_review_rating)
            except ValueError as e:
                FileProcessor.output_error_messages("Please try again", e)
            except Exception as e:
                FileProcessor.output_error_messages("That value is not the correct type of data!", e)


    @staticmethod
    def output_employee_ratings(employee_ratings: list):
        """
        Prints the list all_employee_list.
        all_employee_list: list of dictionaries
        """
        for employee in employee_ratings:
            print(f'{employee.first_name} {employee.last_name} received a '
                  f'rating of {employee.review_rating} on {employee.review_date}')

    @staticmethod
    def input_menu_choice() -> str:
        """
        Used when menu choice is 1 to collect input
        returns the choice made.

        """
        print(MENU)
        choice: str = input(
            "Please make a choice from the menu above (1/2/3/4)  ")
        return choice

    @staticmethod
    def welcome_str_menu():
        """
       Prints a welcome statement and asks if the user to interact with the menu.

        """
        welcome_str = input(
            "Welcome! Would you like to interact with Employee Rating? (Y/N)  ")
        if welcome_str.upper() == 'Y':
            return
        print(exit_statement)
        exit()

if __name__ == '__main__':
    print("This file is not meant to be run. Please run main.py")
