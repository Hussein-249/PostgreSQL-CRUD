"""
This is the application entry point.
It sets up the database via setup_all() and then provides users with a menu.
Users can query until they decide to exit.
"""


from query import getAllStudents, addStudent, deleteStudent, updateStudentEmail
from setup import setup_all


def main():
    """Define menu options and begin prompt loop."""
    options = {'1': getAllStudents, '2': addStudent, '3': deleteStudent, '4': updateStudentEmail}
    prompt_loop(options)
    exit_msg()
    return


def prompt_loop(options: dict):
    prompt = "Your selection: "

    while 1:
        print_menu()
        userinput = input(prompt)
        if userinput == '0':
            break

        # user has selected an option
        else:
            if userinput == '1':
                students = options[userinput]()
                for student in students:
                    print(student)
                print()

            if userinput == '2':
                print(f'You have selected to add a student.')
                student_fname = input('Enter the new student first name: ')
                student_lname = input('Enter the new student\'s last name: ')
                student_email = input('Enter the new student email: ')
                student_date = input('Enter the new student enrolment date, in YYYY-MM-DD format exactly: ')
                options[userinput](student_fname, student_lname, student_email, student_date)

            if userinput == '3':
                print(f'You have selected to delete a student.')
                student_id = input('Please specify the ID of the student you want to delete: ')
                student_id = int(student_id)
                options[userinput](student_id)

            if userinput == '4':
                print(f'You have selected to update a student\'s email.')
                student_id = input('Please specify the ID of the student whose email you are updating: ')
                student_email = input('Please specify the new email address: ')
                options[userinput](student_id, student_email)


def print_menu():
    """ Display for each iteration of the prompt loop."""
    print(f'-----------------------------------------------')
    print(f'Please select one of the following options:\n')
    print(f'(1) View all students currently in the database')
    print(f'(2) Add a new student')
    print(f'(3) Delete a student from the database')
    print(f'(4) Modify an existing student email')
    print(f'(0) Exit this program\n')
    return


def exit_msg():
    """ Display when exiting the program."""
    print(f'You have exited the program.')
    print(f'The final state of the database is as follows: ')


if __name__ == '__main__':
    setup_all()
    main()
