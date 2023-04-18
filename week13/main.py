import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="pass"
)

# Open a cursor to perform database operations
cur = conn.cursor()

value = 2
cur.execute("SELECT * from transactions where customer_id = %s;", (value,))
# Execute a query
# cur.execute("SELECT id, amount, type_op FROM transactions;")

# Fetch the results
# results = cur.fetchall()
results = cur.fetchone()

print(results)

# Close the cursor and connection
cur.close()
conn.close()
