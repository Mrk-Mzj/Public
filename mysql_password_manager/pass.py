"""
mySQL Password Manager
"""


# Standard library imports:
import sys, re

# Third party imports:
import mysql.connector
from mysql.connector import errors
from tabulate import tabulate


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
        user_input = input().strip().split(" ")

        # Executing user command.
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
                        show_chosen_record(id, mycursor)
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
                            print("> You need to add valid 'id' to remove")
                    else:
                        print("> You need to add parameters:\nR number")

                # Add new record:
                case "A":
                    if len(user_input) == 4:
                        title = user_input[1]
                        login = user_input[2]
                        password = user_input[3]

                        # Checking password strength:
                        password_strength_result = password_strenght_check(password)
                        if password_strength_result[0] == "the password is strong":
                            # Adding to the database:
                            mycursor.execute(
                                "INSERT INTO passwords (title, login, password) VALUES (%s, %s, %s)",
                                (title, login, password),
                            )
                            mydb.commit()
                            print("> Added: ", title, login, password)
                        else:
                            # Print how password should be improved:
                            print("\nRecord not added:")
                            for _ in password_strength_result:
                                print(_)
                    else:
                        # the number of parameters wasn't right:
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
                            # Checking password strength:
                            password_strength_result = password_strenght_check(password)
                            if password_strength_result[0] == "the password is strong":
                                # Updating the database:
                                mycursor.execute(
                                    "UPDATE passwords SET title=%s, login=%s, password=%s WHERE ID=%s",
                                    (title, login, password, id),
                                )
                                mydb.commit()
                                print("> Modified: ", title, login, password)
                            else:
                                # Print how password should be improved:
                                print("\nRecord not modified:")
                                for _ in password_strength_result:
                                    print(_)
                        else:
                            # id doesn't exist:
                            print("> You need to add valid 'id' to modify")
                    else:
                        # the number of parameters wasn't right:
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


def password_strenght_check(password):
    """
    Verify the strength of 'password'
    Returns a list of communicates what needs to be changed, or "strong"
    A password is considered strong when it has:
    - 12 or more: characters
    - 1 or more: digit, symbol, lowercase letter, uppercase letter
    """

    password_check_result = []

    # calculating the length
    if len(password) < 12:
        password_check_result.append("> Use 12 characters or more")

    # searching for digits
    if re.search(r"\d", password) is None:
        password_check_result.append("> Use at least 1 digit")

    # searching for symbols
    if re.search(r"\W", password) is None:
        password_check_result.append("> Use at least 1 special character")

    # searching for lowercase
    if re.search(r"[a-z]", password) is None:
        password_check_result.append("> Use at least 1 lowercase letter")

    # searching for uppercase
    if re.search(r"[A-Z]", password) is None:
        password_check_result.append("> Use at least 1 uppercase letter")

    # if there were no errors added to the list
    if password_check_result == []:
        password_check_result.append("the password is strong")

    return password_check_result


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
    print("\nRecords in the database:")
    headers = ["id", "title"]
    print(tabulate(myresult, headers=headers, tablefmt="grid"))


def show_chosen_record(id, mycursor):
    # showing details of a chosen record

    print()

    # checking if user provided valid id number:
    if id_exist(id, mycursor):
        # gathering info to print:
        mycursor.execute(
            "SELECT * FROM passwords WHERE ID=%s", (id,)
        )  # comma is essential, as "execute" expects tuple
        myresult = mycursor.fetchall()
        headers = ["id", "title", "login", "password"]

        # printing in a table:
        print("\nDetails:")
        print(tabulate(myresult, headers=headers, tablefmt="grid"))

    else:
        # id doesn't exist:
        print("> You need to add valid 'id' to display")


if __name__ == "__main__":
    main()
