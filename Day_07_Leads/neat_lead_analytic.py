import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    Import library package yang dibutuhkan
    """)
    return


@app.cell
def _():
    import requests
    import json
    import pandas as pd
    import sys
    import os
    return os, pd, requests


@app.cell
def _(mo):
    mo.md(r"""
    Menagmbil data dari API
    """)
    return


@app.cell
def _(requests):
    url = "https://randomuser.me/api/?results=5000&nat=us,gb,au,fr&seed=coba1"

    print("---Mengirim pesan ke API")

    respon = requests.get(url)

    print(respon)
    if respon.status_code == 200:
        print("Data berhasil diterima")
    return (respon,)


@app.cell
def _(mo):
    mo.md(r"""
    Mengambil info keys pada dictionary API JSON
    """)
    return


@app.cell
def _(respon):
    data = respon.json()
    print(data.keys())
    return (data,)


@app.cell
def _(mo):
    mo.md(r"""
    Membuat data frame pada keys result
    """)
    return


@app.cell
def _(data, pd):
    df = pd.DataFrame(data['results'])
    print(df)
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    Membuat kolom nama dan usia untuk difilter nantinya
    """)
    return


@app.cell
def _(df):
    df['nama'] = df['name'].apply(lambda x: x['first'])
    df['usia'] = df['dob'].apply(lambda x: x['age'])
    print(df.info())
    return


@app.cell
def _(mo):
    mo.md(r"""
    Menyimpan data frame baru dengan kolom yang dibutuhkan ke sebuah variabel
    """)
    return


@app.cell
def _(df):
    analisis = df[['gender', 'nat', 'nama', 'usia']]
    print(analisis)
    return (analisis,)


@app.cell
def _(analisis):
    data_final = analisis[
        (analisis['gender'] == 'female') & 
        (analisis['nat'].isin(['US', 'AU', 'GB'])) & 
        (analisis['usia'] < 30)
    ]
    data_final_sorted = data_final.sort_index(ascending=True).reset_index(drop=True)
    print(data_final_sorted)
    return (data_final,)


@app.cell
def _(mo):
    mo.md(r"""
    Menyimpan hasil analisis menjadi sebuah file CSV
    """)
    return


@app.cell
def _(data_final, os):
    try:
        folder = os.path.dirname(os.path.abspath(__file__))
        alamat =os.path.join(folder, 'Marketing_Target_List_2.csv') 
        simpan = data_final.to_csv(alamat, index=False)
        print(f"\nData CSV berhasil disimpan di {alamat}!")
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return


if __name__ == "__main__":
    app.run()
