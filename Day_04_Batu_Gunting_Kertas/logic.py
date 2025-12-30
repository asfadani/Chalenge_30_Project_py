import random

pilihan = ["batu", "gunting", "kertas"]
orang = ""



def pilihan_com(pilihan):
    pilihan_com = random.choice(pilihan)
    return pilihan_com
com = pilihan_com

def pilihan_orang(inputan):
    global orang
    while True:
        if inputan in ["batu", "b", "bt"]:
            orang = "batu"
            return orang
        elif inputan in ["guntung", "g", "gtg"]:
            orang = "gunting"
            return orang
        elif inputan in ["kertas", "k", "kts"]:
            orang = "kertas"
            return orang
        else:
            print("Inputan anda tidak ada pada pilihan")
            continue


def orang_menang(com, orang):
    if orang == "gunting" and com == "kertas":
        hasil = "menang"
        return hasil
    elif orang == "kertas" and com == "batu":
        hasil = "menang"
        return hasil
    elif orang == "batu" and com == "gunting":
        hasil = "menang"
        return hasil
hasil_menang = orang_menang(com, orang)

def orang_kalah (com, orang):
    if orang == "batu" and com == "kertas":
        hasil = "kalah"
        return hasil
    elif orang == "gunting" and com == "batu":
        hasil = "kalah"
        return hasil
    elif orang == "kertas" and com == "gunting":
        hasil = "kalah"
        return hasil
    
hasil_kalah = orang_kalah(com, orang)

def hasil_seri(com, orang):
    if com == orang:
        return "seri"
seri = hasil_seri(com, orang)    

def hasil(com, orang, hasil_menang, hasil_kalah, seri):
    if hasil_menang == "menang":
        print(f"{"===============selamat anda menang!===============".upper().center(50)}\nPilihan anda ({orang}), pilihan com ({com})")
    elif hasil_kalah == "kalah":
        print(f"{"=============yah computer lebih jago!=============".upper().center(31)}\nPilihan anda ({orang}), pilihan com ({com})")
    elif seri == "seri":
        print(f"{"=============hasilnya seri, ayo lagi!=============".upper().center(31)}\nPilihan anda ({orang}), pilihan com ({com})")
    ada_hasil = True
    return ada_hasil
    








