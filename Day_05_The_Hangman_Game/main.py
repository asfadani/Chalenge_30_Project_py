import logic
import tampilan



while True:
    logic.ui.clear_screen()
    kata_rahasia = []
    sudah = []
    tampilan.menu()
    level = input("\nPilih kesulitan((m)udah, (n)ormal, (s)ulit, (r)andom) : ")
    lvl = logic.kesulitan(level)
    if lvl == None:
        print("Input level kesulitan tidak sesuai")
        continue
    logic.ui.clear_screen()
    count = 5
    while True:
        print(tampilan.ambil_gambar(count))
        kt_rhs = logic.tampilan_jawaban(lvl)
        if not kata_rahasia:
            kata_rahasia.extend(kt_rhs)
        print(f"Level\t: {logic.tampilkan_kesulitan(level)}")
        print(f"Kata\t: {kata_rahasia}")

        
        print("\n[INFO]")
        print(f"> Sisa Nyawa \t\t: {count}")
        print(f"> Huruf/Kata yang sudah ditebak : {sudah}")
        mess = logic.pesan(sudah, lvl)
        jwb_usr = input("\nMasukkan huruf/kata jawaban : ").upper()
        if jwb_usr in kata_rahasia or jwb_usr in sudah or jwb_usr =="":
            print("Anda sudah menjawab pilihan tersebut")
            continue
        sudah.append(jwb_usr)
        
        if len(jwb_usr) == 1 :
            if jwb_usr not in lvl:
                count -= 1
        elif len(jwb_usr) > 1 :
            cek = list(filter(lambda x: x in lvl, jwb_usr))
            if not cek:
                count -= 1

        logic.mencocokkan_huruf(jwb_usr, lvl, kata_rahasia)

        if "_" not in kata_rahasia:
            logic.ui.clear_screen()
            print(f"{'='*50}")
            print(f"{'SELAMAT ANDA MENANG!'.center(50)}")
            print(f"{'-'*50}")
            print(f"\t\t{tampilan.ambil_gambar(count)}")
            print(f"jawabannya\t: {lvl}\nJawaban anda\t: {kata_rahasia}\nTrack jawaban\t: {sudah}\nSisa nyawa\t: {count}")
            print(f"{'='*50}")
            break
        if count == 0 and "_" in kata_rahasia:
            logic.ui.clear_screen()
            print(f"{'='*50}")
            print(f"{'SELAMAT ANDA MENANG!'.center(50)}")
            print(f"{'-'*50}")
            print(f"\t\t{tampilan.ambil_gambar(count)}")
            print(f"jawabannya\t: {lvl}\nJawaban anda\t: {kata_rahasia}\nTrack jawaban\t: {sudah}\nSisa nyawa\t: {count}")
            print(f"{'='*50}")
            break

    if logic.ui.lagi():
        logic.ui.clear_screen()
        print("Terimakasih sudah bermain")
        break