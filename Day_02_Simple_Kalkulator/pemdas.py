import operator
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}



def perhitungan(operasikan):
    while "*" in operasikan or "/" in operasikan:
        for i,item in enumerate(operasikan):
            if item == "*" or item == "/":
                ops = item
                angka_kiri = operasikan[i - 1]
                angka_kanan = operasikan[i + 1]
                hasil = op[ops](angka_kiri, angka_kanan)
                operasikan.pop(i + 1)
                operasikan.pop(i)
                operasikan[i - 1] = hasil
                break
    while "+" in operasikan or "-" in operasikan:
        for i,item in enumerate(operasikan):
            if item == "+" or item == "-":
                ops = item
                angka_kiri = operasikan[i - 1]
                angka_kanan = operasikan[i + 1]
                hasil = op[ops](angka_kiri, angka_kanan)
                operasikan.pop(i + 1)
                operasikan.pop(i)
                operasikan[i - 1] = hasil
                break
    # print(f"Hasil akhir = {operasikan}")
    return operasikan[0]

        

def menu():
    print(f"""
{"="*50}
{"Selamat Datang di Program Kalkulator Sederhana".center(50).upper()}
{"="*50}""")

while True:
    inputan = []
    dapat_hasil = False
    try:
        angka_awal = float(input("Masukkan angka : "))
        inputan.append(angka_awal)
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
        continue
  
    operasi = input("Masukkan operator : ")
    if operasi in op:
        inputan.append(operasi)
        continue
        # if operasi == "/" and angka_selanjutnya == 0:
        #     print("Tidak bisa dibagi 0")
        #     continue
    elif operasi == "=":
        hasil_akhir = perhitungan(inputan)
        print(hasil_akhir)
        # for hasil in operasikan:
        #     print(f"Hasilnya = {hasil}")
        dapat_hasil = True
        break
    else:
        print("Operator tidak tersedia masukkan (+, -, *, /)")
        continue

    # print(perhitungan())
    # for hasil in operasikan:
    #     print(f"Hasilnya adalah {hasil}")
    #     dapat_hasil = True
    #     break

    if dapat_hasil == True:
        pilihan = input("\nHitung lagi (y/n)? ").lower()
        operasikan.clear()
        if pilihan != "y":
            ui.clear_screen()
            print("Terimakasih telah menggunakan program kalkulator sederhana")
            break