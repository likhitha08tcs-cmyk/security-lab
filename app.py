import sqlite3
from flask import Flask, request

app = Flask(__name__)

connection = sqlite3.connect(
    ":memory:",
    check_same_thread=False,
)

connection.execute(
    "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)"
)
connection.execute(
    "INSERT INTO users (username) VALUES (?)",
    ("alice",),
)


@app.route("/user")
def find_user():
    username = request.args.get("username", "")

    # Intentionally vulnerable: security scanning test only.
    query = (
        "SELECT id, username FROM users "
        f"WHERE username = '{username}'"
    )

    result = connection.execute(query).fetchone()
    return str(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
