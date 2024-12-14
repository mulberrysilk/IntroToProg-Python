##Introduction

The Employee Ratings Program was developed in the Fall of 2024 using Python 3.13. The following provides documentation for this program. 
Problem to Be Addressed
The customer desires to collect employee ratings information from employees, including date of rating and the rating result. The program records this information against the employees’ first and last names. The customer plans to store this information in a file to create a record. 

##Design
The program was developed according to the specifications provided in the Introduction to Python class in fall of 2024. It is a simple program intended to help students develop knowledge and skills and achieve the educational goals of learning to program in the Python language. The program is structured as a Python module containing the following files, which together follow a standard structure to encapsulate the script:

##Primary Program
•	main.py 
o	Entry point for the application which controls flow of execution.

•	data_classes.py 
o	Has a class hierarchy incorporating inheritance. The base class is Person with attributes of first name and last name. The Employee class inherits Person class.

•	processing_classes.py 
o	File input and output is handled in this module reading employee data to and from a JSON file.

•	presentation_classes.py
o	Here user interactions occur including inputs and outputs.  A Menu is generated, and errors are handled. 

##Testing modules
•	test_data_classes.py
•	test_processing_classes.py
•	test_presentation_classes.py
Together these modules run the program which follows a structured approach that eliminates redundancy, and also provides a clear pattern of separations of concern. 
Three files are used to test the program. The test files are for development purposes only during the data validation effort (see below). 

##Classes Diagram
A class diagram illustrates the classes used in this program (Figure 1). 

![image](https://github.com/user-attachments/assets/673921a4-46d3-413b-a852-8c445221255f)

##Program Operation
This program initializes by loading data stored in the JSON file to memory formatted as a list of Employee object rows and manages the list when in the program. 
The program requests and accepts information from an employee and saves that data.  When the program starts, a user can choose to add information, look at existing data, save data to a file, or end the program. 
Data collected from the user includes first name, last name, review date, and review rating.
•	Review ratings are categorized as 1, 2, 3, 4, or 5. 
•	Review dates are entered following the “YYYY-MM-DD” format. 
•	First name and last name are limited to only allowing alphabetical information.
The information is stored in a convenient JSON file format. The file is named “EmployeeRatings.json”.  
The user may view the saved data. However, at the current time, the user cannot implement a change to the saved data. 

##Testing and Quality Assurance
This program has been tested and proven to run within the specifications, to the customer’s expectations and with common conventions for this type of program. Error handling is provided, including messages returned to the user when incorrect information is provided. 
Unit testing was developed and implemented to confirm that correct data was accepted and incorrect information not recorded. Unit testing evaluates individual units of code to examine performance. The 
testing works under the Python unittest framework which provides automation and incorporates use of the “assert” statement in test cases. 
Acceptance criteria included:
•	The program will successfully read and write employee data to a JSON file without data loss or file corruption.
•	The program will include information on employee ratings and the date of the rating in a standard format. 
•	User input will be validated.

##Conclusion
The Employee Ratings Program was developed in the Fall of 2024 using Python 3.13 and was submitted as the solution to Assignment 8. To complete the assignment several important computer programming concepts were implemented. This program has been tested and proven to run within the specifications, to the costumer’s expectations and common conventions for this type of program. The program, while simple, it performs to established acceptance criteria. 

