#-------------------------------------------------------------------------- #
# Title:  Assignment 08 - Test Processing Classes
# Description: This file tests processing classes
#
# Change Log:
# 12/07/2024: Establish file, per example in lab and lecture example.
#12/12/2024: Final testing
#
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #

import unittest
import json
from tempfile import NamedTemporaryFile

import data_classes as data
from processing_classes import FileProcessor, FIRST_NAME_KEY
import tempfile



class TestFileProcessor(unittest.TestCase):
    SAMPLE_DATA = [{
    "First Name": "K",
    "Last Name": "K",
    "Review Date": "2024-22-12",
    "Review Rating": 5
        }]

    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    FIRST_NAME_KEY: str = "First Name"
    LAST_NAME_KEY: str = "Last Name"
    REVIEW_DATE_KEY: str = "Review Date"
    REVIEW_RATING_KEY: str = "Review Rating"
    def test_read_data_from_file(self): # read data from the temporary file
        with open(self.temp_file_name, "w") as file:
            json.dump(self.SAMPLE_DATA, file)

        # Call the read_data_from_file and check if it returns the expected data:
        test_data=FileProcessor.read_data_from_file(self.temp_file_name)
        self.assertEqual(self.SAMPLE_DATA,  test_data)

    def test_write_data_to_file(self):# Create some sample employee objects
        sample_employee_list = [
            data.Employee("Vic", "Vu", "1900-10-10", 4),
            data.Employee("Alice", "Smith", "1900-10-10", 4),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_data_to_file(sample_employee_list,self.temp_file_name)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)
        self.assertEqual(len(file_data), len(sample_employee_list))
        self.assertEqual(file_data[0][FIRST_NAME_KEY], "Vic")


if __name__ == "__main__":
    unittest.main()
