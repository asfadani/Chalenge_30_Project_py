import operator
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def menu():
    print(f"""
{"="*50}
{"Selamat Datang di Program Kalkulator Sederhana".center(50).upper()}
{"="*50}""")

dapat_hasil = False

while True:
    menu()
    try:
        angka1 = float(input("Masukkan angka : "))
        angka2 = float(input("Masukkan angka : "))
        operator_input = input("Masukkan operator : ")
    except:
        print("angka inputan harus berupa angka!")
        ui.kembali()
        ui.clear_screen()
        continue 
    if operator_input not in operator:
        print("operator input tidak tersedia")
        ui.kembali()
        ui.clear_screen()
        continue
    elif operator_input == '/':
        if angka2 == 0:
            print("Pembagian tidak bisa dibagi dengan 0")
            ui.kembali()
            ui.clear_screen()
            continue
    ui.clear_screen()
    hasil = operator[operator_input](angka1, angka2)
    print(f"Hasilnya\n{angka1} {operator_input} {angka2} = {hasil}")
    dapat_hasil = True

    if dapat_hasil == True:
        pilihan = input("\nHitung lagi (y/n)? ").lower()
        if pilihan != "y":
            ui.clear_screen()
            print("Terimakasih telah menggunakan program kalkulator sederhana")
            break
    

