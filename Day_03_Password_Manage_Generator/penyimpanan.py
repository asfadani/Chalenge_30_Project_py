import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_csv =os.path.join(folder, "data_akun.csv") 



# load csv
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
        fieldnames = ["Aplikasi", "Akun", "Password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

data_akun = load_csv()

if __name__ == "__main__":
    from setup import PasswordGenerator
    from setup import ui

    tempalte_akunmanager = {
        'Akun' : "akun",
        'Password' : "password"
    }

    def kecuali():
        kecuali = input("Kecualikan Upper/Lower/Number/Char (y/n)? ").lower()
        if kecuali != "y":
            return
        else:
            print("\nTEKAN ENTER UNTUK MELEWATI")
            kapital = input("huruf kapital(upper) yang ingin dikecualikan : ").upper()
            lower = input("Huruf non-kapital(lower) yang ingin dikecualikan : ").lower()
            angka = input("Angka yang ingin dikecualikan : ")
            schar = input("Karakter spesial yang ingin dikecualikan : ")
            return kapital, lower, angka, schar    
    def generator(panjang, kapital, lower, angka, schar):
        pwg = PasswordGenerator()
        pwg.maxlen = panjang
        pwg.minlen = 1
        pwg.excludeuchars = kapital
        pwg.excludelchars = lower
        pwg.excludenumbers = angka
        pwg.excludeschars = schar
        password = pwg.generate()
        return password
    
    def tampilkan_daftar():
        print(f"{'Aplikasi':<15} {'Akun':<20} {'Password':<15} \n{'='*50}")
        if len(data_akun) == 0:
            print("Tidak ada data terdaftar")
        else:
            for key in data_akun:
                aplikasi = key["Aplikasi"]
                akun = key["Akun"]
                password = key["Password"]
                # Akun = data_akun[key]['Akun']
                # Password = data_akun[key]['Password']
                print(f"{aplikasi:<15} {akun:<20} {password:<15}")

    def generator_password():
        while True:
            try:
                aplikasi = input("Masukkan nama aplikasi : ")
                akunnya = input("Masukkan alamat akun : ")
                panjang = int(input("Panjang password : "))
                hasil_kecuali = kecuali()
                if hasil_kecuali:
                    pw = generator(panjang, *hasil_kecuali)
                else:
                    pw = generator(panjang, "", "", "", "")
                print(f"Password generated : {pw}")
            except Exception as e:
                print(f"\nTerjadi error: {e}")
                print(f"Tipe error: {type(e)}")
                print("Silakan ulangi input data.\n")
                continue
                
            # akun_data = {
            #     'Akun' : akunnya,
            #     'Password' : pw
            # }   
            
            count = 1
            key_aplikasi = aplikasi
            while key_aplikasi in data_akun:
                key_aplikasi = f"{aplikasi}_{count}"
                count += 1
            if key_aplikasi != aplikasi:
                print(f"Info: Nama '{aplikasi}' sudah ada. Disimpan sebagai '{key_aplikasi}'")
            # data_akun.append({key_aplikasi: akun_data})
            data_akun.append({"Aplikasi": key_aplikasi, "Akun":akunnya, "Password": pw })
            save_csv(data_akun)
            print("Data telah terdaftar")
            # for key, value in daftar.items():
            #     print("Data telah terdaftar")
            #     print(f"{key} \t: {value}")

            sudah = input("\nTambah daftar lagi (y/n)? ").lower()
            if sudah != "y":
                break
    # read
    while True:
        print("""
        1. lihat daftar
        2. tambah daftar
        3. keluar
        """)
        pilihan = input("apa yang diinginkan : ")
        if pilihan == "1":
            tampilkan_daftar()
            ui.kembali()
            ui.clear_screen()
        elif pilihan == "2":
            generator_password()
        elif pilihan == "3":
            break
        else:
            print("pilihan tidak sesuai")
            continue        

