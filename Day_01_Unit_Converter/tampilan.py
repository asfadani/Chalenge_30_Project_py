import os
import sys

def menu_utama():
    print(f"""
    {"="*47}
    {"====Selamat Datang di Program Konversi Suhu====".center(47)}
    {"="*47}
    {"Titik beku dan titik didih masing masing suhu".center(47)}

    {"Fahrenheit \t= 32 - 212\tKelvin \t= 273 - 373"}
    {"Reamur \t= 0  - 80\tCelcius = 0   - 100"}  
    {"="*47}
    {"Suhu yang akan di konversi".center(47)}
    {"(Celcius/Fahrenheit/Kelvin/Reamur)".center(47)}
    """)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def kembali():
    input("\nTekan ENTER untuk kembali ke menu utama...")