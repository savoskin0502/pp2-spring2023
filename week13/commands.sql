
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  amount DECIMAL NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT into customers (name, email) VALUES ('roma', 'ro_savoskin@kbtu.kz');
commit;


CREATE table customers (
    id SERIAL PRIMARY KEY
    , first_name VARCHAR(30)
    , last_name VARCHAR(30)
);

create table transactions (
    id SERIAL PRIMARY KEY
    , type_op VARCHAR(3)
    , amount NUMERIC
    , customer_id INTEGER NOT NULL
    , FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

ALTER TABLE transactions ADD COLUMN operation_date DATE;

INSERT INTO customers (first_name, last_name) VALUES ('roma', 's');
INSERT INTO customers (first_name, last_name) VALUES ('alibek', 'a');


INSERT INTO transactions (type_op, amount, customer_id)  VALUES ('DBT', 1000, 2);
INSERT INTO transactions (type_op, amount, customer_id)  VALUES ('CRD', 5000, 2);


SELECT * from transactions;

SELECT
    customer_id
    , first_name
    , type_op
    , amount
FROM customers
    inner join transactions on customers.id = transactions.customer_id;

select
    *
from transactions;

SELECT
--     id, first_name, last_name -- *
    *
FROM customers;
WHERE first_name = 'roma';

DELETE FROM customers;
TRUNCATE table customers;
WHERE first_name = 'roma';

UPDATE customers SET last_name = 'b' WHERE first_name = 'alibek';

-- DROP TABLE customers;
-- DROP TABLE transactions;
