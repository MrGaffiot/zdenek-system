import sqlite3

class DatabaseHandler:
    def __init__(self, path: str="src\data\\test.db"):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    def read(self, query: str="SELECT * FROM *"):
        return self.cursor.execute(query).fetchall()

    def insert(self, data: str, where: str):
        return self.cursor.execute("INSERT INTO ? VALUES ?", (data, where))
