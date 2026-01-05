import logic



while True:
    logic.ui.clear_screen()
    kata_rahasia = []
    sudah = []
    logic.menu()
    level = input("\nPilih kesulitan((m)udah, (n)ormal, (s)ulit, (r)andom) : ")
    lvl = logic.kesulitan(level)
    if lvl == None:
        print("Input levelkesulitan tidak sesuai")
        continue
    logic.ui.clear_screen()
    count = 5
    while count > 0:
        kt_rhs = logic.tampilan_jawaban(lvl)
        if not kata_rahasia:
            kata_rahasia.extend(kt_rhs)
        print(f"Level\t: {logic.tampilkan_kesulitan(level)}")
        print(f"Kata\t: {kata_rahasia}")

        
        print("\n[INFO]")
        print(f"> Sisa Kesempatan \t\t: {count}")
        print(f"> Huruf/Kata yang sudah ditebak : {sudah}")
        logic.pesan(sudah, lvl)
        jwb_usr = input("\nMasukkan huruf/kata jawaban : ").upper()
        if jwb_usr in kata_rahasia or jwb_usr in sudah:
            print("Anda sudah menjawab pilihan tersebut")
            continue
        sudah.append(jwb_usr)
        if "_" not in kata_rahasia:
            logic.ui.clear_screen()
            print(f"{'='*50}\n{'SELAMAT ANDA MENANG!'.center(50)}\n\njawabannya\t: {lvl}\nJawaban anda\t: {kata_rahasia}\nTrack jawaban\t: {sudah}\n{'='*50}")
            break
        logic.mencocokkan_huruf(jwb_usr, lvl, kata_rahasia)
        count -= 1

    if count == 0 and "_" in kata_rahasia:
        logic.ui.clear_screen()
        print(f"{'='*50}\n{'Sayang sekali anda kalah'.center(50)}\n\njawabannya\t: {lvl}\nJawaban anda\t: {kata_rahasia}\nTrack jawaban\t: {sudah}\n{'='*50}")


    if logic.ui.lagi():
        logic.ui.clear_screen()
        print("Terimakasih sudah bermain")
        break