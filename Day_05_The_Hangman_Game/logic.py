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

def tampilan_jawaban(kata_jawaban):
    global kata_rahasia
    if not kata_rahasia:
        for huruf in kata_jawaban:
            huruf = "_"
            kata_rahasia.append(huruf)
    return None
    

def mencocokkan_huruf(jawaban_user, jawaban):
    list(jawaban_user)
    while jawaban_user in jawaban:
        for i, huruf in enumerate(jawaban):
            if jawaban_user == huruf:
                return i
        if len(jawaban_user) > 1:
            for j, hrf_jwban in enumerate(jawaban_user):
                if hrf_jwban in jawaban:
                    return j
    return None

def reveal(indek_sama, jawaban_user):
    while indek_sama is not None:
        kata_rahasia[indek_sama] = jawaban_user
    return

level = input("pilih kesulitan(m,n,s,r) : ")
lvl = kesulitan(level)

count = 5
while count > 0:
    tampilan_jawaban(lvl)
    print("Kata : ")
    for i in kata_rahasia:
        print(i, end="")
    
    print("\nINFO")
    print(f"Kesempatan \t: {count}")
    jwb_usr = input("Masukkan Huruf jawaban : ").upper()

    hsl = mencocokkan_huruf(jwb_usr, lvl)
    reveal(hsl, jwb_usr)
    count -= 1

if count == 0:
    print(f"anda kalah, jawabannya {lvl}")






