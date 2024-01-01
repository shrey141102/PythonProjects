#===================================||
# School Library Management Project ||
#===================================||

import time
import os
import mysql.connector

def database():
    print("============================================================================")
    print("\t\t\t   Database Menu")
    print("============================================================================")
    print("Welcome User. Choose the Desired Action.")
    cursor.execute("show databases;")
    databases = cursor.fetchall()
    dbs = {}
    n = 1
    for i in databases :
        dbs[n] = i[0]
        print(str(n) + ". " + i[0])
        n += 1
    dbs[n] = "Create A New DataBase"
    dbs[n + 1] = "Exit From The Connection"
    print("****************************************************************************")
    print(str(n) + ". " + "Create A New DataBase")
    print(str(n + 1) + ". " + "Exit From The Connection")
    decision = 0
    while decision not in range(1, n + 1) :
        decision = int(input("Enter your choice => "))
        if decision in range(1, n) :
            query = "USE " + dbs[decision]
            cursor.execute(query)
            os.system("cls")
            tables(dbs[decision])
        elif decision == n :
            new_db_name = input("Enter The New DataBase Name(A-Z,a-z,0-9,_) => ")
            if new_db_name == "" :
                print("Can't assign Null Value")
            else :
                dec = input("Are you sure you want to Create This DataBase?(y/n) => ")
                if dec == "y":
                    query = "create database " + new_db_name
                    cursor.execute(query)
                    cnx.commit()
                    print("Successfully created '" + new_db_name + "' DataBase...")
            input("Press Enter to go to DataBase Menu...")
            os.system("cls")
            database()
        elif decision == n + 1 :
            os.system("cls")
            exit_decision = input("Are you sure you want to Exit?(y/n) => ")
            if exit_decision == "y" :
                cnx.close()
                print("See ya later.")
                time.sleep(3)
                quit()
            else :
                os.system("cls")
                database()
        else :
            print("Please enter from the given choices.")



def tables(db) :
    print("============================================================================")
    print("\t\t\tTables In", db.title())
    print("============================================================================")
    cursor.execute("show tables")
    tables = cursor.fetchall()
    n = 1
    for i in tables :
        print(str(n) + ". " + i[0])
        n += 1
    print("****************************************************************************")
    print("This Python Program Will Now Use These 3 Tables in this DataBase:")
    print("$. School_Students  $. Library_Books  $. Issued_Books")
    print("If these tables exist already with the Specified Columns in ReadMe, use")
    print("them directly. Otherwise Create these Tables.")
    decision = input("Do you want to Create these Tables here?(y/n) => ")
    if decision == "y":
        cursor.execute("""CREATE TABLE IF NOT EXISTS issued_books (
  Accession_No int NOT NULL PRIMARY KEY CHECK (Accession_No > 0),
  Book_Name varchar(200) NOT NULL,
  RNo int NOT NULL CHECK (RNO > 0),
  Student_Name varchar(100) NOT NULL,
  Date_Of_Issue date NOT NULL
  )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS library_books (
  Accession_No int NOT NULL PRIMARY KEY CHECK (Accession_No > 0),
  Book_Name varchar(200) NOT NULL,
  Price_In_Rs int NOT NULL CHECK (Price_In_Rs > 0),
  Author varchar(100) NOT NULL
  )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS school_students (
  RNo int NOT NULL PRIMARY KEY CHECK (RNo > 0),
  Student_Name varchar(200) NOT NULL,
  Class int NOT NULL CHECK (Class > 0),
  Section varchar(100) NOT NULL
  )""")
        cnx.commit()
        print("Tables Created Successfully...")
    decision = input("Do you want to Use these Tables here?(y/n) => ")
    if decision == "y" :
        os.system("cls")
        menu()
    else :
        os.sytem("cls")
        database()
    

