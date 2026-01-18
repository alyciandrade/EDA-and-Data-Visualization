import os
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import pandas as pd

def formatar_bilhoes(x, pos):
    if x >= 1e9:
        return f"{x/1e9:.1f} bi"
    elif x >= 1e6:
        return f"{x/1e6:.1f} mi"
    elif x >= 1e3:
        return f"{x/1e3:.1f} mil"
    return f"{x:.0f}"

def save_fig(fig_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fig_dir = os.path.join(base_dir, "reports", "figures")
    os.makedirs(fig_dir, exist_ok=True)
    plt.savefig(os.path.join(fig_dir, fig_name), dpi=300)
    plt.close()

def boxplot_streams(df):
    plt.figure(figsize=(10,5))
    plt.boxplot(
        df['streams'].dropna(),
        vert=False,
        medianprops=dict(color='red', linewidth=2)
    )
    plt.title("Boxplot — Streams")
    plt.gca().xaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))
    save_fig("boxplot_streams.png")

def top_n_artists(df, n=10):
    top = df['artist(s)_name'].value_counts().head(n)

    plt.figure(figsize=(20,10))
    sns.barplot(x=top.index, y=top.values)
    plt.title(f"Top {n} artistas mais ouvidos")
    plt.xticks(rotation=45)
    save_fig("top_artistas.png")

def top_n_tracks(df, n=10):
    top = df[['track_name','streams']].sort_values(by='streams', ascending=False).head(n)

    plt.figure(figsize=(20,10))
    sns.barplot(x=top['track_name'], y=top['streams'])
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))
    plt.title(f"Top {n} músicas mais ouvidas")
    save_fig("top_musicas.png")
