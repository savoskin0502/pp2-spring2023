import psycopg2
# python-dotenv
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="pass"
)
query_create_user = "INSERT INTO customers (first_name, last_name) VALUES (%s, %s) RETURNING id;"
query_add_transaction = "INSERT INTO transactions (type_op, amount, customer_id)  VALUES (%s, %s, %s);"

cursor = connection.cursor()


cursor.execute(query_create_user, ("roma", "sv"))
customer_id = cursor.fetchone()[0]

# cursor.execute(query_add_transaction, ('CRD', 5000, customer_id))
rows = [
    ('CRD', 5000, customer_id),
    ('CRD', 15_000, customer_id),
]
cursor.executemany(query_add_transaction, rows)

connection.commit()  # or revert/reset

print(customer_id)

cursor.close()
connection.close()
# add new customer
# add transactions to customer
