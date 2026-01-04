import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_pribadi import ui

kata_mudah = ["BUKU", "MEJA", "BOLA", "SAPI", "BIRU", 
    "AIR",  "API",  "TAS",  "JAM",  "ROTI", 
    "SUSU", "GIGI", "MATA", "KAKI", "JARI", 
    "BAJU", "TOPI", "IKAN", "AYAM", "OBAT",
    "PENA", "KUE",  "KOPI", "TEH",  "NASI",
    "GULA", "BUAH", "BATU", "KAYU", "DASI"]

kata_normal = ["KURSI", "PAGAR", "RUMAH", "MOBIL", "MOTOR", 
    "HUJAN", "BADAI", "AWAN",  "PASAR", "KELAS", 
    "BOTOL", "GELAS", "PIRING", "SENDOK", "GARPU",
    "JERUK", "SALAK", "MELON", "KASUR", "LAMPU",
    "KIPAS", "EMBER", "SIKAT", "SABUN", "HANDUK",
    "HITAM", "PUTIH", "MERAH", "HIJAU", "UNGU",
    "EMAS",  "INTAN", "KUNCI", "PINTU", "ATAP"]

kata_sulit = ["KOMPUTER", "TELEVISI", "JENDELA",  "LEMARI",    "SELIMUT",
    "PRESIDEN", "INDONESIA", "MATAHARI", "SAMUDRA",   "GUNUNG",
    "KANGURU",  "KELELAWAR", "BENGKEL",  "RESTORAN",  "SEKOLAH",
    "PELANGI",  "SAHABAT",   "KELUARGA", "TETANGGA",  "MAJALAH",
    "MONITOR",  "KEYBOARD",  "INTERNET", "JARINGAN",  "PROGRAM",
    "SEMANGKA", "RAMBUTAN",  "MANGGIS",  "DURIAN",    "ANGGUR",
    "PETUALANG", "KERAJAAN", "PAHLAWAN", "KENDARAAN", "PESAWAT"]

kata_random = kata_mudah + kata_normal + kata_sulit


kata_rahasia = []

def kesulitan(input_kesulitan):
    if input_kesulitan in ["mudah", "m"]:
        kata = random.choice(kata_mudah)
        return list(kata)
    elif input_kesulitan in ["normal", "n"]:
        kata = random.choice(kata_normal)
        return list(kata)
    elif input_kesulitan in ["sulit", "s"]:
        kata = random.choice(kata_sulit)
        return list(kata)
    elif input_kesulitan in ["random", "r"]:
        kata = random.choice(kata_random)
        return list(kata)
    else:
        return None

def tampilkan_kesulitan(input_kesulitan):
    if input_kesulitan in ["mudah", "m"]:
        return "Mudah"
    elif input_kesulitan in ["normal", "n"]:
        return "Normal"
    elif input_kesulitan in ["sulit", "s"]:
        return "Sulit"
    elif input_kesulitan in ["random", "r"]:
        return "Random"
    else:
        return None 

# def sudah_ditebak(input_jwb):
#     if not input_jwb:
#         return None
#     else:
#         return input_jwb[-1]

def pesan(input_jwb, jawaban):
    if not input_jwb:
        print("Belum ada jawaban dikirim")
    else:
        terakhir = input_jwb[-1]
        if (len(terakhir) == 1 and terakhir in jawaban) or (terakhir == jawaban):
            print(f"Huruf/kata {terakhir} ada pada jawaban")
        else:
            print(f"Sayang sekali, huruf/kata {terakhir} salah!")


def tampilan_jawaban(kata_jawaban):
    global kata_rahasia
    if not kata_rahasia:
        for huruf in kata_jawaban:
            huruf = "_"
            kata_rahasia.append(huruf)
    return None
    

def mencocokkan_huruf(jawaban_user, jawaban):
    global kata_rahasia
    if jawaban_user in jawaban:
        for i, huruf in enumerate(jawaban):
            if jawaban_user == huruf:
                kata_rahasia[i] = jawaban_user
        return kata_rahasia
    if len(jawaban_user) > 1:
        for index, huruf_asli in enumerate (jawaban):
            if huruf_asli in jawaban_user:
                kata_rahasia[index] = huruf_asli
        return kata_rahasia
    return None

def menu():
    print(f"""
{'='*50}
{'SELAMAT DATANG DI PERMAINAN THE HANGING GAME'.center(50)}
{'='*50}
""")

# if __name__ == "__main":
#     level = input("pilih kesulitan(m,n,s,r) : ")
#     lvl = kesulitan(level)

# count = 5
# while count > 0:
#     tampilan_jawaban(lvl)
#     print("Kata : ")
#     for i in kata_rahasia:
#         print(i, end="")
    
#     print("\nINFO")
#     print(f"Kesempatan \t: {count}")
#     jwb_usr = input("Masukkan Huruf jawaban : ").upper()

#     mencocokkan_1huruf(jwb_usr, lvl)
#     count -= 1

# if count == 0:
#     print(f"anda kalah, jawabannya {lvl}")

# sdh = ["j"]
# jwb = "API"
# pesan(sdh, jwb)




