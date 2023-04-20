import psycopg2

# Establish a connection to the database
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="pass"
)
query_get_transactions = "SELECT id, amount, type_op FROM transactions;"
query_create_user = "INSERT INTO customers(first_name, last_name) VALUES (%s, %s) RETURNING id;"
query_add_transaction = "INSERT INTO transactions (type_op, amount, customer_id) VALUES (%s, %s, %s);"
# Open a cursor to perform database operations
cur = connection.cursor()


# Execute a query
# cur.execute(query_get_transactions)
try:
    cur.execute(query_create_user, ('ro', 'sa'))

    customer_id = cur.fetchone()[0]  # (id, )

    # cur.execute(query_add_transaction, ('DBT', 100_000, customer_id))
    transactions = [
        ('DBT', 500_000, customer_id),
        ('DBT', 600_000, customer_id),

    ]
    cur.executemany(
        query_add_transaction,
        transactions
    )
    connection.commit()
    print(customer_id)
except psycopg2.DatabaseError:
    connection.rollback()
finally:
    cur.close()
    connection.close()

# Fetch the results
# results = cur.fetchall() list[tuple]
# results = cur.fetchone()

# print(results)

# Close the cursor and connection

