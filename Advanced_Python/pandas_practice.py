"""data analysis library"""
"""
from pandas we can do :
1. Reading & Writing Data to excel,csv,text,json,pickle,sql,html etc
2. DataFrame Creation : list,dictionary,np array, another array
3. Data Inspection : head(), tail(), info(), describe(), shape, columns, dtypes
4. Selecting & Filtering Data: df['col'],df[['col1','col2']],loc[] (label-based),iloc[] (index-based),Conditional filtering: df[df['age'] > 30]
5. Modifying Data : Add new column,Modify column,Delete column,Rename column
6. Handling Missing Data : isnull(),fillna(),dropna()
7. Sorting : sort_values(),sort_index()
8. Grouping & Aggregation : groupby(),sum(), mean(), count(), etc.
9. Merging / Joining : merge(),join(),concat()
10.Applying Functions : apply(),map(),applymap(),Lambda operations
11.Working with Dates & Time : Convert to datetime,Extract day/month/year,Date filtering
12.Pivot Tables
13.Statistics & Math:max(), min(), mean(), std(), etc.
"""

"""
Pandas is common in testing for:

1. Data comparison
2. Reading UI/API test data
3. Data validation
4 Log analysis
5 Converting output to CSV/Excel reports
6 Comparing expected vs actual test results
"""

#1. Reading & Writing Data to excel,csv,text,json,pickle,sql,html etc

"""
import pandas as pd

#Create a sample Excel file
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 72]
}

df = pd.DataFrame(data)
df.to_excel("sample.xlsx", index=False) # index=False - do not write the DataFrame row index into the Excel file.

print("sample.xlsx created")

# Read it back
df = pd.read_excel("sample.xlsx")
print(df)

# Create and write data to data.txt

with open("data1.txt", "w") as f:
    f.write("Name,Age,City\n")
    f.write("Ravi,25,Bangalore\n")
    f.write("Sita,30,Hyderabad\n")
    f.write("Arjun,28,Chennai\n")

print("data.txt created successfully!")

df = pd.read_csv("data1.txt")
print(df)

"""

# Data Inspection : head(), tail(), info(), describe(), shape, columns, dtypes
"""
import pandas as pd

# --------------------------------------------------
# 1. Create sample data
# --------------------------------------------------
data = {
    "name": ["John", "Alice", "Bob", "David", "Mary", "Chris", "Mohan"],
    "age": [25, 30, 22, 28, 35, 40, 26],
    "salary": [50000, 65000, 48000, 52000, 70000, 72000, 51000],
    "dept": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)
print("data frame created")

# --------------------------------------------------
# 2. Write to CSV
# --------------------------------------------------
df.to_csv("employees.csv", index=False)
print("CSV file created!\n")
#
# --------------------------------------------------
# 3. Read from CSV
# --------------------------------------------------
df = pd.read_csv("employees.csv")

print("\n===== DataFrame Loaded =====")
print(df)

# --------------------------------------------------
# 4. Data Inspection Functions
# --------------------------------------------------

# A. Show first 5 rows
print("\n===== HEAD (first 5 rows) =====")
print(df.head())
#
# B. Show last 3 rows
print("\n===== TAIL (last 3 rows) =====")
print(df.tail(3))
#
# C. Full info
print("\n===== INFO =====")
print(df.info())
#
# D. Statistical summary
print("\n===== DESCRIBE =====")
print(df.describe())
#
# E. Shape of dataframe
print("\n===== SHAPE =====")
print("Rows, Columns:", df.shape)
#
# F. List of columns
print("\n===== COLUMNS =====")
print(df.columns)
#
# G. Data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

"""
"""
The results of all these activities

data frame created
CSV file created!


===== DataFrame Loaded =====
    name  age  salary     dept
0   John   25   50000       IT
1  Alice   30   65000       HR
2    Bob   22   48000  Finance
3  David   28   52000       IT
4   Mary   35   70000       HR
5  Chris   40   72000  Finance
6  Mohan   26   51000       IT

===== HEAD (first 5 rows) =====
    name  age  salary     dept
0   John   25   50000       IT
1  Alice   30   65000       HR
2    Bob   22   48000  Finance
3  David   28   52000       IT
4   Mary   35   70000       HR

===== TAIL (last 3 rows) =====
    name  age  salary     dept
4   Mary   35   70000       HR
5  Chris   40   72000  Finance
6  Mohan   26   51000       IT

===== INFO =====
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    7 non-null      object
 1   age     7 non-null      int64 
 2   salary  7 non-null      int64 
 3   dept    7 non-null      object
dtypes: int64(2), object(2)
memory usage: 356.0+ bytes
None

===== DESCRIBE =====
             age        salary
count   7.000000      7.000000
mean   29.428571  58285.714286
std     6.214423  10307.186582
min    22.000000  48000.000000
25%    25.500000  50500.000000
50%    28.000000  52000.000000
75%    32.500000  67500.000000
max    40.000000  72000.000000

===== SHAPE =====
Rows, Columns: (7, 4)

===== COLUMNS =====
Index(['name', 'age', 'salary', 'dept'], dtype='object')

===== DATA TYPES =====
name      object
age        int64
salary     int64
dept      object
dtype: object

"""

