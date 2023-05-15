"""
installation: https://dev.mysql.com/downloads/mysql/
install Community Server + Workbench
make sure the service is set to startup with system
python -m pip install mysql-connector-python

https://www.w3schools.com/python/python_mysql_getstarted.asp
"""
# login, pass: check .gitignore


# Standard library imports:
import sys

# Third party imports:
import mysql.connector
from mysql.connector import errors


def main():

    # password chcecking:
    MY_SQL_USER, MY_SQL_PASSWORD = login_db()

    # connecting to the database:
    mydb = connect_db(MY_SQL_USER, MY_SQL_PASSWORD)
    mycursor = mydb.cursor()

    # show all databases:
    show_all_db(mycursor)

    # close the cursor and the connection
    mycursor.close()
    mydb.close()


    # TODO: view, add, modify, delete entry (CRUD operations)
    # TODO: view as a formatted text table
    # TODO: search
    # TODO: encryption
    # TODO: interface


# chcecking if program was launched with password as parameter:
def login_db():

    print()
    if len(sys.argv) != 3:
        sys.exit(
            "You must add mySQL username and password as parameters: 'python pass.py username password'"
        )
    else:
        return sys.argv[1], sys.argv[2]


# connecting to the database:
def connect_db(MY_SQL_USER, MY_SQL_PASSWORD):
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = MY_SQL_USER,
            password = MY_SQL_PASSWORD,
            database = "db_pass_python",  # TODO: check if there is db_pass_python database. If not: create_database(mycursor, db_pass_python)
        )
        return mydb

    except errors.ProgrammingError as e:
        sys.exit(f"cannot connect to MySQL database: \n{e}")


# create database:
def create_database(mycursor, name="db_pass_python"):
    mycursor.execute("CREATE DATABASE {name}")


# show all databases:
def show_all_db(mycursor):
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

        
if __name__ == "__main__":
    main()
