# --------------------------------------------------------------------------- #
# Title:  Assignment 08 - Data Classes
# Description: This file collects data in two classes Person and Employee
##
# Change Log:
# 12/01/2024: Establish file by breakout from main.py
# 12/08/2024: Update calls
# 12/12/2024: Ready for submission
#
#
# Kristie Dunkin                12/15/2024                Assignment 08
# ------------------------------------------------------------------------------- #
from datetime import date

class Person:
    _first_name: str
    _last_name: str
    """   Base Class  - Establishes a class of person objects with attributes of first and last name.

     Properties:
     -first_name(str): the person's first name.
     -last_name(str): the person's last name.

    """

    def __init__(self, first_name: str, last_name: str):  #Add validation
        self.first_name = first_name
        self.last_name = last_name

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

class Employee(Person):
    """A  class representing employee's rating information.
    Inherits from the Person class.
    Properties:
    first_name(str): The person's first name - inherited.
    last_name(str): The person's last name - inherited.
    review_date(str): Date of review in YYYY-MM-DD format.
    review_rating(int):  Employee's rating, 1 through 5.
    .
    """
    review_rating: str = "3"
    review_date: str =[f"1900-01-01"]

    def __init__(self, first_name: str, last_name: str, review_date: str = '1900-01-01"', review_rating: int = 3):
        super().__init__(first_name=first_name, last_name=last_name)
        self._review_date = review_date
        self._review_rating = review_rating

    @property
    def review_date(self):
        return self._review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self._review_date = value
        except ValueError:
            raise ValueError ("That is not a correct date format. Date format is YYYY-MM-DD. ")

    @property
    def review_rating(self):
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value:str):  # add try catch to all setters. make sure data is correct everytime.
        if value in (1, 2, 3, 4, 5):
            self._review_rating = value
        else:
            raise ValueError("Please enter a number: 1 through 5. ")

    def __str__(self):
        result = super().__str__()
        return f'{result}, {self.review_date}, {self.review_rating}'

    def __repr__(self):
        result = super().__str__()
        return f'{result}, {self.review_date}, {self.review_rating}'

if __name__ == '__main__':
    print("This file is not meant to be run. Please run main.py")