# Selecting & Filtering Data
"""

import pandas as pd

# --------------------------------------------------
# 1. Create sample data
# --------------------------------------------------
data = {
    "name": ["John", "Alice", "Bob", "David", "Mary", "Chris", "Mohan"],
    "age": [25, 30, 22, 28, 35, 40, 26],
    "salary": [50000, 65000, 48000, 52000, 70000, 72000, 51000],
    "dept": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)

print("=========== FULL DATA ==========")
print(df)

# --------------------------------------------------
# 2. Select Single Column
# --------------------------------------------------
print("\n=========== Single Column (df['name']) ==========")
print(df["name"])

# --------------------------------------------------
# 3. Select Multiple Columns
# --------------------------------------------------
print("\n=========== Multiple Columns (df[['name', 'salary']]) ==========")
print(df[["name", "salary"]])

# --------------------------------------------------
# 4. Using loc[] --> label-based indexing
# --------------------------------------------------
print("\n=========== loc[] (Rows 1 to 4, columns 'name' & 'age') ==========")
print(df.loc[1:4, ["name", "age"]])

# --------------------------------------------------
# 5. Using iloc[] --> index-based indexing
# --------------------------------------------------
print("\n=========== iloc[] (Rows 0 to 3, first 2 columns) ==========")
print(df.iloc[0:4, 0:2])

# --------------------------------------------------
# 6. Conditional Filtering
# --------------------------------------------------

# A. Employees older than 30
print("\n=========== Age > 30 ==========")
print(df[df["age"] > 30])

# B. Salary greater than 60k
print("\n=========== Salary > 60000 ==========")
print(df[df["salary"] > 60000])

# C. Employees in IT department
print("\n=========== dept == 'IT' ==========")
print(df[df["dept"] == "IT"])

# D. Multiple conditions (Age > 30 AND Salary > 60000)
print("\n=========== (age > 30) AND (salary > 60000) ==========")
print(df[(df["age"] > 30) & (df["salary"] > 60000)])
"""
"""
result is 

=========== FULL DATA ==========
    name  age  salary     dept
0   John   25   50000       IT
1  Alice   30   65000       HR
2    Bob   22   48000  Finance
3  David   28   52000       IT
4   Mary   35   70000       HR
5  Chris   40   72000  Finance
6  Mohan   26   51000       IT

=========== Single Column (df['name']) ==========
0     John
1    Alice
2      Bob
3    David
4     Mary
5    Chris
6    Mohan
Name: name, dtype: object

=========== Multiple Columns (df[['name', 'salary']]) ==========
    name  salary
0   John   50000
1  Alice   65000
2    Bob   48000
3  David   52000
4   Mary   70000
5  Chris   72000
6  Mohan   51000

=========== loc[] (Rows 1 to 4, columns 'name' & 'age') ==========
    name  age
1  Alice   30
2    Bob   22
3  David   28
4   Mary   35

=========== iloc[] (Rows 0 to 3, first 2 columns) ==========
    name  age
0   John   25
1  Alice   30
2    Bob   22
3  David   28

=========== Age > 30 ==========
    name  age  salary     dept
4   Mary   35   70000       HR
5  Chris   40   72000  Finance

=========== Salary > 60000 ==========
    name  age  salary     dept
1  Alice   30   65000       HR
4   Mary   35   70000       HR
5  Chris   40   72000  Finance

=========== dept == 'IT' ==========
    name  age  salary dept
0   John   25   50000   IT
3  David   28   52000   IT
6  Mohan   26   51000   IT

=========== (age > 30) AND (salary > 60000) ==========
    name  age  salary     dept
4   Mary   35   70000       HR
5  Chris   40   72000  Finance

Process finished with exit code 0

"""

