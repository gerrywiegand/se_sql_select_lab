import sqlite3  # noqa: F401, I001
import pandas as pd  # noqa: F401, I001

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql(
    """
SELECT employeeNumber, lastName
    FROM employees
""",
    conn,
)

print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql(
    """
SELECT lastName, employeeNumber
    FROM employees
""",
    conn,
)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql(
    """
SELECT lastName, employeeNumber AS 'ID'
    FROM employees
""",
    conn,
)
print(df_alias)
# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
    """
SELECT CASE jobTitle
        WHEN 'President' THEN 'Executive'
        WHEN 'VP Sales' THEN 'Executive'
        WHEN 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
        END AS 'role'
    FROM EMPLOYEES
    
    """,
    conn,
)
print(df_executive)
# STEP 6
# Replace None with your code
df_name_length = pd.read_sql(
    """
SELECT length(lastName) AS name_length
    FROM employees
""",
    conn,
)
print(df_name_length)
# STEP 7
# Replace None with your code
df_short_title = pd.read_sql(
    """
SELECT substr(jobTitle, 0,3) AS short_title
    FROM employees
""",
    conn,
)
print(df_short_title)
# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql(
    """
SELECT round(priceEach * quantityOrdered) AS total_price
    FROM orderdetails
    """,
    conn,
).sum()
print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql(
    """
SELECT strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
    FROM orders
""",
    conn,
)
print(df_day_month_year)
conn.close()