def menu() :
    print("============================================================================")
    print("\t\t\t\tMenu")
    print("============================================================================")
    print("Welcome User. Choose the desired action.")
    print("1. Library")
    print("2. School")
    print("3. Exit to Databases")
    print("Note* : For a better experience, open the program in python terminal.")
    print("****************************************************************************")
    decision = 0
    while decision not in ("1", "2", "3") :
        decision = input("Enter your choice => ")
        if decision not in ("1", "2", "3") :
            print("Please enter from the given choices.")
        if decision == "1" :
            os.system("cls")
            library()
        elif decision == "2" :
            os.system("cls")
            school()
        elif decision == "3" :
            os.system("cls")
            exit_decision = input("Are you sure you want to Exit?(y/n) => ")
            if exit_decision == "y" :
                os.system("cls")
                databases()
            else :
                os.system("cls")
                menu()


def library() :
    print("============================================================================")
    print("\t\t\t\tLibrary")
    print("============================================================================")
    print("Welcome to the Library. Choose the desired action.")
    print("1. Show all Books")
    print("2. Add a New Book")
    print("3. Delete an Existing Book")
    print("4. Modify an Existing Book")
    print("5. Issue a Book to a Student")
    print("6. Return an Issued Book")
    print("7. Show all the Books Issued to Students")
    print("8. Back to the Menu")
    print("Note* : For a better experience, open the program in python terminal.")
    print("****************************************************************************")
    decision = 0
    while decision not in ("1", "2", "3", "4", "5", "6", "7", "8") :
        decision = input("Enter your choice => ")
        if decision not in ("1", "2", "3", "4", "5", "6", "7", "8") :
            print("Please enter from the given choices.")
        if decision == "1" :
            os.system("cls")
            show_books()
        elif decision == "2" :
            os.system("cls")
            add_book()
        elif decision == "3" :
            os.system("cls")
            delete_book()
        elif decision == "4" :
            os.system("cls")
            modify_book()
        elif decision == "5" :
            os.system("cls")
            issue_book()
        elif decision == "6" :
            os.system("cls")
            return_book()
        elif decision == "7" :
            os.system("cls")
            show_issued_books()
        elif decision == "8" :
            os.system("cls")
            menu()



def school() :
    print("============================================================================")
    print("\t\t\t\tSchool")
    print("============================================================================")
    print("Welcome to the School. Choose the desired action.")
    print("1. Show Details of All Students")
    print("2. Add a New Student Record")
    print("3. Delete an Existing Student Record")
    print("4. Modify an Existing Student Record")
    print("5. Back to the Menu")
    print("Note* : For a better experience, open the program in python terminal.")
    print("****************************************************************************")
    decision = 0
    while decision not in ("1", "2", "3", "4", "5") :
        decision = input("Enter your choice => ")
        if decision not in ("1", "2", "3", "4", "5") :
            print("Please enter from the given choices.")
        if decision == "1" :
            os.system("cls")
            show_students()
        elif decision == "2" :
            os.system("cls")
            add_student()
        elif decision == "3" :
            os.system("cls")
            delete_student()
        elif decision == "4" :
            os.system("cls")
            modify_student()
        elif decision == "5" :
            os.system("cls")
            menu()


def show_books() :
    print("============================================================================")
    print("\t\t\t List of All Books")
    print("============================================================================")
    cursor.execute("select * from library_books;")
    data = cursor.fetchall()
    n = 1
    for row in data :
        print(str(n) + ". Accesion No. : {0}\n Book Name : {1}\n Author :  {2}\n Price : {3}".format(row[0], row[1], row[2], row[3]))
        n += 1
    print("****************************************************************************")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()



