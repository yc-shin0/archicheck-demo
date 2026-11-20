import sqlite3

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):
        conn = sqlite3.connect("app.db")
        return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
