import logic



while True:
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
        logic.tampilan_jawaban(lvl)
        print(f"Level\t: {logic.tampilkan_kesulitan(level)}")
        print("Kata:")
        for i in kata_rahasia:
            print(i, end="")
        
        print("\n[INFO]")
        print(f"> Sisa Kesempatan \t: {count}")
        print(f">Huruf/Kata yang sudah ditebak : {sudah}")
        logic.pesan(sudah, lvl)
        jwb_usr = input("\nMasukkan huruf/kata jawaban : ").upper()
        sudah.append(jwb_usr)

        logic.mencocokkan_huruf(jwb_usr, lvl)
        count -= 1

    if count == 0 and "-" in kata_rahasia:
        print(f"{'='*50}{'\nSayang sekali anda kalah, jawabannya'.center(50)}\n{lvl}\n{'='*50}")
        break
    if "_" not in kata_rahasia:
        print(f"{'='*50}{'\nSayang sekali anda kalah, jawabannya'.center(50)}\n{lvl}\n{'='*50}")
        break

    if logic.ui.lagi():
        logic.ui.clear_screen()
        print("Terimakasih sudah bermain")
        break