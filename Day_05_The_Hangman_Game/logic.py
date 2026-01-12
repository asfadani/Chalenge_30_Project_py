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

def pesan(input_jwb, jawaban):
    if not input_jwb:
        print("Belum ada jawaban dikirim")
    else:
        terakhir = input_jwb[-1]
        if (len(terakhir) == 1 and terakhir in jawaban) or (terakhir == jawaban):
            print(f"Huruf {terakhir} ada pada jawaban")
        elif len(terakhir) > 1 and len(terakhir) != len(jawaban):
            print(f"Masukkan hanya 1 huruf atau satu kata!")
        elif len(terakhir) == len(jawaban):
            print(f"Kata {terakhir} salah!")
        else:
            print(f"Sayang sekali, huruf/kata {terakhir} salah!")

def tampilan_jawaban(kata_jawaban):
    a = list(kata_jawaban)
    hasil = []
    for huruf in a:
        huruf = "_"
        hasil.append(huruf)
    if not a:
        return None
    return hasil

def mencocokkan_huruf(jawaban_user, jawaban, kata_rahasia):
    if jawaban_user in jawaban:
        for i, huruf in enumerate(jawaban):
            if jawaban_user == huruf:
                kata_rahasia[i] = jawaban_user
        return kata_rahasia
    if len(jawaban_user) == len(jawaban):
        jwbn = list(jawaban_user)
        if jwbn == jawaban :
            for index, huruf_asli in enumerate (jawaban):
                kata_rahasia[index] = huruf_asli
            return kata_rahasia
    return None

if __name__ == "__main__":
    jawaban = "AYAM"
    kunci = ["A", "Y", "A", "M"]
    rahasia = ["_", "_", "_", "_"]

    print(rahasia)
    print("++++")
    mencocokkan_huruf(jawaban, kunci, rahasia)
    print(rahasia)




