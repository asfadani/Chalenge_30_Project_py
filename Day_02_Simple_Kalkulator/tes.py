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

list = []

def itung(operasi):
    while "*" in operasi or "/" in operasi:
        for i,item in enumerate(operasi):
            if item == "*" or item == "/":
                ops = item
                angka_kiri = operasi[i - 1]
                angka_kanan = operasi[i + 1]
                hasil = op[ops](angka_kiri, angka_kanan)
                # print(f"hasilnya sementara : {hasil}")
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
                # print(f"hasilnya sementara : {hasil}")
                operasi.pop(i + 1)
                operasi.pop(i)
                operasi[i - 1] = hasil
                break
    return operasi[0]

def menu():
    print("=== KALKULATOR PEMDAS (Input '=' untuk hasil) ===")

menu()
ada_hasil = False
while True:
    try:
        angka = int(input("masukkan angka : "))
        list.append(angka)
        status = " ".join(map(str, list))
        print(f"\nInput saat ini:  {status} ")
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")

    opra = input("masukkan opra : ")
    if opra in op:
        list.append(opra)
        continue
    elif opra == "=":
        ui.clear_screen()
        hasil = itung(list)
        print(f"Hasil dari perhitungan {status}")
        print(f"Hasilnya = {hasil}")
        ada_hasil = True
        break
    elif opra == "/" and angka == 0:
        print("Tidak bisa dibagi dengan 0")
        continue

    if ada_hasil == True:
        sudah = ui.lagi()
        list.clear()
        ui.clear_screen()
        if sudah == True:
            print("terimakasih sudah bermain!".upper())
            break