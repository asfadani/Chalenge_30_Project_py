from setup import PasswordGenerator
from setup import ui
from setup import penyimpanan


data_akun = penyimpanan.load_csv()

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
    pwg.minlen = panjang
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
        if len(data_akun) == 0:
            print("Tidak ada data terdaftar")
        else:
            for key in data_akun:
                aplikasi = key["Aplikasi"]
                akun = key["Akun"]
                password = key["Password"]

                print(f"{aplikasi:<15} {akun:<20} {password:<15}")
        
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
            
            count = 1
            key_aplikasi = aplikasi
            while ui.ada_tidak(key_aplikasi, data_akun):
                key_aplikasi = f"{aplikasi}_{count}"
                count += 1
            data_akun.append({"Aplikasi": key_aplikasi, "Akun":akunnya, "Password": pw })
            penyimpanan.save_csv(data_akun)
            print("Data telah terdaftar")

            if ui.selesai():
                break

    @staticmethod
    def update_delete():
        Fitur.tampilkan_daftar()
        while True:
            tanya_lagi = False
            try:
                ubah = input("\nApa yang ingin anda lakukan (update/delete/back) ? ").lower()
                if ubah in ["delete", "del", "d"]:
                    try:
                        HAPUS = input("\nMasukkan nama aplikasi yang akan dihapus: ")
                        index = ui.cari_index(HAPUS, data_akun)
                        del data_akun[index]
                        penyimpanan.save_csv(data_akun)
                        print(f"Data {HAPUS} berhasil terhapus")
                    except Exception as e:
                        print(f"\nTerjadi error: {e}")
                        print(f"Tipe error: {type(e)}")
                        continue
                elif ubah in ["update", "up", "u"]:
                    try:
                        pilih = int(input("\nData ke berapa yang akan dirubah: "))
                        index = pilih - 1
                        opsi = input("masukkan data yang ingin diubah: ")
                        key = ui.cari_key(opsi, data_akun[index])
                        baru = input("Masukkan data baru: ")
                        data_akun[index][key] = baru
                        penyimpanan.save_csv(data_akun)
                        print(f"Data {opsi} berhasil dirubah menjadi, {baru}")
                    except Exception as e:
                        print(f"\nTerjadi error: {e}")
                        print(f"Tipe error: {type(e)}")
                        continue
                elif ubah in ["back", "b"]:
                    break
                else:
                    print("\nInput tidak sesuai")
                    continue
            except Exception as e:
                print(f"\nTerjadi error: {e}")
                print(f"Tipe error: {type(e)}")
                continue

            if ui.selesai():
                break












