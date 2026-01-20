import csv
import os


folder = os.path.dirname(os.path.abspath(__file__))
file_csv =os.path.join(folder, "data_akun.csv") 




def load_csv():
    if not os.path.exists(file_csv):
        return []
    data = []
    with open(file_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        return data
        
def save_csv(data):
    with open(file_csv, mode='w', newline='') as file:
        fieldnames = ["Aplikasi", "Akun", "Password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

data_akun = load_csv()

if __name__ == "__main__":
   for i in data_akun:
       print(i)