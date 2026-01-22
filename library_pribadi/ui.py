import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def kembali():
    input("\nTekan ENTER untuk melannjutkan...")

def selesai():
    sudah = input("\nLagi (y/n)? ").lower()
    if sudah != "y":
        sudah = True
        return sudah
    
def cari_index(dicari, data_list):
    for index, isi in enumerate(data_list):
        for key in isi.items():
            if dicari in key:
                return index

def cari_key(dicari, data_dict):
    for key, value in data_dict.items():
        if value == dicari:
            return key

def ada_tidak(dicari, data):
    for cari in data:
        for key, value in cari.items():
            if value == dicari:
                return True


def menyimpan_file(data):
    import json
    import openpyxl
    import csv
    import pandas as pd
    while True:
        print("format di dukung (json, csv, excel)")
        nama_file = input("Masukkan nama file: ")
        folder = os.path.dirname(os.path.abspath(__file__))
        alamat =os.path.join(folder, nama_file) 
        if "csv" in nama_file:
            simpan = data.to_csv(alamat)
            return simpan
        elif "json" in nama_file:
            simpan = data.to_json(alamat)
            return simpan
        elif "xlsx" in nama_file:
            simpan = data.to_excel(alamat)
            return simpan
        else:
            print("format tidak valid")
            continue


if __name__ == "__main__":
    import requests
    import pandas as pd
    url = "https://api.sampleapis.com/coffee/hot"
    respon = requests.get(url)
    data_kopi = respon.json()
    df = pd.DataFrame(data_kopi)
    data_latte = df.loc[df['title'].str.contains('Latte'), ['title', 'description', 'id']]
    menyimpan_file(data_latte)

"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui
"""

"""
print(f"Terjadi error: {e}")
print(f"Tipe error: {type(e)}")
"""