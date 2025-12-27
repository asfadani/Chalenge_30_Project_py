import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def kembali():
    input("\nTekan ENTER untuk kembali...")

def lagi():
    sudah = input("\nTambah daftar lagi (y/n)? ").lower()
    if sudah != "y":
        return