# Modifying Data : Add new column,Modify column,Delete column,Rename column

"""
import pandas as pd

# --------------------------------------------------
# 1. Create sample data
# --------------------------------------------------
data = {
    "name": ["John", "Alice", "Bob", "David", "Mary"],
    "age": [25, 30, 22, 28, 35],
    "salary": [50000, 65000, 48000, 52000, 70000],
}

df = pd.DataFrame(data)

print("=========== ORIGINAL DATA ==========")
print(df)

# --------------------------------------------------
# 2. Add New Column
# --------------------------------------------------
df["dept"] = ["IT", "HR", "Finance", "IT", "HR"]   # Add column

print("\n=========== AFTER ADDING COLUMN 'dept' ==========")
print(df)

# --------------------------------------------------
# 3. Modify Column (increase salary by 10%)
# --------------------------------------------------
df["salary"] = df["salary"] * 1.10

print("\n=========== AFTER MODIFYING 'salary' ==========")
print(df)

# --------------------------------------------------
# 4. Delete Column
# --------------------------------------------------
df.drop("dept", axis=1, inplace=True)

print("\n=========== AFTER DELETING COLUMN 'dept' ==========")
print(df)

# --------------------------------------------------
# 5. Rename Columns
# --------------------------------------------------
df.rename(columns={"name": "employee_name", "salary": "monthly_salary"}, inplace=True)

print("\n=========== AFTER RENAMING COLUMNS ==========")
print(df)

# output is 

=========== ORIGINAL DATA ==========
    name  age  salary
0   John   25   50000
1  Alice   30   65000
2    Bob   22   48000
3  David   28   52000
4   Mary   35   70000

=========== AFTER ADDING COLUMN 'dept' ==========
    name  age  salary     dept
0   John   25   50000       IT
1  Alice   30   65000       HR
2    Bob   22   48000  Finance
3  David   28   52000       IT
4   Mary   35   70000       HR

=========== AFTER MODIFYING 'salary' ==========
    name  age   salary     dept
0   John   25  55000.0       IT
1  Alice   30  71500.0       HR
2    Bob   22  52800.0  Finance
3  David   28  57200.0       IT
4   Mary   35  77000.0       HR

=========== AFTER DELETING COLUMN 'dept' ==========
    name  age   salary
0   John   25  55000.0
1  Alice   30  71500.0
2    Bob   22  52800.0
3  David   28  57200.0
4   Mary   35  77000.0

=========== AFTER RENAMING COLUMNS ==========
  employee_name  age  monthly_salary
0          John   25         55000.0
1         Alice   30         71500.0
2           Bob   22         52800.0
3         David   28         57200.0
4          Mary   35         77000.0
"""

