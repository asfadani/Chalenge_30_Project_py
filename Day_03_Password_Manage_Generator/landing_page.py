import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

admin = {}

def tambah_admin():
    global admin
    usn = input("Masukkan username : ")
    pw = input("Masukkan password : ")
    admin['Username'] = usn
    admin['Password'] = pw
    print("Akun telah terdaftar")



while True:
    print(f"{"SELAMAT DATANG DI PROGRAM PASSWORD MANAGER".center(50)}\n{"="*50}")

    if not admin:
        print(f"{"Belum ada admin terdaftar, daftar admin".center(50)}")
        tambah_admin()
        ui.kembali()
        continue
    else:
            try:
                print(f"{"Login".center(50)}")
                usn = input("Masukkan username : ")
                pw = input("Masukkan password : ")

                if usn == admin['Username'] and pw == admin["Password"]:
                    ui.clear_screen()
                    print("menuju menu utama")
                    break
                else:
                    print("Username atau Password salah")
                    ui.kembali
                    ui.clear_screen
                    continue
            except:
                print("input tidak sesuai")
                ui.kembali()
                ui.clear_screen()
                continue