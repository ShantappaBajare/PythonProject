import sqlite3
from tabulate import tabulate

def show_table_structure(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    if columns:
        print(f"\nTable Structure: {table_name}")
        print(tabulate(columns, headers=["CID", "Name", "Type", "NotNull", "Default", "PK"], tablefmt="grid"))
    else:
        print(f"\nTable '{table_name}' does not exist.")


# Connect to database
conn = sqlite3.connect("company2.db")
cursor = conn.cursor()

# -----------------------------------------
# 1️⃣ CREATE TABLE
# -----------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary REAL
);
""")
conn.commit()
print("\n✔ TABLE CREATED: employees")
show_table_structure(cursor, "employees")


# -----------------------------------------
# 2️⃣ ALTER TABLE – ADD COLUMN
# -----------------------------------------
cursor.execute("""
ALTER TABLE employees 
ADD COLUMN department TEXT;
""")
conn.commit()
print("\n✔ COLUMN ADDED: department")
show_table_structure(cursor, "employees")


# -----------------------------------------
# 3️⃣ RENAME TABLE
# -----------------------------------------
cursor.execute("""
ALTER TABLE employees 
RENAME TO staff;
""")
conn.commit()
print("\n✔ TABLE RENAMED → staff")
show_table_structure(cursor, "staff")


# -----------------------------------------
# 4️⃣ DROP TABLE
# -----------------------------------------
cursor.execute("""
DROP TABLE IF EXISTS staff;
""")
conn.commit()
print("\n✔ TABLE DROPPED: staff")
show_table_structure(cursor, "staff")


# Close database
conn.close()
