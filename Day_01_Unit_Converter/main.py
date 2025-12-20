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


def input_suhu():
    while True:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi : "))
        except:
            clear_screen()
            print(f"Suhu yang anda masukan tidak sesua, suhu : {suhu}/nSuhu harus berupa angka")
            kembali()
            clear_screen()
            continue
        else:
            return suhu

# class Konversi():
def celcius(suhu):    
    reamur = (4/5) * suhu
    kelvin = suhu + 273
    fahrenheit = ((9/5) * suhu) + 32
    hasil = f"{"Hasil Konversi Suhu {suhu} Celcius".center(47)}\n{"="*47}\nKelvin\t\t: {kelvin:.2f}\nReamur\t\t: {reamur:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
    print(hasil)
def reamur(suhu):
    celcius = (5/4) * suhu
    kelvin = ((5/4) * suhu) + 273
    fahrenheit = ((9/4) * suhu) + 32
    hasil = f"{"Hasil Konversi Suhu {suhu}Reamur".center(47)}\n{"="*47}\nKelvin\t\t: {kelvin:.2f}\nCelcius\t\t: {celcius:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
    print(hasil)
def kelvin(suhu):
    celcius = suhu - 273
    reamur = 4/5 *(suhu - 273)
    fahrenheit = (9/5 * (suhu - 273)) + 32
    hasil = f"{"Hasil Konversi Suhu {suhu}Kelvin".center(47)}\n{"="*47}\nReamur\t\t: {reamur:.2f}\nCelcius\t\t: {celcius:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
    print(hasil)
def fahrenheit(suhu):
    celcius = 5/9 * (suhu - 32)
    reamur = 4/9 * (suhu - 32)
    kelvin =(5/9 * (suhu - 32)) + 273
    hasil = f"{"Hasil Konversi Suhu {suhu}Fahrenheit".center(47)}\n{"="*47}\nReamur\t: {reamur:.2f}\nCelcius\t: {celcius:.2f}\nKelvin\t: {kelvin:.2f}"
    print(hasil)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def kembali():
    input("\nTekan ENTER untuk kembali ke menu utama...")


    

while True:
    clear_screen()
    menu_utama()
    try:
        pilihan = input("Akan mengkonversi apa atau (q/quit) : ".center(47)).lower()
    except:
        clear_screen()
        ("Pilihan konversi anda tidak sesuai")
        kembali()
        clear_screen()
        continue
    else:
        if pilihan == "c" or pilihan == "celcius":
            clear_screen()
            print("Suhu yang akan di konversikan Celcius")
            suhu = input_suhu()
            clear_screen()
            celcius(suhu)

            konversi_lagi = input("\nkonversikan lagi (y/n)? ").lower()
            if konversi_lagi != "y":
                clear_screen()
                print("Terimakasih telah menggunakan program konversi suhu")
                break
        elif pilihan == "f" or pilihan == "fahrenheit":
            clear_screen()
            print("Suhu yang akan di konversikan Fahrenheit")
            suhu = input_suhu()
            clear_screen()
            fahrenheit(suhu)

            konversi_lagi = input("\nkonversikan lagi (y/n)? ").lower()
            if konversi_lagi != "y":
                clear_screen()
                print("Terimakasih telah menggunakan program konversi suhu")
                break          
        elif pilihan == "k" or pilihan == "kelvin":
            clear_screen()
            print("Suhu yang akan di konversikan Kelvin")
            suhu = input_suhu()
            clear_screen()
            kelvin(suhu)

            konversi_lagi = input("\nkonversikan lagi (y/n)? ").lower()
            if konversi_lagi != "y":
                clear_screen()
                print("Terimakasih telah menggunakan program konversi suhu")
                break
        elif pilihan == "r" or pilihan == "reamur":
            clear_screen()
            print("Suhu yang akan di konversikan Reamur")
            suhu = input_suhu()
            clear_screen()
            reamur(suhu)

            konversi_lagi = input("\nkonversikan lagi (y/n)? ").lower()
            if konversi_lagi != "y":
                clear_screen()
                print("Terimakasih telah menggunakan program konversi suhu")
                break      
        elif pilihan == "quit" or pilihan == "q":
            clear_screen()
            print("Terimakasih telah menggunakan program konversi suhu")
            break
        else:
            clear_screen()
            print(f"input satuan {pilihan} tidak ada dipilihan")
            kembali()
            clear_screen()
            continue


    
    




