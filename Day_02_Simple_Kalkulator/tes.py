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



def itung(operasi):
    while "*" in operasi or "/" in operasi:
        for i,item in enumerate(operasi):
            if item == "*" or item == "/":
                ops = item
                angka_kiri = operasi[i - 1]
                angka_kanan = operasi[i + 1]
                try:
                    hasil = op[ops](angka_kiri, angka_kanan)
                except ZeroDivisionError:
                    print("Tidak bisa membagi dengan 0")
                    return "Error"
                operasi.pop(i + 1)
                operasi.pop(i)
                operasi[i - 1] = hasil
                break
    while "+" in operasi or "-" in operasi:
        for i,item in enumerate(operasi):
            if item == "+" or item == "-":
                ops = item
                angka_kiri = operasi[i - 1]
                angka_kanan = operasi[i + 1]
                hasil = op[ops](angka_kiri, angka_kanan)
                operasi.pop(i + 1)
                operasi.pop(i)
                operasi[i - 1] = hasil
                break
    return operasi[0]

def menu():
    print("=== KALKULATOR PEMDAS (Input '=' untuk hasil) ===")


while True:
    ui.clear_screen()
    menu()
    list_inputan = []
    ada_hasil = False
    try:
        angka = float(input("masukkan angka : "))
        list_inputan.append(angka)
    except ValueError:
        print("Harus angka!")
        ui.kembali()
        continue

    while True:
        status = " ".join(map(str, list_inputan))
        print(f"\nInput saat ini:  {status} ")
        opra = input("masukkan operator : ")
        if opra == "=":
            ui.clear_screen()
            hasil = itung(list_inputan)
            print(f"Hasil dari perhitungan {status}")
            print(f"Hasilnya = {hasil}")
            break
        elif opra not in op:
            print("Operator tidak tersedia, silahkan masukkan (+, -, *, /)")
            continue
        list_inputan.append(opra)


        while True:
            try:
                angka_selanjutnya = float(input("masukkan angka : "))
                list_inputan.append(angka_selanjutnya)
                break
            except ValueError:
                print("Harus angka!")

    if  ui.lagi():
        print("terimakasih sudah bermain!".upper())
        break
