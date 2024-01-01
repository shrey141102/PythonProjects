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
  
# ScreenShots
### 1. Login With Username And Password
<img width="546" alt="Login With Username And Password" src="https://github.com/shiv325/PythonProjects/assets/139581888/567d420e-f562-46c3-bfc0-4f091df7aef2">

### 2. Creation of Connection Object and Cursor Object
<img width="546" alt="Creation of Connection Object and Cursor Object" src="https://github.com/shiv325/PythonProjects/assets/139581888/4a91f337-f951-4dbf-b70a-744787786f9c">

### 3. DataBase Menu Showing All DataBases and 2 Options
<img width="675" alt="DataBase Menu Showing All DataBases and 2 Options" src="https://github.com/shiv325/PythonProjects/assets/139581888/8c69c869-7590-4d3a-b3b7-7077c29a150c">

### 4. Creation of New DataBase
<img width="675" alt="Creation of New DataBase" src="https://github.com/shiv325/PythonProjects/assets/139581888/b9b439fa-bb3d-4d09-b6b2-9ecb280bf42f">

### 5. Tables Of Selected DataBase and Creation Of Tables and Using The Tables in that DataBase
<img width="675" alt="Tables Of Selected DataBase and Creation Of Tables and Using The Tables in that DataBase" src="https://github.com/shiv325/PythonProjects/assets/139581888/7e2501b4-cd11-4068-886e-d70009c5d8b8">

### 6. DataBase Menu
<img width="494" alt="DataBase Menu" src="https://github.com/shiv325/PythonProjects/assets/139581888/6b1931f4-2f3a-42e3-be9a-19f3a017b44a">

### 7. Library Menu
<img width="675" alt="Library Menu" src="https://github.com/shiv325/PythonProjects/assets/139581888/a7273757-aab6-4b71-b4c2-bfac9ef4cf89">

### 8. Add New Book
<img width="497" alt="Add New Book" src="https://github.com/shiv325/PythonProjects/assets/139581888/d4a29f7f-ec15-488f-9b97-3ff0d335dd45">

### 9. List Of All Books
<img width="497" alt="List Of All Books" src="https://github.com/shiv325/PythonProjects/assets/139581888/fb5dda08-55c6-4946-8c67-8a9b13e4fd79">

### 10. Modify An Existing Book
<img width="497" alt="Modify An Existing Book" src="https://github.com/shiv325/PythonProjects/assets/139581888/2509b8c8-b4e9-42b9-87b6-5814e0b16c0a">

### 11. School Menu
<img width="497" alt="School Menu" src="https://github.com/shiv325/PythonProjects/assets/139581888/a468dab2-4962-4995-b33c-bdf290539ad5">

### 12. Add New Student
<img width="497" alt="Add New Student" src="https://github.com/shiv325/PythonProjects/assets/139581888/93731d65-4d93-40d5-8d94-6900898ddc67">

### 13. List Of All Students
<img width="497" alt="List Of All Students" src="https://github.com/shiv325/PythonProjects/assets/139581888/592a5d9b-39d3-4657-8d0b-f80da77dc722">

### 14. Modify Existing Student Record
<img width="497" alt="Modify Existing Student Record" src="https://github.com/shiv325/PythonProjects/assets/139581888/c28c5917-30c5-4580-b24f-6f90f86d65eb">

### 15. Issue a Book
<img width="494" alt="Issue a Book" src="https://github.com/shiv325/PythonProjects/assets/139581888/3d849390-a6a5-4b29-a4eb-285ee6a7adec">

### 16. List of All Issued Books
<img width="507" alt="List of All Issued Books" src="https://github.com/shiv325/PythonProjects/assets/139581888/98d3254f-3ef0-45c2-bdb8-0cab12e5cc43">

### 17. Return Issued Book
<img width="507" alt="Return Issued Book" src="https://github.com/shiv325/PythonProjects/assets/139581888/e98c25bd-81e3-4307-877c-fa97ecd16698">

### 18. Delete Student Record
<img width="507" alt="Delete Student Record" src="https://github.com/shiv325/PythonProjects/assets/139581888/efbac752-8b46-4cf6-99dd-955b06eac711">

### 19. Delete Book
<img width="461" alt="Delete Book" src="https://github.com/shiv325/PythonProjects/assets/139581888/c220748e-942e-40ad-8a02-fe496c7297e2">

### 20. Exiting the Application
<img width="675" alt="Exiting the Application" src="https://github.com/shiv325/PythonProjects/assets/139581888/78925c96-bfc0-412e-a84c-945497584e97">
