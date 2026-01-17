# JALANKAN KODE DARI SINI

from setup import ui
import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_csv =os.path.join(folder, "data_admin.csv") 



def load_csv():
    if not os.path.exists(file_csv):
        return []
    data = []
    with open(file_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        return data
        
def save_csv(data):
    with open(file_csv, mode='w', newline='') as file:
        fieldnames = ["Username", "Password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)



data_admin = load_csv()

def tambah_admin():
    usn = input("Masukkan username : ")
    pw = input("Masukkan password : ")
    data_admin.append({"Username": usn, "Password": pw})
    save_csv(data_admin)
    print("Akun telah terdaftar")



while True:
    print(f"{'SELAMAT DATANG DI PROGRAM PASSWORD MANAGER'.center(50)}\n{'='*50}")
    if len(data_admin) == 0:
        print(f"{'Belum ada admin terdaftar, silahkan daftar admin'.center(50)}\n{'(Username dan password tidak boleh hanya huruf q->quit)'.center(50)}")
        tambah_admin()
        ui.kembali()
        ui.clear_screen()
        continue
    else:
        try:
            print(f"{'Login'.center(50)}")
            usn = input("Masukkan username : ")
            pw = input("Masukkan password : ")

            if usn == data_admin[0]["Username"] and pw == data_admin[0]["Password"]:
                ui.clear_screen()
                import main_program
                main_program.program()
            elif usn == "q" and pw == "q":
                ui.clear_screen()
                print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA PASWORD MANAJEMEN")
                break
            elif usn != data_admin[0] and pw != data_admin[0]:
                print("\nUsername dan password salah")
                ui.kembali()
                ui.clear_screen()
                continue
            elif usn != data_admin[0]:
                print("\nUsername salah")
                ui.kembali()
                ui.clear_screen()
                continue
            elif pw != data_admin[0]:
                print("\nPassword salah")
                ui.kembali()
                ui.clear_screen()
                continue
        except Exception as e:
            print(f"\nTerjadi error: {e}")
            print(f"Tipe error: {type(e)}")
            print("Silakan ulangi input data.\n")
            continue