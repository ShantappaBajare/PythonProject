"""
It is very common requirement to save data for the future purpose

temporary:available until program execution, after it will get delete by garbage collector
permanent: data will be stored inside

File systems :small scale storage areas (excel data), not suitable for huge data, no querry language support, no security
              data inconsistency(duplicate data)

Databases : large scale (oracle, postgres, mysql), data stored in tables, data secured,data consistent

limitations: not suitable for very huge data(video storage/mail storage)
             not suitable for unstructured data(image file,video files - not in tabular format) and semi structured data(xml)

Advanced data storage: Cloud/hadoop/bigData

"""

"""
Python Data Base Connectivity:

steps to connect PDBC

1. Import database specific module: cx_Oracle, pymssql, pymysql etc
2. Establish connection to the database
    con = cx_Oracle.connect(database information);
3. create a cursor object : to connect, perform operations hold results
    cursor = con.cursor()
4. execute our query
    cursor.execute(sqlquery) ---single query
    cursor.executescript(sqlqueries) -- multiple quries seperately
    cursor.executemany() -- to execute a parameterized query
5. get/fetch the result
    cursor.fetchone()------to fetch only one row
    cursor.fetchall()------to fetch all rows
    cursor.fetchmany(n)--- to fetch n rows
6.  con.commit() - save in db once comit it is permanently stored in db
    con.rollback - revert the changes before commiting
    
7. con.close()
    cursor.close()
"""

"""working with oracle database"""

# import pymysql
#
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="yourpassword",
#     database="testdb"
# )
#
# cursor = connection.cursor()
# cursor.execute("SELECT VERSION()")
# print(cursor.fetchone())
#
# cursor.close()
# connection.close()
###############################################################

# import sqlite3
#
# # create database file (if not exists)
# conn = sqlite3.connect("pythondb.db")
#
# print("Database created!")
# conn.close()

import sqlite3

# -------------------------
# 1. CONNECT TO DATABASE
# -------------------------
# conn = sqlite3.connect("company.db")
# cur = conn.cursor()
# if conn!= None:
#     print("connecting to database is success")
#     print("SQLite version:", sqlite3.sqlite_version)
#     cur.execute("select sqlite_version()")
#     print("DB version:", cur.fetchone()[0])

# delete existing table
#------------------------------------------
# cur.execute("DROP TABLE IF EXISTS employees")
# conn.commit()
# print(" employee tabled dropped successfully")

#
# # -------------------------
# # 2. CREATE TABLE
# # -------------------------
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER,
#         salary REAL
#     )
# """)
# conn.commit()
# print("\n✔ Table created")
#
# # -------------------------
# # 3. ADD A NEW COLUMN (SAFE)
# # -------------------------
# # Check if column exists before adding
# cur.execute("PRAGMA table_info(employees)")
# columns = [col[1] for col in cur.fetchall()]
#
# if "is_active" not in columns:
#     cur.execute("ALTER TABLE employees ADD COLUMN is_active INTEGER DEFAULT 1")
#     conn.commit()
#     print("✔ Column 'is_active' added")
# else:
#     print("✔ Column 'is_active' already exists")
#
# # -------------------------
# # 4. INSERT DATA
# # -------------------------
# cur.execute("DELETE FROM employees")  # Clear table to insert fresh records
#
# employees_data = [
#     ("Alice", 30, 60000),
#     ("Bob", 25, 50000),
#     ("Charlie", 35, 75000)
# ]
#
# cur.executemany("""
#     INSERT INTO employees(name, age, salary)
#     VALUES (?, ?, ?)
# """, employees_data)
#
# conn.commit()
# print("✔ 3 rows inserted")
#
# # -------------------------
# # 5. SELECT (READ DATA)
# # -------------------------
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
#
# print("\n📌 INITIAL DATA:")
# for row in rows:
#     print(row)
#
# # -------------------------
# # 6. UPDATE RECORD
# # -------------------------
# cur.execute("""
#     UPDATE employees
#     SET salary = salary + 5000
#     WHERE name = 'Bob'
# """)
# conn.commit()
# print("\n✔ Updated salary for Bob")
#
# # Display after update
# cur.execute("SELECT * FROM employees WHERE name='Bob'")
# print("Updated Bob:", cur.fetchone())
#
# # -------------------------
# # 7. DELETE RECORD
# # -------------------------
# cur.execute("DELETE FROM employees WHERE name='Charlie'")
# conn.commit()
# print("\n✔ Deleted Charlie")
#
# # Display after delete
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# print("\n📌 AFTER DELETE:")
# for row in rows:
#     print(row)
#
# # -------------------------
# # 8. SHOW TABLE SCHEMA
# # -------------------------
# print("\n📎 TABLE STRUCTURE:")
# cur.execute("PRAGMA table_info(employees)")
# for col in cur.fetchall():
#     print(col)
#
# # -------------------------
# # 9. DROP TABLE (OPTIONAL)
# # -------------------------
# # Uncomment this to remove the table completely
# cur.execute("DROP TABLE employees")
# conn.commit()
# print("✔ Table dropped")
#
# # -------------------------
# # 10. CLOSE CONNECTION
# # -------------------------
# conn.close()
# print("\n✔ Database operations completed!")
#
#
