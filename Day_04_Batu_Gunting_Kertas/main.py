import logic
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

pilihan = "batu", "gunting", "kertas"

def menu():
    print(f"""
{"-"*50}
{"Selamat Datang di Program Game Sederhana".center(50)}
{"batu gunting kertas".center(50).upper()}
{"-"*50}
    """)

while True:
    menu()
    com = logic.pilihan_com(pilihan)
    ada_hasil = False
    try:
        inputan = input("Silahkan pilih (Batu/Gunting/Kertas) : ").lower()
        orang = logic.pilihan_orang(inputan)
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
        ui.kembali()
        ui.clear_screen()
        continue
    hasil_menang  = logic.orang_menang(com, orang)
    hasil_kalah = logic.orang_kalah(com, orang)
    seri = logic.hasil_seri(com, orang)
    ui.clear_screen()
    logic.hasil(com, orang, hasil_menang, hasil_kalah, seri)
    ada_hasil = True

    if ada_hasil == True:
        sudah = ui.lagi()
        ui.clear_screen()
        if sudah == True:
            print("terimakasih sudah bermain!".upper())
            break
