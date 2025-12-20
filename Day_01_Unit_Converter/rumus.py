import tampilan

def input_suhu():
    while True:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi : "))
        except:
            tampilan.clear_screen()
            print(f"Suhu yang anda masukan tidak sesua, suhu : {suhu}/nSuhu harus berupa angka")
            tampilan.kembali()
            tampilan.clear_screen()
            continue
        else:
            return suhu
class Konversikan():
    def celcius(suhu):    
        reamur = (4/5) * suhu
        kelvin = suhu + 273
        fahrenheit = ((9/5) * suhu) + 32
        hasil = f"{f"Hasil Konversi Suhu {suhu} Celcius".center(47)}\n{"="*47}\nKelvin\t\t: {kelvin:.2f}\nReamur\t\t: {reamur:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
        print(hasil)
    def reamur(suhu):
        celcius = (5/4) * suhu
        kelvin = ((5/4) * suhu) + 273
        fahrenheit = ((9/4) * suhu) + 32
        hasil = f"{f"Hasil Konversi Suhu {suhu} Reamur".center(47)}\n{"="*47}\nKelvin\t\t: {kelvin:.2f}\nCelcius\t\t: {celcius:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
        print(hasil)
    def kelvin(suhu):
        celcius = suhu - 273
        reamur = 4/5 *(suhu - 273)
        fahrenheit = (9/5 * (suhu - 273)) + 32
        hasil = f"{f"Hasil Konversi Suhu {suhu} Kelvin".center(47)}\n{"="*47}\nReamur\t\t: {reamur:.2f}\nCelcius\t\t: {celcius:.2f}\nFahrenheit\t: {fahrenheit:.2f}"
        print(hasil)
    def fahrenheit(suhu):
        celcius = 5/9 * (suhu - 32)
        reamur = 4/9 * (suhu - 32)
        kelvin =(5/9 * (suhu - 32)) + 273
        hasil = f"{f"Hasil Konversi Suhu {suhu} Fahrenheit".center(47)}\n{"="*47}\nReamur\t: {reamur:.2f}\nCelcius\t: {celcius:.2f}\nKelvin\t: {kelvin:.2f}"
        print(hasil)
