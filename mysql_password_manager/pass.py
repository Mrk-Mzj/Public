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

    while True:
        # showing contents of the database:
        show_all_records(mycursor)

        # gathering user input:
        print("\nWhat to do?")
        print("  S N              - show record nr NN")
        print("  R N              - remove record nr NN")
        print("  A TTT LLL PPP    - add new record: title TTT login LLL and pass PPP")
        print("  M N TTT LLL PPP  - modify record nr NN: title TTT login LLL pass PPP")
        print("  ERASE            - delete the whole database and quit")
        print("  E                - exit\n")
        user_input = input()

        # executing command:
        do(user_input, mydb, mycursor)

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
            database=DATABASE,
        )
        mycursor = mydb.cursor()
        return mydb, mycursor

    except errors.ProgrammingError as error:
        if error.errno == 1049:
            # database does not exist:
            print("> Database does not exist, creating a new one")

            # create new database and table:
            mydb = mysql.connector.connect(
                host="localhost", user=MY_SQL_USER, password=MY_SQL_PASSWORD
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE " + DATABASE)
            mycursor.execute("USE " + DATABASE)
            mycursor.execute(
                "CREATE TABLE passwords (ID int NOT NULL AUTO_INCREMENT, title TEXT, login TEXT, password TEXT, PRIMARY KEY (ID))"
            )
            return mydb, mycursor

        elif error.errno == 1045:
            # wrong username or password:
            sys.exit("> Wrong username or password")

        else:
            sys.exit(f"> Other database error: {error}")


def do(user_input, mydb, mycursor):
    user_input = user_input.strip().split(" ")

    # input checking:
    if 1 > len(user_input) or len(user_input) > 5:
        print("> Wrong command")

    # if everything's fine:
    else:
        match user_input[0].upper():
            # Show decoded record values:
            case "S":
                if len(user_input) == 2:
                    id = user_input[1]
                    print()
                    mycursor.execute(
                        "SELECT * FROM passwords WHERE ID=%s", (id,)
                    )  # comma is essential, as "execute" expects tuple
                    myresult = mycursor.fetchall()

                    # checking if user provided valid id number:
                    if id_exist(id, mycursor):
                        print(myresult)
                    else:
                        # id doesn't exist:
                        print("> You need to add valid number of row to display")
                else:
                    print("> You need to add parameters:\nS number")

            # Remove record:
            case "R":
                if len(user_input) == 2:
                    id = user_input[1]

                    # checking if user provided valid id number:
                    if id_exist(id, mycursor):
                        mycursor.execute(
                            "DELETE FROM passwords WHERE ID=%s", (id,)
                        )  # comma is essential, as "execute" expects tuple
                        mydb.commit()
                        print("> Removing...", user_input[1])
                    else:
                        # id doesn't exist:
                        print("> You need to add valid number of row to remove")
                else:
                    print("> You need to add parameters:\nR number")

            # Add new record:
            case "A":
                if len(user_input) == 4:
                    title = user_input[1]
                    login = user_input[2]
                    password = user_input[3]

                    mycursor.execute(
                        "INSERT INTO passwords (title, login, password) VALUES (%s, %s, %s)",
                        (title, login, password),
                    )
                    mydb.commit()
                    print("> Added: ", title, login, password)
                else:
                    print("> You need to add parameters:\nA title login password")

            # Modify record values:
            case "M":
                if len(user_input) == 5:
                    id = user_input[1]
                    title = user_input[2]
                    login = user_input[3]
                    password = user_input[4]

                    # checking if user provided valid id number:
                    if id_exist(id, mycursor):
                        mycursor.execute(
                            "UPDATE passwords SET title=%s, login=%s, password=%s WHERE ID=%s",
                            (title, login, password, id),
                        )
                        mydb.commit()
                        print("> Modified: ", title, login, password)
                    else:
                        # id doesn't exist:
                        print("> You need to add valid number of row to modify")
                else:
                    print("> You need to add parameters:\nM title login password")

            # Erase database:
            case "ERASE":
                confirmation = input(
                    "> Are you sure?\n Y - yes, erase database\n N - no, keep database"
                )
                if confirmation.strip().upper() == "Y":
                    mycursor.execute("DROP DATABASE " + DATABASE)
                    print("> Database erased")
                    show_all_db(mycursor)
                    exit(mydb, mycursor)
                else:
                    print("> Database stays intact")

            # Exit:
            case "E":
                print("> Exiting...")
                exit(mydb, mycursor)

            case _:
                print("> Wrong command")


def exit(mydb, mycursor):
    # close cursor, connection and exit:

    mycursor.close()
    mydb.close()
    sys.exit()


def id_exist(id, mycursor):
    # returns True if id exists in database:
    
    mycursor.execute(
        "SELECT * FROM passwords WHERE ID=%s", (id,)
    )  # comma is essential, as "execute" expects tuple
    myresult = mycursor.fetchall()

    if myresult == []:
        return False
    else:
        return True


def login_db():
    # chceck if program was launched with password as parameter

    print()
    if len(sys.argv) != 3:
        sys.exit(
            "> You must add mySQL username and password as parameters: 'python pass.py username password'"
        )
    else:
        return sys.argv[1], sys.argv[2]


def show_all_db(mycursor):
    # show all databases

    print()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


def show_all_records(mycursor):
    # showing all records, without logins or passwords

    mycursor.execute("SELECT ID, title FROM passwords")
    myresult = mycursor.fetchall()
    print()
    for x in myresult:
        print(x)


if __name__ == "__main__":
    main()
