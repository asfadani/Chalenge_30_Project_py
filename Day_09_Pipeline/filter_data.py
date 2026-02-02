import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _():
    import requests
    import pandas as pd 
    import os
    return os, pd, requests


@app.cell
def _(requests):
    url = "https://randomuser.me/api/?results=1000&seed=day9"
    print("Mengirim pesan ke server")

    try:
        response = requests.get(url)
        if response.status_code == 200 :
            print("Data berhasil di terima")
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return (response,)


@app.cell
def _(response):
    data = response.json()
    print(data.keys())
    return (data,)


@app.cell
def _(data, pd):
    df = pd.DataFrame(data['results'])
    print(df.info())

    print(df.head())
    return (df,)


@app.cell
def _(df):
    df['nama'] = df['name'].apply(lambda x: x['first'])
    df['umur'] = df['dob'].apply(lambda x: x['age'])

    print(df.info())
    return


@app.cell
def _(df):
    analisis = df[df['nat'].isin(['US', 'AU', 'FR'])]

    print(analisis[['nama', 'nat']].head())
    print(analisis.info())

    return (analisis,)


@app.cell
def _(analisis):
    data_final = analisis[['nama', 'umur', 'gender', 'nat', 'email']].sort_index(ascending=True).reset_index(drop=True)
    print(data_final.head())
    print(data_final.info())
    return (data_final,)


@app.cell
def _(data_final, os):
    try:
        folder = os.path.dirname(os.path.abspath(__file__))
        alamat =os.path.join(folder, 'marketing_warehouse.csv') 
        simpan = data_final.to_csv(alamat, index=False)
        print(f"\nData CSV berhasil disimpan di {alamat}!")
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return


if __name__ == "__main__":
    app.run()
