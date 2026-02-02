import sqlite3
import pandas as pd
import os


folder = os.path.dirname(os.path.abspath(__file__))
file_database =os.path.join(folder, 'marketing_warehouse.db')

try:
    koneksi = sqlite3.connect(file_database)
    kursor = koneksi.cursor()
except Exception as e:
    print(f"Terjadi error: {e}")
    print(f"Tipe error: {type(e)}")




kursor.execute('''
    CREATE TABLE IF NOT EXISTS prospek (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        umur INTEGER,  
        gender TEXT,
        nat TEXT,
        email TEXT
    )
''')

print("Database dan tabel berhasil dibuat")




koneksi.commit()
kursor.close()