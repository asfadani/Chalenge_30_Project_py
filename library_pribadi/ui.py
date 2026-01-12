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