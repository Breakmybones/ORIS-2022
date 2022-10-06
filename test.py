import psycopg2
from congig import host, user, password, db_name

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    db_name=db_name
)
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        db_name=db_name
    )


    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print(f"Server version: {cursor.fetchone()}")
except Exception as _ex:
    print("[INFO} Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('closed')

