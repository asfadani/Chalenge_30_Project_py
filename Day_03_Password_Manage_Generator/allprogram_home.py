import random
from re import template
from password_generator import PasswordGenerator
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

tempalte_akunmanager = {
    'Akun' : "akun",
    'Password' : "password"
}

daftar = {}

def tampilkan_daftar():
    print(f"{"Aplikasi":<15} {"Akun":<15} {"Password":<15} \n{"="*50}")
    if not daftar:
        print("Tidak ada data terdaftar")
    else:
        for key in daftar:
            Akun = daftar[key]['Akun']
            Password = daftar[key]['Password']

        print(f"{key:<15} {Akun:<15} {Password:<15}")

def kecuali():
    kecuali = input("Kecualikan Upper/Lower/Number/Char (y/n)?").lower()
    if kecuali != "y":
        return
    else:
        print("TEKAN ENTER UNTUK MELEWATI")
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
    
def generator_password():
    while True:
        akun = dict.fromkeys(tempalte_akunmanager.keys())
        try:
            aplikasi = input("Masukkan nama aplikasi : ")
            akunnya = input("Masukkan alamat akun")
            panjangnya = int(input("Panjang password : "))
            kecualikan = kecuali()
        except Exception as e:
            print(f"Terjadi error: {e}")
            print(f"Tipe error: {type(e)}")
        
        akun['Akun'] = akunnya
        pw = generator(panjangnya, kecualikan)
        akun['Password'] = pw

        count = 0
        if aplikasi is not daftar:
            daftar.update({aplikasi:akun})
        else:
            aplikasi = f"{aplikasi}{count}"
            daftar.update({aplikasi:akun})
            count += 1
   
        for key, value in daftar.items():
            print("Data telah terdaftar")
            print(f"{key} \t: {value}")

        sudah = input("\nTambah daftar lagi (y/n)? ").lower()
        if sudah != "y":
            break

def update_delete():
    tampilkan_daftar()
    while True:
        try:
            ubah = input("Apa yang ingin anda lakukan (update/delete) ? ").lower()
            if ubah == ("delete" or "del" or "d"):
                hapus = input("Masukkan kata kunci(aplikasi/akun) yang ingin dihapus : ")
            elif ubah == ("update" or "up" or "u"):
                perbarui = input("Masukkan kata kunci(aplikasi/akun) yang ingin diupdate : ")
            else:
                print("Input tidak sesuai")
                continue

        except Exception as e:
            print(f"Terjadi error: {e}")
            print(f"Tipe error: {type(e)}")
        
        tanya_lagi = False

        if hapus or perbarui in daftar.items():
            if hapus:
                del daftar[hapus]
                print(f"Data dengan kata kunci {hapus} berhasil dihapus")
                tampilkan_daftar()
                tanya_lagi = True
            elif perbarui:
                if perbarui in daftar.keys():
                    baru = input(f"Perbarui aplikasi {perbarui} menjadi : ")
                    daftar[perbarui] = baru
                    print(f"Aplikasi {perbarui} berhasil diupdate menjadi {baru}")
                    tampilkan_daftar()
                    tanya_lagi = True
                elif perbarui in daftar.values():
                    baru = input(f"Perbarui akun {perbarui} menjadi : ")
                    daftar[perbarui] = baru
                    print(f"Akun {perbarui} berhasil diupdate menjadi {baru}")
                    tampilkan_daftar()
                    tanya_lagi = True
            else:
                print(f"Data {perbarui} tidak ditemukan di daftar")
                tanya_lagi = True

        if tanya_lagi == True:
            pilihan = input("Update/delete data lain(y/n)? ")
            if pilihan != "y":
                break













