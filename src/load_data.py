import pandas as pd
import os

def load_spotify_data(filename="spotify-2023.csv"):
    # Caminho absoluto da raiz do projeto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "raw", filename)

    df = pd.read_csv(
        file_path,
        sep=",",
        encoding="latin-1",
        low_memory=False
    )
    return df

if __name__ == "__main__":
    print("Lendo CSV...")

    df = load_spotify_data()

    print(df.head())
    print("Linhas:", len(df))
    print("Funcionou!")
