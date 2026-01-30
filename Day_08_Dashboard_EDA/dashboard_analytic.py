import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    load library
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    return os, pd, plt


@app.cell
def _(mo):
    mo.md(r"""
    load file csv
    """)
    return


@app.cell
def _(os):
    folder_ini = os.path.dirname(os.path.abspath(__file__))
    file_csv =os.path.join(folder_ini, '..', 'Day_07_Leads', 'Marketing_Target_List_2.csv') 
    file_csv = os.path.abspath(file_csv)

    print(f"Mencari file di :{file_csv}")
    return (file_csv,)


@app.cell
def _(mo):
    mo.md(r"""
    read csv
    """)
    return


@app.cell
def _(file_csv, pd):
    try:
        df = pd.read_csv(file_csv)
        print(df.head())
    except Exception as e:
        print(f"Terjadi error: {e}")
        print(f"Tipe error: {type(e)}")
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    frekuensi jumlah setiap negara
    """)
    return


@app.cell
def _(df):
    frekuensi_negara = df['nat'].value_counts()
    print(frekuensi_negara)
    return (frekuensi_negara,)


@app.cell
def _(mo):
    mo.md(r"""
    menyimpan pada sumbu x dan y
    """)
    return


@app.cell
def _(frekuensi_negara):
    sumbu_x = frekuensi_negara.index
    sumbu_y = frekuensi_negara.values

    print(f"sumbu x :{sumbu_x}\nsumbu y :{sumbu_y}")

    return sumbu_x, sumbu_y


@app.cell
def _(mo):
    mo.md(r"""
    visualisasi chart (BAR)
    """)
    return


@app.cell
def _(plt, sumbu_x, sumbu_y):
    plt.bar(sumbu_x, sumbu_y, color=['red', 'blue', 'green'])
    plt.title("Jumlah Target Market Berdasar Negara")
    plt.xlabel("Negara asal")
    plt.ylabel("Jumlah orang")

    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    menyimpan data sebaran usia
    """)
    return


@app.cell
def _(df):
    sebaran_usia = df['usia']
    print(sebaran_usia)
    return (sebaran_usia,)


@app.cell
def _(mo):
    mo.md(r"""
    visualisasi data sebaran usia (histogram)
    """)
    return


@app.cell
def _(plt, sebaran_usia):
    from matplotlib.pylab import axis
    plt.hist(sebaran_usia, bins=10, color='teal', edgecolor='#F5F5DC')
    plt.title('Distribusi Usia Target Market (Gen Z & Millennial)')
    plt.xlabel('Usia')
    plt.ylabel('Jumlah orang')
    plt.grid(axis='y', alpha=0.5)

    plt.show()
    return


if __name__ == "__main__":
    app.run()
