"""
installation: https://dev.mysql.com/downloads/mysql/
install Community Server + Workbench
make sure the service is set to startup with system
python -m pip install mysql-connector-python

https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

# python password_manager/pass.py PASSWORD


def main():
    # Standard library imports:
    import sys

    # Third party imports:
    import mysql.connector
    from mysql.connector import errors

    # password chcecking:
    MY_SQL_PASSWORD = password_check()

    print()

    # connecting to the database:
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=MY_SQL_PASSWORD,
            database="db_pass_python",  # TODO: check if there is db_pass_python database. If not: create_database(mycursor, db_pass_python)
        )
        mycursor = mydb.cursor()

    except errors.ProgrammingError as e:
        sys.exit(f"cannot connect to MySQL database: \n{e}")

    # show databases:
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

    # TODO: view, add, modify, delete entry (CRUD operations)
    # TODO: view as a formatted text table
    # TODO: search
    # TODO: encryption
    # TODO: login, password, change password
    # TODO: interface


    # Close the cursor and the connection
    mycursor.close()
    mydb.close()


# chcecking if program was launched with password as parameter:
def password_check():
    import sys
    if len(sys.argv) != 2:
        sys.exit("\nYou must run program with mySQL password as a parameter")
    else:
        return sys.argv[1]

# create database:
def create_database(mycursor, name="db_pass_python"):
    mycursor.execute("CREATE DATABASE {name}")


if __name__ == "__main__":
    main()
