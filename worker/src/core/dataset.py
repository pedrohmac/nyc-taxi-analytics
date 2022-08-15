from src.services.postgres import create_connection
from src.services.parser import extract_json, extract_vendor, extract_payment
from src.models import queries
from psycopg2.extras import execute_values



def load_trips(table, columns, json_path):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(queries.create_statement.format(table, table, columns))
    print(f'table created: {table}')

    json_data = extract_json(json_path)
    print('data extracted')

    query_handler = queries.insert_statement.format(table, json_data[0])
    execute_values(cursor, query_handler, json_data[1])
    print(f'insert successful: {table}')
    return connection.commit()


def load_vendor(table, columns, filepath):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(queries.create_statement.format(table, table, columns))
    print(f'table created: {table}')

    csv_data = extract_vendor(filepath)
    print('data extracted')

    query_handler = queries.insert_statement.format(table, csv_data[0])
    execute_values(cursor, query_handler, csv_data[1])
    print(f'insert successful: {table}')
    return connection.commit()


def update_payment(table, filepath):
    connection = create_connection()
    cursor = connection.cursor()

    payment_lookup = extract_payment(filepath)
 

    for i in payment_lookup:
        query_handler = queries.update_statement.format(table, i[1], i[0])
        cursor.execute(query_handler)
    print(f'update successful')

    return connection.commit()