def add_book() :
    print("============================================================================")
    print("\t\t\t Adding a New Book")
    print("============================================================================")
    cursor.execute("select accession_no, book_name from library_books;")
    data = cursor.fetchall()
    a = [ ]
    b = [ ]
    for i in data :
        a.append(i[0])
        b.append(i[1])
    acc_no = int(input("Enter the Accession No.(4 digits) => "))
    if not (999 < acc_no < 10000) :
        print("The input Accession No. must be a 4-digit number.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    elif acc_no in a :
        print("The input Accession No. already exists.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    book_name = input("Enter the Book Name => ")
    if book_name == "" :
        print("Can't input Null Value.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    elif book_name in b :
        print("The input Book Name already exists.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    author = input("Enter the Name of Author => ")
    if author == "" :
        print("Can't input Null Value.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    price = int(input("Enter the Price(Rs.) of Book => "))
    if price <= 0 :
        print("Price must be greater than 0.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    decision = input("Are you sure you want to add this book?(y/n) => ")
    if decision == "y" :
        data = (acc_no, book_name.title(), author.title(), price)
        query = "insert into library_books(accession_no, book_name, author, price_in_rs) values(%s, %s, %s, %s)"
        cursor.execute(query, data)
        cnx.commit()
        print("Data entered successfully.")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()



def delete_book() :
    print("============================================================================")
    print("\t\t\t Deleting an Existing Book")
    print("============================================================================")
    cursor.execute("select accession_no from library_books;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    acc_no = int(input("Enter the Accession No. => "))
    if acc_no not in a :
        print("The input Accession No. doesn't exist.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    data = (acc_no,)
    query = "select book_name, author, price_in_rs from library_books where accession_no = (%s)"
    cursor.execute(query, data)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Book Name :", b[0])
    print("Author :", b[1])
    print("Price :", b[2])
    decision = input("Are you sure you want to delete this book?(y/n) => ")
    if decision == "y" :
        cursor.execute("select accession_no from issued_books;")
        data = cursor.fetchall()
        c = [ ]
        for i in data :
            c.append(i[0])
        if acc_no in c :
            print("This book has already been issued by someone else.")
            print("It must be  returned to the Library before it can be deleted.")
            input("Press Enter to go back to the Library...")
            os.system("cls")
            library()
        data = (acc_no,)
        query = "delete from library_books where accession_no = (%s)"
        cursor.execute(query, data)
        cnx.commit()
        print("The given book has been deleted.")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()



def modify_book() :
    print("============================================================================")
    print("\t\t\t Modifying an Existing Book")
    print("============================================================================")
    cursor.execute("select accession_no from library_books;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    acc_no = int(input("Enter the Accession No. => "))
    if acc_no not in a :
        print("The input Accession No. doesn't exist.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    arg = (acc_no,)
    query = "select book_name, author, price_in_rs from library_books where accession_no = (%s)"
    cursor.execute(query, arg)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Book Name :", b[0])
    print("Author :", b[1])
    print("Price :", b[2])
    decision = input("Are you sure you want to modify this book?(y/n) => ")
    if decision == "y" :
        cursor.execute("select accession_no from issued_books;")
        data = cursor.fetchall()
        c = [ ]
        for i in data :
            c.append(i[0])
        if acc_no in c :
            print("This book has been issued by someone.")
            print("It must be returned to the Lbrary before it can be modified.")
            input("Press Enter to go back to the Library...")
            os.system("cls")
            library()
        book_name = input("Enter the New Book Name => ").title()
        if book_name == "" :
            print("Can't input Null Value.")
            input("Press Enter to go back to the Library...")
            os.system("cls")
            library()
        author = input("Enter the New Author Name => ").title()
        if author == "" :
            print("Can't input Null Value.")
            input("Press Enter to go back to the Library...")
            os.system("cls")
            library()
        price = int(input("Enter the New Price => "))
        if price <= 0 :
            print("Price must be greater than 0.")
            input("Press Enter to go back to the Library...")
            os.system("cls")
            library()
        decision = input("Are you sure these new details are correct?(y/n) => ")
        if decision == "y" :
            arg = (book_name, author, price, acc_no)
            query = "update library_books set book_name = (%s), author = (%s), price_in_rs = (%s) where accession_no = (%s)"
            cursor.execute(query, arg)
            cnx.commit()
            print("The given book has been modified.")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()



def issue_book() :
    print("============================================================================")
    print("\t\t\t\tIssuing a Book")
    print("============================================================================")
    cursor.execute("select accession_no from library_books;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    acc_no = int(input("Enter the Accession No. => "))
    if acc_no not in a :
        print("The input Accession No. doesn't exist.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    arg = (acc_no,)
    query = "select book_name, author, price_in_rs from library_books where accession_no = (%s)"
    cursor.execute(query, arg)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Book Name :", b[0])
    print("Author :", b[1])
    print("Price :", b[2])
    cursor.execute("select rno from school_students;")
    data = cursor.fetchall()
    c = [ ]
    for i in data :
        c.append(i[0])
    rno = int(input("Enter the Student Roll No. to whom you are issuing => "))
    if rno not in c :
        print("The input Roll No. doesn't exist.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    arg = (rno,)
    query = "select student_name, class, section from school_students where rno = (%s)"
    cursor.execute(query, arg)
    data = cursor.fetchall()
    d = [ ]
    for i in data :
        d.append(i[0])
        d.append(i[1])
        d.append(i[2])
    print("Student Name :", d[0])
    print("Class :", d[1])
    print("Section :", d[2])
    decision = input("Are you sure you want to issue this book to this student?(y/n) => ")
    if decision == "y" :
        query = "insert into issued_books values(%s, %s, %s, %s, curdate())"
        arg = (acc_no, d[0], rno, b[0])
        cursor.execute(query, arg)
        cnx.commit()
        print("The given book has been issued.")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()



def return_book() :
    print("============================================================================")
    print("\t\t\t\tReturn an Issued Book")
    print("============================================================================")
    cursor.execute("select accession_no from issued_books;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    acc_no = int(input("Enter the Accession No. => "))
    if acc_no not in a :
        print("The input Accession No. has not been issued.")
        input("Press Enter to go back to the Library...")
        os.system("cls")
        library()
    data = (acc_no,)
    query = "select rno, student_name, date_of_issue from issued_books where accession_no = (%s)"
    cursor.execute(query, data)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Roll No. :", b[0])
    print("Student Name :", b[1])
    print("Date of Issue :", b[2])
    data = (acc_no,)
    query = "select book_name, author, price_in_rs from library_books where accession_no = (%s)"
    cursor.execute(query, data)
    data = cursor.fetchall()
    c = [ ]
    for i in data :
        c.append(i[0])
        c.append(i[1])
        c.append(i[2])
    print("Book Name :", c[0])
    print("Author :", c[1])
    print("Price :", c[2])
    decision = input("Are you sure you want to return this book?(y/n) => ")
    if decision == "y" :
        data = (acc_no,)
        query = "delete from issued_books where accession_no = (%s)"
        cursor.execute(query, data)
        cnx.commit()
        print("The given book has been returned.")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()


def show_issued_books() :
    print("============================================================================")
    print("\t\t\tList of All Issued Books")
    print("============================================================================")
    cursor.execute("select accession_no, book_name, rno, student_name, date_of_issue from issued_books;")
    data = cursor.fetchall()
    n = 1
    for row in data :
        print(str(n) + ". Accesion No. : {0}\n Book Name : {1}\n Roll No. : {2}\n Student Name : {3}\n Date of Issue : {4}".format(row[0], row[1],  row[2], row[3], row[4]))
        n += 1
    print("****************************************************************************")
    input("Press Enter to go back to the Library...")
    os.system("cls")
    library()


def show_students() :
    print("============================================================================")
    print("\t\t\t List of All Students")
    print("============================================================================")
    cursor.execute("select * from school_students;")
    data = cursor.fetchall()
    n = 1
    for row in data :
        print(str(n) + ". Roll No. : {0}\n Student Name : {1}\n Class : {2}\n Section : {3}".format(row[0], row[1], row[2], row[3]))
        n += 1
    print("****************************************************************************")
    input("Press Enter to go back to the School...")
    os.system("cls")
    school()


def add_student() :
    print("============================================================================")
    print("\t\t\t Adding a New Student")
    print("============================================================================")
    cursor.execute("select rno from school_students;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    rno = int(input("Enter the Roll No.(4 digits) => "))
    if rno == None :
        print("Can't input Null Value.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    if not (999 < rno < 10000) :
        print("The input Roll No. must be a 4-digit number.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    elif rno in a :
        print("The input Roll No. already exists.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    student_name = input("Enter the Student Name => ")
    if student_name == "" :
        print("Can't input Null Value.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    class_ = int(input("Enter the Class => "))
    if class_ == None :
        print("Can't input Null Value.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    elif not class_ in range(1,13) :
        print("Class must lie between 1 and 12(including these also).")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    section = input("Enter the Section(A/B) => ")
    if section.title() not in ("A", "B") :
        print("Section must be either 'A' or 'B'.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    elif section == None :
        print("Can't input Null Value.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    decision = input("Are you sure you want to add this student record?(y/n) => ")
    if decision == "y" :
        data = (rno, student_name.title(), class_ , section.title())
        query = "insert into school_students(rno, student_name, class, section) values(%s, %s, %s, %s)"
        cursor.execute(query, data)
        cnx.commit()
        print("Data entered successfully.")
    input("Press Enter to go back to the School...")
    os.system("cls")
    school()



def delete_student() :
    print("============================================================================")
    print("\t\t Deleting an Existing Student Record")
    print("============================================================================")
    cursor.execute("select rno from school_students;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    rno = int(input("Enter the Roll No. => "))
    if rno not in a :
        print("The input Roll No. doesn't exist.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    data = (rno,)
    query = "select student_name, class, section from school_students where rno = (%s)"
    cursor.execute(query, data)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Student Name :", b[0])
    print("Class :", b[1])
    print("Section :", b[2])
    decision = input("Are you sure you want to delete this student record?(y/n) => ")
    if decision == "y" :
        cursor.execute("select rno from issued_books;")
        data = cursor.fetchall()
        c = [ ]
        for i in data :
            c.append(i[0])
        if rno in c :
            print("This student has issued a book.")
            print("That book must be  returned to the Lbrary before this record can be deleted.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        data = (rno,)
        query = "delete from school_students where rno = (%s)"
        cursor.execute(query, data)
        cnx.commit()
        print("The given student record has been deleted.")
    input("Press Enter to go back to the School...")
    os.system("cls")
    school()


def modify_student() :
    print("============================================================================")
    print("\t\t Modifying an Existing Student Record")
    print("============================================================================")
    cursor.execute("select rno from school_students;")
    data = cursor.fetchall()
    a = [ ]
    for i in data :
        a.append(i[0])
    rno = int(input("Enter the Roll No. => "))
    if rno not in a :
        print("The input Roll No. doesn't exist.")
        input("Press Enter to go back to the School...")
        os.system("cls")
        school()
    arg = (rno,)
    query = "select student_name, class, section from school_students where rno = (%s)"
    cursor.execute(query, arg)
    data = cursor.fetchall()
    b = [ ]
    for i in data :
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
    print("Student Name :", b[0])
    print("Class :", b[1])
    print("Section :", b[2])
    decision = input("Are you sure you want to modify this student record?(y/n) => ")
    if decision == "y" :
        cursor.execute("select rno from issued_books;")
        data = cursor.fetchall()
        c = [ ]
        for i in data :
            c.append(i[0])
        if rno in c :
            print("This student has issued a book.")
            print("That book must be returned to the Lbrary before this record can be modified.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        student_name = input("Enter the New Student Name => ")
        if student_name == "" :
            print("Can't input Null Value.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        class_ = int(input("Enter the Class(1-12) => "))
        if class_ == None :
            print("Can't input Null Value.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        elif not class_ in range(1,13) :
            print("Class must lie between 1 and 12(including these also).")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        section = input("Enter the Section(A/B) => ")
        if section.title() not in ("A", "B") :
            print("Section must be either 'A' or 'B'.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        elif section == None :
            print("Can't input Null Value.")
            input("Press Enter to go back to the School...")
            os.system("cls")
            school()
        decision = input("Are you sure these New Details are Correct?(y/n)  => ")
        if decision == "y" :
            arg = (student_name.title(), class_, section.title(), rno)
            query = "update school_students set student_name = (%s), class = (%s), section = (%s) where rno = (%s)"
            cursor.execute(query, arg)
            cnx.commit()
            print("The Given Student Record has been Modified.")
    input("Press Enter to go back to the School...")
    os.system("cls")
    school()


username = input("Enter the User Name for MySQL Conenction => ")
password = input("Enter the Password to access the MySQL Connection => ")
os.system("cls")
try :
    cnx = mysql.connector.connect(host = "127.0.0.1", user = username, passwd = password)
except :
    print("Incorrect Password.")
    input("Press Enter to Close the Program...")
    exit
if cnx :
    print(cnx)
    print("Successfully Connected...")
    cursor = cnx.cursor()
    input("Press Enter to Access the Database Menu...")
    os.system("cls")
    database()

