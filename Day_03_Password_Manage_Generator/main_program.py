from setup import ui
import allprogram_home

def menu():
    print(f"""
    {'SELAMAT DATANG DI PROGRAM PASSWORD MANAGER'.center(50)}
    {'='*50}
    1. Lihat daftar akun dan password
    2. Generaor password
    3. Update / delete
    4. Keluar
    """)
def program():
    while True:
        ui.clear_screen()
        menu()
        try:
            pilihan = input("Apa yang anda inginkan (1/2/3/4)? ")
        except Exception as e:
            print(f"Terjadi error: {e}")
            print(f"Tipe error: {type(e)}")
            ui.kembali()
            ui.clear_screen()
            continue
        else:
            if pilihan == "1":
                ui.clear_screen()
                allprogram_home.Fitur.tampilkan_daftar()
                ui.kembali()
                ui.clear_screen()
                continue
            elif pilihan == "2":
                ui.clear_screen()
                print(f"{'-'*50}\n{'Generator Password'.center(50)}\n{'-'*50}")
                allprogram_home.Fitur.generator_password()
            elif pilihan == "3":
                ui.clear_screen()
                print(f"{'-'*50}\n{'Manajemen Password'.center(50)}\n{'-'*50}\n")           
                allprogram_home.Fitur.update_delete()
            elif pilihan == "4":
                ui.clear_screen()
                print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA PASWORD MANAJEMEN")
                exit()
                # return
            else:
                print("Input pilihan tidak sesuai. Harapan masukan angka 1/2/3/4 !")
                ui.kembali()
                ui.clear_screen()
                continue

