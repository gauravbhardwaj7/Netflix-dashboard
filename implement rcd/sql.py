import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id TEXT PRIMARY KEY,
        type TEXT,
        title TEXT,
        creator TEXT,
        starring TEXT,
        year TEXT,
        rating TEXT,
        time TEXT,
        genres TEXT,
        country TEXT,
        description TEXT
    )
''')

df = pd.read_csv('netflix_full.csv')
movies =[]
for index, row in df.iterrows():
    movies.append((row['id'],row['type'], row['name'], row['creator'], row['starring'], row['year'], row['rating'], row['time'], row['genres'], row['country'], row['describle']))
    

cursor.executemany('INSERT INTO movies (id ,type, title, creator, starring, year, rating, time, genres, country, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', movies)

conn.commit()
conn.close()
