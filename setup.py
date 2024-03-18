import psycopg2


def connect_database():

    print("Establishing database connection...")

    try:
        # change credentials as needed
        postgres_connection = psycopg2.connect(database="postgres", user="postgres",
                                               password="postgres", host="localhost",
                                               port="5432")
        postgres_connection.autocommit = True

        return postgres_connection

    except Exception as e:
        print("An error occurred whilst attempting to create the database."
              f"\n Exception: {e}")
        return None


def execute_sql_setup(filename: str, connection):
    try:
        cur = connection.cursor()

        with open(filename, 'r') as sql_file:
            sql_query = sql_file.read()
            cur.execute(sql_query)

        cur.close()

        print(f"SQL statements finished executing.")

    except Exception as e:
        print("An error occurred during loading the database (likely due to incorrect filename)."
              f"\n Exception: {e}")


def setup_all():
    print('Now attempting to connect to Postgres database postgres, on localhost, port 5432, with default credentials.')
    print('Please modify setup.py with custom credentials if required.')
    conn = connect_database()

    execute_sql_setup("setup.sql", conn)

    conn.close()
