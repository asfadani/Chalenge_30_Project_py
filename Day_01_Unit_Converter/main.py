satuan_suhu = [["Celcius", "C"], ["Fahrenheit", "F"], ["Kelvin", "K"], ["Reamur", "R"]]

def menu_utama():
    print(f"""
    {"Selamat Datang di Program Konversi Suhu".center(47)}
    {"="*47}
    {"Suhu dalam 0 drajat Celcius".center(47)}
    Fahrenheit = 32     Kelvin = 273    Reamur = 0
    {"="*47}
    {"Suhu yang akan di konversi".center(47)}
    {"(Celcius/Fahrenheit/Kelvin/Reamur)".center(47)}
    """)
    while True:
        try:
            pilihan = input("Akan mengkonversi apa : ")
        except:
            ("Pilihan konversi anda tidak sesuai")
            continue
        return pilihan

def input_suhu():
    while True:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi : "))
        except:
            print(f"Suhu yang anda masukan tidak sesua, suhu : {suhu}/nSuhu harus berupa angka")
            continue
        return suhu

class Konversi():
    def celcius(suhu):    
        reamur = (4/5) * suhu
        kelvin = suhu + 273
        fahrenheit = ((9/5) * suhu) + 32
        return(f"{"Hasil Konversi Suhu".center(47)}\n{"="*47}\nKelvin\t: {kelvin}\nReamur\t: {reamur}\nFahrenheit\t: {fahrenheit}")
    def reamur(suhu):
        celcius = (5/4) * suhu
        kelvin = ((5/4) * suhu) + 273
        fahrenheit = ((9/4) * suhu) + 32
        return(f"{"Hasil Konversi Suhu".center(47)}\n{"="*47}\nKelvin\t: {kelvin}\nCelcius\t: {celcius}\nFahrenheit\t: {fahrenheit}")
    def kelvin(suhu):
        celcius = suhu - 273
        reamur = 4/5 *(suhu - 273)
        fahrenheit = (9/5 * (suhu - 273)) + 32
        return(f"{"Hasil Konversi Suhu".center(47)}\n{"="*47}\nReamur\t: {reamur}\nCelcius\t: {celcius}\nFahrenheit\t: {fahrenheit}")
    def fahrenheit(suhu):
        celcius = 5/9 * (suhu - 32)
        reamur = 4/9 * (suhu - 32)
        kelvin =(5/9 * (suhu - 32)) + 273
        return(f"{"Hasil Konversi Suhu".center(47)}\n{"="*47}\nReamur\t: {reamur}\nCelcius\t: {celcius}\nKelvin\t: {kelvin}")




def konversikan(pilihan):
    if pilihan is not satuan_suhu:
        return "Pilihan anda tidak sesuai"
    elif pilihan == [satuan for satuan in satuan_suhu[0]]:
        Konversi.celcius()




menu_utama()