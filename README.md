# PostgreSQL CRUD Assignment
![](https://img.shields.io/badge/Assignment_Status-Completed-blue)

>  A simple tool for creating a predifined SQL table and performing simple CRUD operations. This project is coursework for a database management course at CU.

[JUMP TO DOCUMENTATION (instructions)](#documentation)
<br>
[JUMP TO DEMONSTRATION VIDEO](#video)

# Purpose

This app is part of my coursework for a DBMS course.

# Environment & Requirements

This project was written using Python 3.11.

It requires the ```psycopg2``` library for map features, which can be installed with 
```
pip install psycopg2
```

# Development Checklists
### Core Features Supported
- [x] Automatically creates and populates table upon start
- [x] Provides users with menu
- [x] Adds students via addStudent()
- [x] Retrieves all students via getAllStudents()
- [x] updates student emails via updateStudentEmail()
- [x] provides delete functionality via deleteStudent()

# Documentation
<a id="documentation"></a>

## setup.py
When main.py is executed, it first executes the setup_all() function from setup.py.
This function established a connection to the database, and creates a student table and populates it based on the provided ```setup.sql``` file.
NOTE: if a 'students' table already exists, this will throw an exception and the student in ```setup.sql``` will not be added to the students table.

## main.py

This contains some simple functions to display the menu and take the user input until the user decides to exit.
Menu options are made by entering a single digit.
Based on this digit input, main will hand off the task to the appropriate function in query.py.

## query.py

query.py contains the backend code for ```addStudent, getAllStudents, updateStudentEmail, and deleteStudent()```.
It reuses the connection function from query.py.

For each function, it connects to the database and creates a cursor separately, to prevent the cursor from being open across functions.
Then it executes a single query and commits the changes.
