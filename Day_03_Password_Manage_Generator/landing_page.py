from setup import ui


admin = {}

def tambah_admin():
    global admin
    usn = input("Masukkan username : ")
    pw = input("Masukkan password : ")
    admin['Username'] = usn
    admin['Password'] = pw
    print("Akun telah terdaftar")



while True:
    print(f"{'SELAMAT DATANG DI PROGRAM PASSWORD MANAGER'.center(50)}\n{'='*50}")
    if not admin:
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

            if usn == admin['Username'] and pw == admin['Password']:
                ui.clear_screen()
                import main_program
                main_program.program()
            elif usn == "q" and pw == "q":
                ui.clear_screen()
                print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA PASWORD MANAJEMEN")
                break
            elif usn != admin['Username'] and pw != admin["Password"]:
                print("\nUsername dan password salah")
                ui.kembali()
                ui.clear_screen()
                continue
            elif usn != admin['Username']:
                print("\nUsername salah")
                ui.kembali()
                ui.clear_screen()
                continue
            elif pw != admin["Password"]:
                print("\nPassword salah")
                ui.kembali()
                ui.clear_screen()
                continue
        except Exception as e:
            print(f"\nTerjadi error: {e}")
            print(f"Tipe error: {type(e)}")
            print("Silakan ulangi input data.\n")
            continue