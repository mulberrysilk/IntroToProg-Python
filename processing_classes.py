# --------------------------------------------------------------------------- #
# Title:  Assignment 08 - Processing Classes
# Description: This file processes data to and from a JSON file.
##
# Change Log:
# 12/01/2024: Establish file by breakout from main.py
#
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #

import json
from data_classes import Employee


FILE_NAME: str = "EmployeeRatings.json"
FIRST_NAME_KEY: str = "First Name"
LAST_NAME_KEY: str = "Last Name"
REVIEW_DATE_KEY:str = "Review Date"
REVIEW_RATING_KEY: str = "Review Rating"

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
        @Param all_employees_list: a list of dictionary rows to be fill with file data.
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
    def load_employee_data(employee_data_file: str) -> list[Employee]:
        raw_file_data = FileProcessor.read_data_from_file(employee_data_file)
        employee_list: list[Employee] = list()
        for row in raw_file_data:
            employee_list.append(Employee(row[FIRST_NAME_KEY], row[LAST_NAME_KEY],
                                            row[REVIEW_DATE_KEY], row[REVIEW_RATING_KEY]))
        return employee_list

    @staticmethod
    def write_data_to_file(save_data: list[Employee], file_location: str):
        """Saves data to a .json file. using open in write mode "w" .
       Note this is using a with, which will close the file for us.
       Saved data is formated using 'indent = 2' to look like a table.
       @param save_data: list
       @param file_location: str
       """
        try:
            output_list: list[dict] = []
            for employee_data in save_data:
                output_list.append({FIRST_NAME_KEY: employee_data.first_name,
                                    LAST_NAME_KEY: employee_data.last_name,
                                   REVIEW_DATE_KEY: employee_data.review_date,
                                   REVIEW_RATING_KEY: employee_data.review_rating})
            with open(file_location, "w") as file:
                json.dump(output_list, file, indent=2)
        except FileNotFoundError as e:
            FileProcessor.output_error_messages(
                "File must exist prior to running this script.", e)
        except Exception as e:
            FileProcessor.output_error_messages(
                "There was an error. Please try again.", e)

if __name__ == '__main__':
    print("This file is not meant to be run. Please run main.py")
