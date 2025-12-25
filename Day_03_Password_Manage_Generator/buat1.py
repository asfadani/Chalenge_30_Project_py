data = {
    'akun' : "asfadani",
    'password' : "khusuu219898" 
}

aplikasi = {
    'facebook' : data
}


print(f"{"Aplikasi":<15} {"Akun":<15} {"Password":<15} \n{"="*50}")
if not aplikasi:
    print("tidak ada aplikasi dan password terdaftar")
else:
    for key in aplikasi:
        Akun = aplikasi[key]['akun']
        Password = aplikasi[key]['password']

        print(f"{key:<15} {Akun:<15} {Password:<15}")