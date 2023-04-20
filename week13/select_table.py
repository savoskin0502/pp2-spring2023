import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="pass"
)
# query = "select id, first_name from customers where id = %s;"
query_create_user = "INSERT INTO customers (first_name, last_name) VALUES (%s, %s) RETURNING id;"
query_add_transaction = "INSERT INTO transactions (type_op, customer_id, amount) VALUES (%s, %s, %s);"

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
# cur.execute("select id, first_name from customers;")
# cur.execute(query, (1, ))
cur.execute(query_create_user, ('r', 's'))
customer_id = cur.fetchone()[0]

transactions = [
    ('CRD', customer_id, 2_000_000),
    ('CRD', customer_id, 5_000_000),
]
# cur.execute(query_add_transaction, ('CRD', customer_id, 1_000_000))
cur.executemany(
    query_add_transaction,
    transactions,
)

print(customer_id)


conn.commit()
# Close the cursor and connection
cur.close()
conn.close()
