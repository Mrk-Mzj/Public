# 🐍 MySQL Password Manager

Store logins and passwords locally using mySQL AES encrypted database.

🪧Note: This is just a test project. The goal was to learn how to integrate and use mySQL with Python. Do not use it to store your real passwords.


# 1. Installation

### 1.1 Installing mySQL:
For fast, reliable, encrypted database support.

1. Download MySQL Community installer
https://dev.mysql.com/downloads/mysql/


2. Install Community Server + Workbench
🪧Make sure the service is set to startup with the system.


### 1.2 Installing mySQL Connector:
For Python and mySQL integration.
```
python -m pip install mysql-connector-python
```

### 1.3 Installing tabulate:
For convenient display of tables.
```
pip install tabulate
```


# 2. Usage


Run app with 2 parameters: mySQL user name, mySQL password.

##### example:
```
python ../Public/password_manager/pass.py login password
```

When started program connects to *db_pass_python* on your device. In case there is none, it creates a new one. 

At start program shows IDs and titles of your entries, but no logins or passwords:

```
Records in the database:
+------+-----------+
|   id | title     |
+======+===========+
|    1 | Twitter   |
+------+-----------+
|    2 | TikTok    |
+------+-----------+
|    3 | Facebook  |
+------+-----------+
```
</br>Now you can decide what to do:
```
What to do?
  S N              - show record nr NN
  R N              - remove record nr NN
  A TTT LLL PPP    - add new record: title TTT login LLL and pass PPP
  M N TTT LLL PPP  - modify record nr NN: title TTT login LLL pass PPP
  ERASE            - delete the whole database and quit
  E                - exit
  ```
</br>Let's view login and password for Twitter:

```
s 1
```
```
+------+---------+------------+----------------+
|   id | title   | login      | password       |
+======+=========+============+================+
|    1 | Twitter | Log@in.in  | Pas@word123456 |
+------+---------+------------+----------------+
```
🪧Note: Logins and passwords are **AES encrypted**. But keep in mind, this is just a test program, possibly with lots of vulnerabilities. <ins>Do not use it to store your real passwords.</ins> 
</br>
We can modify entry, like so:

```
m 1 Twitter Log@in.in NewPassword
```
🪧Note: **Program checks passwords complexity**. 
Should you provide too simple one, you'll be prompted to correct it:
```
Record not modified:
> Use 12 characters or more
> Use at least 1 digit
> Use at least 1 special character
```
</br>

After providing strong password you'll see the confirmation:
```
> Modified: Twitter, Log@in.in, New$trongPass@word123456
```
</br>

To exit program, write 'e'. 
To exit and completly delete database created at startup, write ERASE.



# 3. Contributing
This is just a test project. There is no need to develop it any further.

# 4. License
[CC0](https://creativecommons.org/publicdomain/zero/1.0/)
