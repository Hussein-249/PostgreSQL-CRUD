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

# Execution Instructions
## Windows
- Clone this repository
- Before continuing, modify the setup.py file, lines 10-12, as needed. This app assumes that a default postgres user has been set up, and it attempts to create a table in the postgres database. If you want to change this, then modify these lines:
```python
postgres_connection = psycopg2.connect(database="postgres", user="postgres",
                                               password="postgres", host="localhost",
                                               port="5432")
```
- Create a virtual environment using ```python -m venv venv```. This creates a venv folder that will contain the necessary libraries
- Activate the virtual environment with ```venv\Scripts\activate```. The shell should now indicate you are in the virtual environment.
- Install the requirements with ```pip install -r requirements.txt```
- Start the application with ```python main.py```
- Once you are finished with the application, you can deactivate the virtual environment using ```deactivate```.

# Documentation
## setup.py
<a id="documentation"></a>
When main.py is executed, it first executes the setup_all() function from setup.py.
This function established a connection to the database, and creates a student table and populates it based on the provided ```setup.sql``` file.
NOTE: if a 'students' table already exists, this will throw an exception and the student in ```setup.sql``` will not be added to the students table.

## main.py

This contains some simple functions to display the menu and take the user input until the user decides to exit.
Menu options are made by entering a single digit.
Based on this digit input, main will hand off the task to the appropriate function in query.py.

## query.py

query.py contains the backend code for ```addStudent(), getAllStudents(), updateStudentEmail(), and deleteStudent()```.
It reuses the connection function from query.py.

For each function, it connects to the database and creates a cursor separately, to prevent the cursor from being open across functions.
Then it executes a single query and commits the changes.
