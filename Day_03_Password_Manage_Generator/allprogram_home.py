from setup import PasswordGenerator
from setup import ui

tempalte_akunmanager = {
    'Akun' : "akun",
    'Password' : "password"
}

daftar = {}


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
    pwg.excludeuchars = kapital
    pwg.excludelchars = lower
    pwg.excludenumbers = angka
    pwg.excludeschars = schar
    password = pwg.generate()
    return password
    

class Fitur():
    @staticmethod
    def tampilkan_daftar():
        print(f"{'Aplikasi':<15} {'Akun':<20} {'Password':<15} \n{'='*50}")
        if not daftar:
            print("Tidak ada data terdaftar")
        else:
            for key in daftar:
                Akun = daftar[key]['Akun']
                Password = daftar[key]['Password']
                print(f"{key:<15} {Akun:<20} {Password:<15}")
        
    @staticmethod
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
                
            akun_data = {
                'Akun' : akunnya,
                'Password' : pw
            }   
            
            count = 1
            key_aplikasi = aplikasi
            while key_aplikasi in daftar:
                key_aplikasi = f"{aplikasi}_{count}"
                count += 1
            if key_aplikasi != aplikasi:
                print(f"Info: Nama '{aplikasi}' sudah ada. Disimpan sebagai '{key_aplikasi}'")
            daftar[key_aplikasi] = akun_data
   
            for key, value in daftar.items():
                print("Data telah terdaftar")
                print(f"{key} \t: {value}")

            sudah = input("\nTambah daftar lagi (y/n)? ").lower()
            if sudah != "y":
                break
    @staticmethod
    def update_delete():
        Fitur.tampilkan_daftar()
        while True:
            tanya_lagi = False
            try:
                ubah = input("\nApa yang ingin anda lakukan (update/delete/back) ? ").lower()
                if ubah in ["delete", "del", "d"]:
                    hapus = input("Masukkan nama aplikasi yang ingin dihapus : ")
                    if hapus in daftar:
                        del daftar[hapus]
                        print(f"\nData aplikasi {hapus} berhasil dihapus")
                        Fitur.tampilkan_daftar()
                        tanya_lagi = True
                    else:
                        print("\nData tidak ditemukan.")
                        continue

                elif ubah in ["update", "up", "u"]:
                    opsi = input("Apa yang ingin diupdate (aplikasi/akun)? ").lower()
                    if opsi == "aplikasi":
                        target = input("Masukkan nama aplikasi lama: ")
                        if target in daftar:
                            baru = input(f"Perbarui aplikasi {target} menjadi : ")
                            data_tersimpan = daftar.pop(target)
                            daftar[baru] = data_tersimpan
                            print(f"\nAplikasi {target} berhasil diupdate menjadi {baru}")
                            Fitur.tampilkan_daftar()
                            tanya_lagi = True
                        else:
                            print(f"\nData aplikasi {baru} tidak ditemukan")
                            continue
                    elif opsi == "akun":
                        app_akun = input("Masukkan nama aplikasi pemilik akun: ")
                        if app_akun in daftar:
                            akun_baru = input(f"Ubah akun {daftar[app_akun]['Akun']} menjadi : ")
                            daftar[app_akun]['Akun'] = akun_baru
                            print("\nAkun berhasil diperbarui")
                            tanya_lagi = True
                        else:
                            print(f"\nData aplikasi {app_akun} tidak ditemukan")

                elif ubah in ["back", "b"]:
                    break
                else:
                    print("\nInput tidak sesuai")
                    continue
            except Exception as e:
                print(f"\nTerjadi error: {e}")
                print(f"Tipe error: {type(e)}")
                continue

            if tanya_lagi == True:
                pilihan = input("\nUpdate/delete data lain(y/n)? ")
                if pilihan != "y":
                    break