# Handling Missing Data : isnull(),fillna(),dropna()
"""
import pandas as pd

# --------------------------------------------------
# 1. Create sample data
# --------------------------------------------------
data = {
    "name": ["John", "Alice", "Bob", "David", "Mary"],
    "age": [25, 30, 22, 28, 35],
    "salary": [50000, 65000, 48000, 52000, 70000],
}

df = pd.DataFrame(data)

print("=========== ORIGINAL DATA ==========")
print(df)

# --------------------------------------------------
# 2. Add New Column
# --------------------------------------------------
df["dept"] = ["IT", "HR", "Finance", "IT", "HR"]   # Add column

print("\n=========== AFTER ADDING COLUMN 'dept' ==========")
print(df)

# --------------------------------------------------
# 3. Modify Column (increase salary by 10%)
# --------------------------------------------------
df["salary"] = df["salary"] * 1.10

print("\n=========== AFTER MODIFYING 'salary' ==========")
print(df)

# --------------------------------------------------
# 4. Delete Column
# --------------------------------------------------
df.drop("dept", axis=1, inplace=True) # axis=0 means operate on rows, when used delete row
                                             # axis=1 means operate on columns, when used delete column
                                             # inplace=True make changes directly to the original DataFrame
                                             # inplace=False return a new modified DataFrame but original stays unchanged

print("\n=========== AFTER DELETING COLUMN 'dept' ==========")
print(df)

# --------------------------------------------------
# 5. Rename Columns
# --------------------------------------------------
df.rename(columns={"name": "employee_name", "salary": "monthly_salary"}, inplace=True)

print("\n=========== AFTER RENAMING COLUMNS ==========")
print(df)

----------------Results are---------------------------

=========== ORIGINAL DATA ==========
    name  age  salary
0   John   25   50000
1  Alice   30   65000
2    Bob   22   48000
3  David   28   52000
4   Mary   35   70000

=========== AFTER ADDING COLUMN 'dept' ==========
    name  age  salary     dept
0   John   25   50000       IT
1  Alice   30   65000       HR
2    Bob   22   48000  Finance
3  David   28   52000       IT
4   Mary   35   70000       HR

=========== AFTER MODIFYING 'salary' ==========
    name  age   salary     dept
0   John   25  55000.0       IT
1  Alice   30  71500.0       HR
2    Bob   22  52800.0  Finance
3  David   28  57200.0       IT
4   Mary   35  77000.0       HR

=========== AFTER DELETING COLUMN 'dept' ==========
    name  age   salary
0   John   25  55000.0
1  Alice   30  71500.0
2    Bob   22  52800.0
3  David   28  57200.0
4   Mary   35  77000.0

=========== AFTER RENAMING COLUMNS ==========
  employee_name  age  monthly_salary
0          John   25         55000.0
1         Alice   30         71500.0
2           Bob   22         52800.0
3         David   28         57200.0
4          Mary   35         77000.0
"""

# Handling Missing Data : isnull(),fillna(),dropna()
"""
import pandas as pd
import numpy as np

data = {
    "name": ["John", "Alice", None, "Bob"],
    "age": [28, None, 35, 40],
    "salary": [50000, 62000, None, 70000]
}

df = pd.DataFrame(data)
print(df,"\n")

#isnull() – Check for Missing Values
print(df.isnull())
print(df.isnull().sum())

#fillna() – Replace Missing Values

#1: Replace with a constant value
df_filled = df.fillna("Not Available")
print(df_filled,"\n")

#2. Replace missing ages with mean age
df["age"] = df["age"].fillna(df["age"].mean())
print(df)

#3. Replace missing salary with 0
df["salary"] = df["salary"].fillna(0)
print(df,"\n")

#dropna() – Remove Rows with Missing Values

#Remove rows containing any NaN
df_drop_any = df.dropna()
print(df_drop_any,"\n")

#Remove rows where all values are NaN
df_drop_all = df.dropna(how='all')
print(df_drop_all,"\n")


#Remove rows where specific columns are NaN
df_drop_age = df.dropna(subset=["age"])
print(df_drop_age,"\n")

============================================
     name   age   salary
0   John  28.0  50000.0
1  Alice   NaN  62000.0
2   None  35.0      NaN
3    Bob  40.0  70000.0 

    name    age  salary
0  False  False   False
1  False   True   False
2   True  False    True
3  False  False   False
name      1
age       1
salary    1
dtype: int64
            name            age         salary
0           John           28.0        50000.0
1          Alice  Not Available        62000.0
2  Not Available           35.0  Not Available
3            Bob           40.0        70000.0 

    name        age   salary
0   John  28.000000  50000.0
1  Alice  34.333333  62000.0
2   None  35.000000      NaN
3    Bob  40.000000  70000.0
    name        age   salary
0   John  28.000000  50000.0
1  Alice  34.333333  62000.0
2   None  35.000000      0.0
3    Bob  40.000000  70000.0 

    name        age   salary
0   John  28.000000  50000.0
1  Alice  34.333333  62000.0
3    Bob  40.000000  70000.0 

    name        age   salary
0   John  28.000000  50000.0
1  Alice  34.333333  62000.0
2   None  35.000000      0.0
3    Bob  40.000000  70000.0 

    name        age   salary
0   John  28.000000  50000.0
1  Alice  34.333333  62000.0
2   None  35.000000      0.0
3    Bob  40.000000  70000.0 

"""
# sorting of arrays
