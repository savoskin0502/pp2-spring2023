### functions
___

Function is a pre-written set of instructions that performs a specific task.  
Functions are used to encapsulate logic and calculations that can be 
reused in different parts of an application or database

Functions can be stored in the database and can be called from other functions, 
SQL queries, or even from other applications.  

To create a function in PostgreSQL, you can use the CREATE FUNCTION statement, 
which allows you to specify the function name, input parameters, 
return type, and the code to be executed.

Here's an example of a simple function that adds two numbers:
```postgresql
-- create or replace function
CREATE FUNCTION add_numbers(num1 integer, num2 integer)
RETURNS integer AS
-- RETURN table (first_name, last_name)
$$
declare
    var integer;
BEGIN
  RETURN num1 + num2;
END;
$$
LANGUAGE plpgsql;
-- drop function add_numbers;
```

### procedures
___

Procedure is a pre-written set of instructions that performs a specific task, similar to a function  
The main difference between a procedure and a function is that a procedure doesn't return a value,
whereas a function always returns a value.  
They are typically used for tasks that don't require returning a value,
such as updating a table or sending an email.  

To create a procedure in PostgreSQL, you can use the CREATE PROCEDURE statement,
which allows you to specify the procedure name, input parameters, 
and the code to be executed.  

```postgresql
CREATE PROCEDURE update_customer_status(customer_id integer, status text)
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE customers SET status = status WHERE id = customer_id;
END;
$$;

```

[//]: # (cur.execute&#40;"CALL update_customer_status&#40;%s, %s&#41;", &#40;1, 'inactive'&#41;&#41;)

[//]: # (cur.execute&#40;"CALL add_numbers&#40;%s, %s&#41;, &#40;1, 2&#41;&#41;)
cur.callproc("%s %s", (1, 2))

class A:
    @property
    def fullname():
        return self.first_name + self.last_name 

map(function, iterable)
map(lambda x: x**2, [1, 2, 3, 4]) => [1, 4, 9, 16]



A() => __new__ ==> __init__

[//]: # (cur.execute&#40;"CALL update_customer_status&#40;$1, $2&#41;", &#40;1, 'inactive'&#41;&#41;)


### call function

```python

# first method
# Call the function
cur.callproc("add_numbers", [1, 2])

# Get the result
result = cur.fetchone()[0]

# Print the result
print(result)


# second method
# Call the function using a SQL statement
cur.execute("SELECT add_numbers(%s, %s)", (1, 2))

# Get the result
result = cur.fetchone()[0]

# Print the result
print(result)

```


### call procedure
```python
# Call the procedure
cur.callproc("your_procedure_name", [input_parameter_1, input_parameter_2, ...])

# Call the procedure using a SQL statement
cur.execute("CALL your_procedure_name(%s, %s, ...)", (input_parameter_1, input_parameter_2, ...))

```