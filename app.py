# use psycopg2 to connect to the database
import psycopg2

# Database connection dictionary
db_connect = {
    'dbname': 'school',
    'user': 'username',   # edit here (PostgreSQL username)
    'password': '',       # edit here (PostgreSQL password)
    'host': 'localhost',
    'port': '5432'
}

# connecting the database
def connect():
    return psycopg2.connect(**db_connect)

# FUNCTIONS
# In each function:
# variable conn (connection) holds the connection to the database with the dictionary values above
# cur (cursor) variable is used to send SQL commands to PostgreSQL 
# cursor and connection are closed at the end of each function

def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY first_name;")
    students = cur.fetchall()
    print("\nAll Students:")
    for s in students:
        print(s)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()

