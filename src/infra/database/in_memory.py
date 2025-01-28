import sqlite3
from typing import Dict

class Database:
    def query(self, query: str, args: tuple = ()) -> list[Dict]:
        raise NotImplementedError("Must implement query")

    def query_row(self, query: str, args: tuple = ()) -> Dict:
        raise NotImplementedError("Must implement query_row")
    

class InMemoryDatabase(Database):
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
        self._create_rows()
    
    def _create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    role TEXT,
                    password TEXT
                )
            """)

    def _create_rows(self):
        with self.connection:
            self.connection.executemany(
                "INSERT INTO users (username, role, password) VALUES (?, ?, ?)",
                    [
                        ("user", "user", "L0XuwPOdS5U"),
                        ("admin", "admin", "JKSipm0YH"),
                    ]
                )
        
    def query(self, query: str, args: tuple = ()) -> list[Dict]:
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        if rows:
            return [dict(row) for row in rows]
        return []
    
    def query_row(self, query: str, args: tuple = ()) -> Dict: 
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        row = cursor.fetchone()
        if row:
            return dict(row)
        return {}

    