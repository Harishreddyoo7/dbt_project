import argparse
import pandas as pd
import psycopg2

def export_to_csv(dbname, user, password, host, port, table_name):
    # Connect to the database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    # SQL query to select all columns from the specified table
    sql_query = 'SELECT * FROM staging."{}";'.format(table_name)

    # Read data into a DataFrame
    df = pd.read_sql(sql_query, conn)

    # Close the database connection
    conn.close()

    # Define the file path for the CSV file
    csv_file_path = '{}.csv'.format(table_name)

    # Write DataFrame to CSV file
    df.to_csv(csv_file_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export data from PostgreSQL to CSV file.')
    parser.add_argument('--dbname', required=True, help='Database name')
    parser.add_argument('--user', required=True, help='Database user')
    parser.add_argument('--password', required=True, help='Database password')
    parser.add_argument('--host', required=True, help='Database host')
    parser.add_argument('--port', required=True, help='Database port')
    parser.add_argument('--table1', required=True, help='First table name')
    parser.add_argument('--table2', required=True, help='Second table name')

    args = parser.parse_args()

    # Call export_to_csv function for the first table
    export_to_csv(args.dbname, args.user, args.password, args.host, args.port, args.table1)

    # Call export_to_csv function for the second table
    export_to_csv(args.dbname, args.user, args.password, args.host, args.port, args.table2)
