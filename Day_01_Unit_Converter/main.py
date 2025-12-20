import tampilan
import rumus



while True:
    tampilan.clear_screen()
    tampilan.menu_utama()
    try:
        print("".center(47))
        pilihan = input("Akan mengkonversi apa atau (q/quit) : ").lower()
    except Exception as e:
        tampilan.clear_screen()
        print(f"Terjadi kesalahan {e}")
        tampilan.kembali()
        tampilan.clear_screen()
        continue
    else:
        if pilihan == "quit" or pilihan == "q":
            tampilan.clear_screen()
            print("Terimakasih telah menggunakan program konversi suhu")
            break

        pilihan_sesuai = False

        if pilihan == "c" or pilihan == "celcius":
            tampilan.clear_screen()
            print("Suhu yang akan di konversikan Celcius")
            suhu = rumus.input_suhu()
            tampilan.clear_screen()
            rumus.Konversikan.celcius(suhu)
            pilihan_sesuai = True

        elif pilihan == "f" or pilihan == "fahrenheit":
            tampilan.clear_screen()
            print("Suhu yang akan di konversikan Fahrenheit")
            suhu = rumus.input_suhu()
            tampilan.clear_screen()
            rumus.Konversikan.fahrenheit(suhu)
            pilihan_sesuai = True

        elif pilihan == "k" or pilihan == "kelvin":
            tampilan.clear_screen()
            print("Suhu yang akan di konversikan Kelvin")
            suhu = rumus.input_suhu()
            tampilan.clear_screen()
            rumus.Konversikan.kelvin(suhu)
            pilihan_sesuai = True

        elif pilihan == "r" or pilihan == "reamur":
            tampilan.clear_screen()
            print("Suhu yang akan di konversikan Reamur")
            suhu = rumus.input_suhu()
            tampilan.clear_screen()
            rumus.Konversikan.reamur(suhu)
            pilihan_sesuai = True

        else:
            tampilan.clear_screen()
            print(f"input satuan {pilihan} tidak ada dipilihan")
            tampilan.kembali()
            tampilan.clear_screen()
            continue

        if pilihan_sesuai :
            konversi_lagi = input("\nkonversikan lagi (y/n)? ").lower()
            if konversi_lagi != "y":
                tampilan.clear_screen()
                print("Terimakasih telah menggunakan program konversi suhu")
                break  
    
    




