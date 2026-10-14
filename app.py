
import sqlite3


def initialize_database():
    """Create a small local database for the CodeQL test."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)"
    )
    connection.execute(
        "INSERT INTO users (username) VALUES (?)",
        ("alice",),
    )
    return connection


def find_user(connection, username):
    """
    Intentionally vulnerable example for CodeQL testing.

    Do not use this query construction in a real application.
    """
    query = (
        "SELECT id, username FROM users "
        f"WHERE username = '{username}'"
    )
    return connection.execute(query).fetchone()


if __name__ == "__main__":
    database = initialize_database()
    print(find_user(database, "alice"))
    database.close()
