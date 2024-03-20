import psycopg2

# Note: I named my database 'Assignment3', if the database you're using is different, you can change it
# Also, please provide your own login info for the password parameter, I just left it blank after removing mine
connection = psycopg2.connect(database = "Assignment3", user = "postgres", password = "", host = "localhost", port = "5432")

cursor = connection.cursor()

def getAllStudents():
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

def addStudent(first_name, last_name, email, enrollment_date):
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES \
                   ('{fname}', '{lname}', '{mail}', '{enroll_date}');".format(fname = first_name, lname = last_name, mail = email, enroll_date = enrollment_date)
    cursor.execute(query)
    connection.commit()

def updateStudentEmail(student_id, new_email):
    query = "UPDATE students SET email = '{email}' WHERE student_id = {id}".format(email = new_email, id = student_id)
    cursor.execute(query)
    connection.commit()

def deleteStudent(student_id):
    query = "DELETE FROM students WHERE student_id = {id}".format(id = student_id)
    cursor.execute(query)
    connection.commit()


def menu():
    print("Assignment 3 Q1 Menu:")
    print("1. Question 1: getAllStudents")
    print("2. Question 2: addStudent")
    print("3. Question 3: updateStudentEmail")
    print("4. Question 4: deleteStudent")
    print("5. Exit")


while True:
    menu()
    option = input("Enter which question you want to run: ")

    if option == "1":
        print("Question 1 results: ")
        getAllStudents()
    elif option == "2":
        fname = input("Choose a first name: ")
        lname = input("Choose a last name: ")
        em = input("Choose a unique email: ")
        date = input("Choose an enrollment date: ")
        addStudent(fname, lname, em, date)
    elif option == "3":
        s_id = input("Enter the student id: ")
        new_em = input("Enter the new email: ")
        updateStudentEmail(s_id, new_em)
    elif option == "4":
        s_id = input("Enter id of student to be deleted: ")
        deleteStudent(s_id)
    elif option == "5":
        break
    else:
        print("Please select a valid option")


connection.close()
