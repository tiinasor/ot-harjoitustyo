from database_connection import get_database_connection
def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    """)

    connection.commit()

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users;")

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)

    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
