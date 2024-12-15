#-------------------------------------------------------------------------- #
# Title:  Assignment 08 - Test presentation Classes
# Description: This file tests presentation classes
#
# Change Log:
# 12/07/2024: Establish file, per example in lab and lecture example.
#12/12/2024: Wrap up
#
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #
import unittest
import unittest.mock
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.mock_employee = Employee("Vic", "Vu", "1600-10-10", 4) #employee object for test class

    def test_input_menu_choice(self):
        with patch("builtins.input", return_value = "2"):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, "2")

    def test_input_employee_data(self):
        with patch("builtins.input", side_effect=['Vic',' Vu', '1600-10-10', '4']):
            employee = IO.input_employee_data()
            self.assertEqual(employee.first_name, "Vic")
            self.assertEqual(employee.last_name, "Vu")
            self.assertEqual(employee.review_date, "1600-10-10")
            self.assertEqual(employee.review_rating, 4)


if __name__ == "__main__":
        unittest.main()
