import sqlite3
from flask import g

DATABASE = 'database/tickets.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_Cities():
    db = get_db()
    cursor = db.cursor()    
    cursor.execute("select * from Cities")
    rows = cursor.fetchall()
    Cities = [row[0] for row in rows]
    return Cities

def get_Theatres():
    db = get_db()
    cursor = db.cursor() 
    cursor.execute("select * from Theatres")
    rows = cursor.fetchall()
    Theatres = [row[0] for row in rows]
    return Theatres

def get_Movies():
    db = get_db()
    cursor = db.cursor() 
    cursor.execute("select Movie_Name from Tickets_Availability")
    rows = cursor.fetchall()
    Movies = [row[0] for row in rows]
    return Movies

def book(movie_name, tickets):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("update Tickets_Availability set Total_Tickets = Total_Tickets - ? where Movie_Name = ?", (tickets, movie_name))
    db.commit()