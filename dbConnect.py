import sqlite3

def connect_and_creating_table():
    conn = sqlite3.connect("users.db")

    c = conn.cursor()

    c.execute("CREATE TABLE members(tag text, hasPremium text)")