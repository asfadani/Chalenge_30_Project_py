import random

pilihan = ["batu", "gunting", "kertas"]

def pilihan_com():
    return random.choice(pilihan)

def pilihan_orang(inputan):
    inputan = inputan.lower()
    if inputan in ["batu", "b", "bt"]:
        return "batu"
    elif inputan in ["gunting", "g", "gtg"]:
        return "gunting"
    elif inputan in ["kertas", "k", "kts"]:
        return "kertas"
    else:
        return None



def orang_menang(com, orang):
    if orang == com:
        return "seri"

    if (orang == "gunting" and com == "kertas") or\
        (orang == "kertas" and com == "batu") or\
        (orang == "batu" and com == "gunting") :
        return "menang"
    return "kalah"   

# def hasil(com, orang, hasil_menang, hasil_kalah, seri):
#     if hasil_menang == "menang":
#         print(f"{'===============selamat anda menang!==============='.upper().center(50)}\nPilihan anda ({orang}), pilihan com ({com})")
#     elif hasil_kalah == "kalah":
#         print(f"{'=============yah computer lebih jago!============='.upper().center(31)}\nPilihan anda ({orang}), pilihan com ({com})")
#     elif seri == "seri":
#         print(f"{'=============hasilnya seri, ayo lagi!============='.upper().center(31)}\nPilihan anda ({orang}), pilihan com ({com})")
#     ada_hasil = True
#     return ada_hasil
    








