import sqlite3
from tabulate import tabulate


def show_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    if rows:
        col_names = [description[0] for description in cursor.description]
        print(f"\nCurrent Data in {table_name}:")
        print(tabulate(rows, headers=col_names, tablefmt="grid"))
    else:
        print(f"\nNo data found in {table_name}.")


# Connect to database
conn = sqlite3.connect("company2.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE employees
ADD COLUMN department TEXT;
""")
conn.commit()



# -----------------------------------------
# 1️⃣ INSERT DATA
# -----------------------------------------
cursor.execute("""
               INSERT INTO employees (name, age, salary, department)
               VALUES ('John', 30, 50000, 'Engineering');
               """)

cursor.execute("""
               INSERT INTO employees (name, age, salary, department)
               VALUES ('Sara', 26, 48000, 'HR');
               """)

cursor.execute("""
               INSERT INTO employees (name, age, salary, department)
               VALUES ('Peter', 32, 55000, 'Finance');
               """)

conn.commit()
print("\n✔ Data Inserted Successfully")
show_data(cursor, "employees")

# -----------------------------------------
# 2️⃣ UPDATE DATA
# -----------------------------------------
cursor.execute("""
               UPDATE employees
               SET salary = salary + 5000
               WHERE name = 'John';
               """)
conn.commit()
print("\n✔ Salary Updated for John")
show_data(cursor, "employees")

# -----------------------------------------
# 3️⃣ DELETE DATA
# -----------------------------------------
cursor.execute("""
               DELETE
               FROM employees
               WHERE name = 'Sara';
               """)
conn.commit()
print("\n✔ Deleted record of Sara")
show_data(cursor, "employees")

# -----------------------------------------
# 4️⃣ SELECT (filter example)
# -----------------------------------------
cursor.execute("""
               SELECT name, salary
               FROM employees
               WHERE salary > 52000;
               """)

rows = cursor.fetchall()
print("\n✔ Employees with salary > 52000")
print(tabulate(rows, headers=["Name", "Salary"], tablefmt="grid"))

# Close connection
conn.close()
