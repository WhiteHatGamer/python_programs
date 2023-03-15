#just for Adding SQL Commands, Rules etc...
#PyMySql - Libraries for connecting SQL This one for MySQL
#sqlite3 - for slqlite3
import sqlite3
import db_connection
conn = sqlite3.connect("hellow_world\employee.db")
cur = sqlite3.Cursor(conn)
TABLE_NAME = "Employee1"
create_table = f"CREATE TABLE {TABLE_NAME} (emp_id,emp_name,emp_no)"
cur.execute(create_table)

def insert_employee(emp_id,emp_name,emp_no):
    cur.execute(f"""
    INSERT INTO employee1 VALUES
        ({emp_id}, {emp_name}, {emp_no})
    """)
    conn.commit()


def display_employee():
    res = cur.execute(f"SELECT * FROM {TABLE_NAME}")
    print(res.fetchall())


#DELETE from {table_name} where {condition}
#fetchone(), fetchmany({no_of_records}), fetchall()
#cur.rowcount()
#

display_employee()
conn.close()
