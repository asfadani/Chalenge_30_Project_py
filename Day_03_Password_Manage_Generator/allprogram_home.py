import random
from re import template

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

def generator():
    print("generator")