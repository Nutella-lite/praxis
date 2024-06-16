import tkinter as tk
from tkinter import ttk
import sqlite3

app = tk.Tk()
app.geometry('300x300')
app.title('Система управления заказами')



conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS orders
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL, 
quantity INTEGER, 
price REAL)
            ''')
conn.commit()

cur.execute("INSERT INTO orders (name, quantity, price) VALUES (?, ?, ?)",
            ('item1', 1, 10.0))
conn.commit()
cur.execute('SELECT * FROM orders')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()
