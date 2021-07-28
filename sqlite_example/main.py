import sqlite3
from sqlite3 import Error


def db_connect(db_file_name):
    conn = sqlite3.connect(db_file_name)
    # conn = sqlite3.connect(':memory:')  this will not create a file
    #print(conn)
    return conn


def create_table(conn):
    student_table = """CREATE TABLE IF NOT EXISTS student (
                        sid INT PRIMARY KEY,
                        snm TEXT
                        );"""
    cursor = conn.cursor()
    cursor.execute(student_table)

def insert_student(conn,sid,snm):
    print("in insert")
    sql = """INSERT INTO student VALUES (?,?)"""
    cur = conn.cursor()
    cur.execute(conn, (sid,snm))
    conn.commit()
def select_student(conn):
    sql = "SELECT * FROM student"
    cur = conn.cursor()
    cur.executes(sql)

    dataRows = cur.fetchall()
    for row in dataRows:
        print(row)


if __name__ == '_main_':
    print(sqlite3.version)
    conn = db_connect("student.db")
    create_table(conn)
    insert_student(conn,1,"param")
    select_student(conn)