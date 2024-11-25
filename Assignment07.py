# --------------------------------------------------------------------------- #
# Title:  Assignment 07
## Description: This Assignment 07 will collect information
# then display a message about a student's registration for
# a Python course. In this assignment, we are using classes.
#
# Change Log:
# 11/18/2024: Beginning script outline by coping over 06.
# 11/212024: First attempt to expand classes
# 11/23/2024: Big push to get this to work. Fixed issues with classes
# 11/24/2024: Most of the effort was on fixing File Processor
#
#
# Kristie Dunkin       11/25/2024     Assignment 07
# ------------------------------------------------------------------------------- #

import json

# Define Constants:
MENU: str = '''
 ----Course Registration Program Menu-----
 1. Register a student for a course 
 2. Show current data 
 3. Save data to a file 
 4. Exit this program
 '''

FILE_NAME: str = "Enrollments.json"

FIRST_NAME_KEY: str = "First Name"
LAST_NAME_KEY: str = "Last Name"
COURSE_NAME_KEY: str = "Course Name"

# Define variables
menu_choice: str = ''
all_students_list: list = []  # A table of student data. NOTE that this is the same variable as the assignment's "students".
exit_statement: str = "'Thank you. Goodbye.'"  # I added this myself, not a requirement.
#
# Declare the class.
class Person:
    _first_name: str
    _last_name: str
    """   Base Class  - Establishes a class of person objects with attributes of first and last name.

     Properties:
     -first_name(str): the person's first name.
     -last_name(str): the person's last name.

    """

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self._first_name = value
        else:
            raise ValueError("The first name should not be numerical. ")

    @property
    def last_name(self):
        return self._last_name.title()

    @last_name.setter
    def last_name(self, value):
        if value.isalpha() or value == "":
            self._last_name = value
        else:
            raise ValueError("The last name should not be numerical.")

    def __str__(self):
        return f'{self._first_name}, {self._last_name}'

class Student(Person):
    """A  class representing class registration data.
    Student class inherits some properties from the Person class.
    Properties:
    first_name(str): the person's first name - inherited.
    last_name(str): the person's last name - inherited.
    course_name(str):  course name.
    """
    _course_name: str = ''

    def __init__(self, first_name: str, last_name: str, course_name: str):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if value.isprintable():
            self._course_name = value
        else:
            raise ValueError("That is not a correct course name. ")

    def __str__(self):
        result = super().__str__()
        return f'{result}, {self.course_name}'

    def __repr__(self):
        result = super().__str__()
        return f'{result}, {self.course_name}'

class FileProcessor:
    """Reads data from JSON file and writes data to JSON file for storage"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays a custom error message to the user"""
        print(message, end="\n\n")
        if error is not None:
            print(f"--Error present, please correct --.")
            print(error, error.__doc__, type(error), end='\n')
            return

    @staticmethod
    def read_data_from_file(file_json: str) -> list[dict]:
        """
        Opens a .json file in read mode. Reads information into memory using load.
        Note that the file must already exist.
        @rtype: object
        @param file_json: str  string data with name of file to read from.
        @Param all_students_list: a list of dictionary rows to be fill with file data.
        @return: list
        """
        dict_table: list
        try:
            with open(file_json, "r") as file:
                dict_table = json.load(file)
            return dict_table
        except FileNotFoundError as e:
            FileProcessor.output_error_messages(
                "Sorry, your file was not found.", e)
            return []  # needed this because it was getting stuck here.
        except  json.JSONDecodeError as e:
            FileProcessor.output_error_messages(
                "There was an error decoding your file", e)
            raise e

    @staticmethod
    def load_student_data(student_data_file: str) -> list[Student]:
        raw_file_data = FileProcessor.read_data_from_file(student_data_file)
        student_list: list[Student] = list()
        for row in raw_file_data:
            student_list.append(Student(row[FIRST_NAME_KEY], row[LAST_NAME_KEY],
                                        row[COURSE_NAME_KEY]))
        return student_list

    @staticmethod
    def write_data_to_file(save_data: list[Student], file_location: str):
        """Saves data to a .json file. using open in write mode "w" .
       Note this is using a with, which will close the file for us.
       Saved data is formated using 'indent = 2' to look like a table.
       @param save_data: list
       @param file_location: str
       """
        try:
            output_list: list[dict] = []
            for student_data in save_data:
                output_list.append({FIRST_NAME_KEY: student_data.first_name,
                                    LAST_NAME_KEY: student_data.last_name,
                                    COURSE_NAME_KEY: student_data.course_name})
            with open(file_location, "w") as file:
                json.dump(output_list, file, indent=2)
        except FileNotFoundError as e:
            FileProcessor.output_error_messages(
                "File must exist prior to running this script.", e)
        except Exception as e:
            FileProcessor.output_error_messages(
                "There was an error. Please try again.", e)

class IO:
    all_students_list: list = [Student]
    student_row: Student = None
    """
        A collection of functions that manage user input and output ."""

    @staticmethod
    def input_student_data() -> Student:
        """Accepts information entered by user as string and formats as a dictionary
        Appends it to a student_file.
        """
        first_name: str = ''
        last_name: str = ''
        course_name: str = ''
        while True:
            try:
                first_name = input("What is your first name? ").strip().title()
                if not first_name.isalpha():
                    raise Exception("Sorry, that was not a good first name")
                last_name = input("What is your last name? ").strip().title()
                if not last_name.isalpha():
                    raise Exception("Sorry, that was not a good last name")
                course_name = input(
                    "Please enter the name of the course: ").strip().title()  # pass
                if not course_name.isprintable():
                    raise Exception("Sorry, that was not a good course name")
            except Exception as e:
                FileProcessor.output_error_messages("Please try again", e)
            return Student(first_name, last_name, course_name)

    @staticmethod
    def output_student_courses(students_list: list):
        """
        Prints the list all_students_list.
        all_students_list: list of dictionaries
        """
        for student in students_list:
            print(f'{student.first_name} {student.last_name} is '
                  f'signed up for {student.course_name}')

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
       Prints a welcome statement and asks if the user would like to register for a course.

        """
        welcome_str = input(
            "Welcome! Would you like to interact with registration? (Y/N)  ")
        if welcome_str.upper() == 'Y':
            return
        print(exit_statement)
        exit()

# This is where it all happens.

FILE_NAME: str = "Enrollments.json"
all_students_list: list[Student] = FileProcessor.load_student_data(FILE_NAME)
IO.welcome_str_menu()  # Provides a greeting and menu for input
while True:
    menu_choice = IO.input_menu_choice()
    if menu_choice == str(1):
        next_student_data = IO.input_student_data()
        all_students_list.append(next_student_data)
        print(all_students_list)
    elif menu_choice == str(2):
        IO.output_student_courses(all_students_list)
    elif menu_choice == str(3):
        FileProcessor.write_data_to_file(all_students_list, FILE_NAME)
        IO.output_student_courses(all_students_list)
    else:
        print(exit_statement)
        quit()
