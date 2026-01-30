import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _():
    import requests
    import json
    import pandas as pd
    import sys
    import os
    return os, pd, requests


@app.cell
def _(requests):
    url = "https://randomuser.me/api/?results=100&seed=coba2"

    print("---Mengirim pesan ke API")

    respon = requests.get(url)

    print(respon)
    if respon.status_code == 200:
        print("Data berhasil diterima")
    return (respon,)


@app.cell
def _(respon):
    data = respon.json()
    print(data.keys())
    return (data,)


@app.cell
def _(data, pd):
    df = pd.DataFrame(data['results'])
    print(df)
    return (df,)


@app.cell
def _(df):
    df['nama'] = df['name'].apply(lambda x: x['first'])
    df['usia'] = df['dob'].apply(lambda x: x['age'])
    print(df.info())
    return


@app.cell
def _(df):
    analisis = df[['gender', 'nat', 'nama', 'usia']]
    print(analisis)
    return (analisis,)


@app.cell
def _(analisis):
    filter_perempuan = analisis[analisis['gender'].str.contains('female')]
    print(filter_perempuan)
    return (filter_perempuan,)


@app.cell
def _(filter_perempuan):
    filter_negara = filter_perempuan[filter_perempuan['nat'].isin(['US', 'AU', 'GB'])]
    print(filter_negara)
    return (filter_negara,)


@app.cell
def _(filter_negara):
    filter_usia = filter_negara[filter_negara['usia']<30]
    print(filter_usia)
    return (filter_usia,)


@app.cell
def _(filter_usia):
    data_final = filter_usia.sort_index(ascending=True).reset_index(drop=True)
    print(data_final)
    return (data_final,)


@app.cell
def _(data_final, os):
    try:
        folder = os.path.dirname(os.path.abspath(__file__))
        alamat =os.path.join(folder, 'Marketing_Target_List.csv') 
        simpan = data_final.to_csv(alamat, index=False)
        print(f"\nData CSV berhasil disimpan di {alamat}!")
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return


if __name__ == "__main__":
    app.run()
