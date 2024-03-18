from setup import connect_database


def getAllStudents():
    conn = connect_database()

    cur = conn.cursor()

    try:
        statement = "SELECT * FROM students"

        cur.execute(statement)

        result = cur.fetchall()

        return result

    except Exception as e:
        print(f'{e}')

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    # returning none instead of nothing as prompt loop expects something returned
    # due to (for student in students)
    return None


def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_database()

    cur = conn.cursor()

    try:
        statement = "INSERT into students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"

        cur.execute(statement, (first_name, last_name, email, enrollment_date))

        conn.commit()

    except Exception as e:
        print(f'Exception: {e}')

    # always include to prevent leaving open cursors and connections
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return


def updateStudentEmail(student_id, new_email):
    conn = connect_database()

    cur = conn.cursor()

    try:
        statement = "UPDATE students SET email = %s WHERE student_id = %s"

        cur.execute(statement, (new_email, student_id))

        conn.commit()

    except Exception as e:
        print("Student email was not updated successfully.")
        print(f'Exception: {e}')

    finally:
        # always include to prevent leaving open cursors and connections
        if cur:
            cur.close()
        if conn:
            conn.close()

    return


def deleteStudent(student_id):
    conn = connect_database()
    cur = conn.cursor()

    try:
        statement = "DELETE FROM students WHERE student_id = %s"

        cur.execute(statement, (student_id,))

        conn.commit()

    except Exception as e:
        print(f'{e}')

    finally:
        # always include to prevent leaving open cursors and connections
        if cur:
            cur.close()
        if conn:
            conn.close()

    conn.close()

    return
