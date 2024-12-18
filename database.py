import sqlite3
from flask import g
import bcrypt
from cryptography.fernet import Fernet

DATABASE = 'database/tickets.db'

encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def register(username, password):
    db = get_db()
    cursor = db.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        encrypted_username = cipher.encrypt(username.encode('utf-8'))
        cursor.execute ('insert into UsersInfo (Username, Password) values (?, ?)', (encrypted_username, hashed_password))
        db.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login(username, password):
    db = get_db()
    cursor = db.cursor()

    encrypted_username = cipher.encrypt(username.encode('utf-8'))
    cursor.execute ('select Password from UsersInfo where Username = ?', (encrypted_username,))
    row = cursor.fetchone()

    if row:
        stored_password = row[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return True
        return False

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

def ticket_info(movie_name):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select Total_Tickets from Tickets_Availability where Movie_Name = ?", (movie_name,))
    Availabile_Tickets = cursor.fetchone()
    return Availabile_Tickets[0]

def get_Tickets():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select * from Tickets_Availability")
    Available_Tickets = cursor.fetchall()
    return Available_Tickets