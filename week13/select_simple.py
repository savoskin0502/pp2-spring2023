import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="pass"
)

# Open a cursor to perform database operations
cur = conn.cursor()  #

# Execute a query
# cur.execute("SELECT first_name, last_name FROM customers;")
query_add_user = "INSERT INTO customers(first_name, last_name, region) VALUES(%s, %s, %s) RETURNING id;"
query_get_user = "select * from customers where first_name = %s;"

# Fetch the results
# results = cur.fetchall()  # list[tuple, ...]
cur.execute(query_add_user, ('roma', 's', 'A'))
customer_id = cur.fetchone()[0]

cur.execute(query_get_user, ('alibek',))
print(cur.fetchall())
query_add_transaction = "INSERT INTO transactions(type_op, customer_id, amount) VALUES(%s, %s, %s);"

# cur.execute(query_add_transaction, ('CRD', customer_id, 1000))
customer_transactions = [
    ('CRD', customer_id, 2000),
    ('DBT', customer_id, 5000),
]
cur.executemany(
    query_add_transaction,
    customer_transactions,
)

conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
