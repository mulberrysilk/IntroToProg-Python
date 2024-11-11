# --------------------------------------------------------------------------- #
# Title:  Assignment 05
## Description: This Assignment 05 will collect information
# then display a message about a student's registration for
# a Python course. In this assignment we are building a list of dictionaries.
#
# Change Log:
# 10/6/2024: Beginning script outline
# 11/7/2024: Pycharm is somewhat fixed. adding first attempt to make list of list
# 11/8/2024: Implement more tries at List-of-List (LOL). Nearly to complete.
# 11/9/2024: Following office hours I fixed up the script by adding for loops and with
# statements.
#
# Kristie Dunkin       11/11/2024     Assignment 05
# ------------------------------------------------------------------------------- #
#
import json

# Define Constants:
FILE_NAME: str = "C:\\Users\\Kristie\\OneDrive\\Python Fundamentals\\_Module05\\Assignment\\Enrollments.json"
MENU: str = '''
 ----Course Registration Program Menu-----
 1. Register a student for a course 
 2. Show current data 
 3. Save data to a file 
 4. Exit this program
 '''
FIRST_NAME_KEY: str = "First Name"
LAST_NAME_KEY: str = "Last Name"
COURSE_NAME_KEY: str = "Course Name"
# Define variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
menu_choice: str = ''
welcome_str: str = ''
student_data: dict[str, str] = {}
students: list[dict[str, str]] = []
exit_statement: str = "'Thank you. Goodbye.'"

def read_file(file_json: str):
    with open(file_json, "r") as file:  # open Enrollments.json on C drive.
        return json.load(file)

def save_file(save_data: list, file_location: str):
    with open(file_location, "w") as file:
        json.dump(save_data, file, indent=2)

try:
    students = read_file(FILE_NAME)
except FileNotFoundError as e:
    print("Sorry, your file was not found.")
    quit()
except json.JSONDecodeError as e:
    print("There was an error decoding your file")
    quit()

# welcome statement and start of while loop with some conditions
welcome_str = input("Welcome! Would you like to register for a course? (Y/N)  ")

if welcome_str.upper() == "N":
    print(exit_statement)
while welcome_str.upper() == 'Y':
    print(MENU)
    menu_choice: str = input("Please make a choice from the menu above (1/2/3/4)  ")
    # Requests user make a choice from the menu offer choices 1 through 4 using if and else.
    if menu_choice == str(1):
        try:
            while True:
                student_first_name = input("What is your first name? ").strip().title()
                if not student_first_name.isalpha():
                    raise Exception("Sorry, that was not a good first name")
                student_last_name = input("What is your last name? ").strip().title()
                if not student_last_name.isalpha():
                    raise Exception("Sorry, that was not a good last name")
                course_name = input(
                    "Please enter the name of the course: ").strip().title()
                if not course_name.isprintable():
                    raise Exception("Sorry, that was not a good course name")
                else:
                    break
        except Exception as e:
            print(e)
            continue

        student_data = {FIRST_NAME_KEY: student_first_name,
                        LAST_NAME_KEY: student_last_name, COURSE_NAME_KEY: course_name}
        students.append(student_data)
        print(students)

        print(f'You have registered {student_first_name} {student_last_name} for'
              f' {course_name}.')

    elif menu_choice == str(2):
        for student_row in students:
            print(f'{student_row[FIRST_NAME_KEY]} {student_row[LAST_NAME_KEY]} is '
                  f'signed up for {student_row[COURSE_NAME_KEY]}')

    elif menu_choice == str(3):
        try:
            save_file(students, FILE_NAME)
            for student in students:
                print(f'{student[FIRST_NAME_KEY]} {student[LAST_NAME_KEY]} is '
                      f'signed up for {student[COURSE_NAME_KEY]}')
        except FileNotFoundError as e:
            print(f'Error saving file: {e}')

    else:
        print(exit_statement)
        quit()
