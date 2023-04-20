-- table - customers; id, first_name, last_name
-- table - transactions; id, amount, type_op, date, customer_id

CREATE TABLE customers (
      id SERIAL PRIMARY KEY
    , first_name VARCHAR(30)
    , last_name VARCHAR(50)
);


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY
    , type_op VARCHAR(3)
    , amount NUMERIC
    , date DATE
    , customer_id INT NOT NULL
    , FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
INSERT INTO transactions (type_op, amount, customer_id)
VALUES
    ('DBT', 36600.50, 2),
    ('CRD', 160, 2),
    ('CRD', 10000, 2);
commit;

-- DROP TABLE transactions;

INSERT INTO customers (first_name, last_name)
VALUES ('roman', 'sv');

INSERT INTO customers (first_name, last_name)
VALUES ('bayazid', 'yr');
commit;

rollback;
-- sequence

ALTER TABLE customers
ADD COLUMN region VARCHAR(10);

UPDATE customers
SET region = 'ASTANA'
WHERE id = 2;


DELETE FROM customers
WHERE id = 1;
TRUNCATE TABLE customers;


select
    *
from customers
    left join transactions
        on customers.id = transactions.customer_id;

select * from customers where id = 2;



SELECT
--     *
    id
    , type_op
    , customer_id
    , amount
--     , date

FROM transactions;

