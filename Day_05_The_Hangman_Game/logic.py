import random

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

def jawaban(input_jawaban, kata_jawaban):
    jawab = list(input_jawaban)
    if len(jawab) > len(kata_jawaban):
        return None
    for i, huruf in enumerate(kata_jawaban):
        

print("test")
print(kesulitan("m"))
