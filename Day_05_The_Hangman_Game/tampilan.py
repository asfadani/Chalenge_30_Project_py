TAHAPAN_GAMBAR = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
    ,
    """
      +---+
      |   |
      O   |
          |
          |
   _ /|\ _|
    =========
    """
]

def ambil_gambar(sisa_nyawa):
    index = 5 - sisa_nyawa

    if index > 6 : index = 6
    if index < 0 : index = 0

    return TAHAPAN_GAMBAR[index]


def menu():
    print(f"""
{'='*50}
{'SELAMAT DATANG DI PERMAINAN THE HANGING GAME'.center(50)}
{'='*50}
""")


if __name__ == "__main__":
    print(ambil_gambar(3))