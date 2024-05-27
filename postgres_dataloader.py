import psycopg2

# Database connection parameters
dbname = 'test'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    print("Connected to the database successfully!")
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)
    exit(1)

# Define SQL statement to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS hacker_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    state VARCHAR(255),
    occupation VARCHAR(255),
    country VARCHAR(255)
);
"""
try:
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'hacker_data' created successfully!")
except psycopg2.Error as e:
    print("Error creating table:", e)
    conn.rollback()

# Define raw data to be inserted
raw_data = [
    ('Alice', 'New York', 'Hacker', 'USA'),
    ('Bob', 'California', 'Programmer', 'USA'),
    ('Charlie', 'Texas', 'Analyst', 'USA'),
    ('David', 'Florida', 'Engineer', 'USA'),
    ('Emma', 'Washington', 'Developer', 'USA'),
    ('Frank', 'Illinois', 'Designer', 'USA'),
    ('Grace', 'Ohio', 'Manager', 'USA'),
    ('Hannah', 'Georgia', 'Consultant', 'USA'),
    ('Ivan', 'Arizona', 'Architect', 'USA'),
    ('Jessica', 'Michigan', 'Scientist', 'USA'),
    # Add 10 more rows with additional columns here
]

# SQL statement for insertion
sql_insert = "INSERT INTO hacker_data (name, state, occupation, country) VALUES (%s, %s, %s, %s)"

# Insert raw data into the database
try:
    cursor.executemany(sql_insert, raw_data)
    conn.commit()
    print("Data inserted successfully!")
except psycopg2.Error as e:
    print("Error inserting data:", e)
    conn.rollback()

# Close the cursor and connection
cursor.close()
conn.close()
