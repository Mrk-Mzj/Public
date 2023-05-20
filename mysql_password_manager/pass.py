"""
mySQL Password Manager
"""


# Standard library imports:
import sys

# Third party imports:
import mysql.connector
from mysql.connector import errors

DATABASE = "db_pass_python"


def main():
    # password chcecking:
    MY_SQL_USER, MY_SQL_PASSWORD = login_db()

    # connecting to the database (or creating a new one):
    mydb, mycursor = connect_create_db(MY_SQL_USER, MY_SQL_PASSWORD)


    # show all databases:
    show_all_db(mycursor)

    # delete database:
    print("\nDeleting database")
    mycursor.execute("DROP DATABASE " + DATABASE)


    # close the cursor and the connection:
    mycursor.close()
    mydb.close()

    # TODO: view, add, modify, delete entry (CRUD operations)
    # TODO: view as a formatted text table
    # TODO: search
    # TODO: encryption
    # TODO: interface


def connect_create_db(MY_SQL_USER, MY_SQL_PASSWORD):
    # connect to the database or create a new one if one doesn't exist
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=MY_SQL_USER,
            password=MY_SQL_PASSWORD,
            database=DATABASE
        )
        mycursor = mydb.cursor()
        return mydb, mycursor

    except errors.ProgrammingError as error:
        

        if error.errno == 1049:
            # database does not exist:
            print("database does not exist, creating a new one")

            # create a new database:
            mydb = mysql.connector.connect(
                host="localhost",
                user=MY_SQL_USER,
                password=MY_SQL_PASSWORD
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE " + DATABASE)
            return mydb, mycursor

        elif error.errno == 1045:
            # wrong username or password:
            sys.exit("wrong username or password")
        
        else:
            sys.exit(f"other database error: {error}")



def login_db():
    # chceck if program was launched with password as parameter

    print()
    if len(sys.argv) != 3:
        sys.exit(
            "You must add mySQL username and password as parameters: 'python pass.py username password'"
        )
    else:
        return sys.argv[1], sys.argv[2]


def show_all_db(mycursor):
    # show all databases
    print()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


if __name__ == "__main__":
    main()
