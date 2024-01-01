# Python MySQL Project : School Library Management

1. Python
2. MySQL Connector Python
3. Tables Created

## Python

- All Operations through MySQL Commands
- Handles DataBases, Tables and the Data Stored in Tables

## MySQL Connector Python

- Connects Python with MySQL DataBase through a Connection Object
- Cursor is associated to Connection Object
- This Cursor helps execute MySQL Commands in Python
- Cursor stores the corresponding Output Data which can be obtained from it
- Cursor can also Create Tables and DataBases

 To install this connector, use the following command in your terminal :
`pip install mysql-connector-python`

## Tables Formed

1. school_students
2. library_books
3. issued_books

## Python Modules Imported

### 1. time
Provides with time functions :
#### 1.1 time.sleep(<No. of seconds to delay>)
- This function delays the execution of the next statement for the argument time (in seconds)
  
### 2. os
- Provides with very useful system functions :
#### 2.1 os.system("cls")
This function clears everything from the screen when executed. This helps to give a very cool effect during changing menus.
Note that the effect of this function only takes place in terminals. That's why, we advise the users to run this program in the Python Shell or Terminal, but not in Idle.

### 3. mysql.connector
- Provides many useful functions for the handling of DataBases and their Data through Cursor Object
- Helps Connect Python and MySQL via Connection Object
#### 3.1 mysql.connector.connect(host=<hostname>, user=<username>, passwd=<password>)
- This function helps connect the MySQL and Python through Connection Object.
- _Note that <hostname> used in the Program is "127.0.0.1" which is the localhost._
- <username> and <password> are interactively received from the user via input function.
- This Connection Object is stored in a variable called "cnx" which acts a link between Python and MySQL.
#### 3.2 cnx.cursor("<MySQL Command>")
- Helps execute various MySQL Commands.
- Stores the Output in itself.
- The Output can be used in every way we want to.
  
