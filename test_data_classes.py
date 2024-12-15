#-------------------------------------------------------------------------- #
# Title:  Assignment 08 - Test Data Classes
# Description: This file tests data classes
#
# Change Log:
# 12/07/2024: Establish file, per example in lab and lecture example.
# 12/12/2024: Setup for final review and submission.
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #
import unittest
from data_classes import Person


class   TestPersonClass(unittest.TestCase):

    def test_person_init(self):
        #test that the function correctly collects the first names and last names.
        person = Person ("Vic", "Vu")
        self.assertEqual("Vic", person.first_name)
        self.assertEqual( "Vu",  person.last_name)

    def test_person_invalid_name(self):
        # make sure value error are raised when needed.
        with self.assertRaises(ValueError):
           Person('123', 'Vu')
        with self.assertRaises(ValueError):
           Person( '123',  'Vu')

if __name__ == "__main__":
        unittest.main()
