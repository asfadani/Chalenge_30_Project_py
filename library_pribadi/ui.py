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