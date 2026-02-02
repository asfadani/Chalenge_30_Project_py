import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    set up library
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import sqlite3
    import requests
    import os
    return os, plt, sqlite3


@app.cell
def _(mo):
    mo.md(r"""
    koneksi ke database
    """)
    return


@app.cell
def _(os, sqlite3):
    folder = os.path.dirname(os.path.abspath(__file__))
    file_database =os.path.join(folder, 'marketing_warehouse.db')

    try:
        koneksi=sqlite3.connect(file_database)
        kursor = koneksi.cursor()
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return (kursor,)


@app.cell
def _(mo):
    mo.md(r"""
    cek/menampilkan data pada database
    """)
    return


@app.cell
def _(kursor):
    kursor.execute("SELECT * FROM prospek")
    baris_data = kursor.fetchall()
    for data in baris_data:
        print(data[:5])
    return


@app.cell
def _(mo):
    mo.md(r"""
    mengambil dan mengelompokkan negara serta jumlahnya
    """)
    return


@app.cell
def _(kursor):
    value_count = kursor.execute("SELECT nat, count(*) as jumlah FROM prospek GROUP BY nat")
    hasil = kursor.fetchall()
    print(hasil)

    return (hasil,)


@app.cell
def _(mo):
    mo.md(r"""
    mengambil nilai negara, dan jumlah
    """)
    return


@app.cell
def _(hasil):
    negara =[]
    jumlah = []

    for i in hasil:
        for j, k in enumerate(i):
            if j == 0:
                negara.append(k)
            elif j == 1:
                jumlah.append(k)

    print(negara)
    print(jumlah)
    return jumlah, negara


@app.cell
def _(mo):
    mo.md(r"""
    menentukan sumbu x dan sumbu y
    """)
    return


@app.cell
def _(jumlah, negara):
    sumbu_x = negara
    sumbu_y = jumlah
    return sumbu_x, sumbu_y


@app.cell
def _(mo):
    mo.md(r"""
    visualisasi
    """)
    return


@app.cell
def _(plt, sumbu_x, sumbu_y):
    plt.bar(sumbu_x, sumbu_y, color=['#B8001F', '#041562', '#F5F5F5'], edgecolor='black')
    plt.title('Distribusi Konsumen Tiap Negara (USA, AU, FR)')
    plt.xlabel('Negara')
    plt.ylabel('Jumlah')

    plt.show()
    return


if __name__ == "__main__":
    app.run()
