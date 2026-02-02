import sqlite3
import pandas as pd
import os


folder = os.path.dirname(os.path.abspath(__file__))
file_csv =os.path.join(folder, 'marketing_warehouse.csv')
df = pd.read_csv(file_csv)
print(df.head())


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

# for i, row in df.iterrows():
#     sql = "INSERT INTO prospek (nama, umur, gender, nat, email) VALUES (?,?,?,?,?)"
#     kursor.execute(sql, (row['nama'], row['umur'], row['gender'], row['nat'], row['email']))

# kursor.execute("DELETE FROM prospek")
# kursor.execute("DELETE FROM sqlite_sequence WHERE name='prospek'")

koneksi.commit()
print("\nMenampilkan data dari database")
kursor.execute("SELECT * FROM prospek")
baris_data = kursor.fetchall()
for data in baris_data:
    print(data[:5])

kursor.close()