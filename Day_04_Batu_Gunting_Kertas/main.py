import logic
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

pilihan = "batu", "gunting", "kertas"

def menu():
    print(f"""
{'-'*50}
{'Selamat Datang di Program Game Sederhana'.center(50)}
{'batu gunting kertas'.center(50).upper()}
{'-'*50}
    """)

def game():
    while True:
        ui.clear_screen()
        menu()
        com = logic.pilihan_com()
        ada_hasil = False
        while True:
            inputan = input("Silahkan pilih (Batu/Gunting/Kertas) : ").lower()
            orang = logic.pilihan_orang(inputan)

            if orang is not None:
                break
            print("Input tidak valid")

        hasil = logic.orang_menang(com, orang)

        ui.clear_screen()
        print(f"""
    {'='*40}
    Komputer memilih : {com.upper()}
    Anda memilih : {orang.upper()}
    {'='*40}
        """)
        
        if hasil == "seri":
            print(f"{'HASIL SERI'.center(40)}")
        elif hasil == "menang":
            print(f"{'SELAMAT ANDA MENANG'.center(40)}")
        else:
            print(f"{'YAH ANDA KALAH'.center(40)}")
        ada_hasil = True

        if ada_hasil == True:
            sudah = ui.selesai()
            ui.clear_screen()
            if sudah == True:
                print("terimakasih sudah bermain!".upper())
                break

if __name__ == "__main__":
    game()
