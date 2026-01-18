import numpy as np
import pandas as pd

def clean_spotify_data(df):

    # porcentagens
    cols_pct = [
        'danceability_%', 'valence_%', 'energy_%', 'acousticness_%',
        'instrumentalness_%', 'liveness_%', 'speechiness_%'
    ]
    df[cols_pct] = df[cols_pct].astype(float)

    # categorias
    df['key'] = df['key'].astype('category')
    df['mode'] = df['mode'].astype('category')

    # datas
    df['released_date'] = pd.to_datetime(
        df['released_year'].astype(str) + '-' +
        df['released_month'].astype(str) + '-' +
        df['released_day'].astype(str),
        errors='coerce'
    )
    df = df.drop(columns=['released_year','released_month','released_day'])

    # numéricos
    numeric_cols = [
        'streams','in_spotify_charts','in_apple_charts',
        'in_deezer_charts','in_shazam_charts'
    ]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # missing key
    df['key'] = df['key'].cat.add_categories('Unknown').fillna('Unknown')

    # limpar valores inválidos
    df.replace({'': np.nan, ' ': np.nan, 'nan': np.nan, 'NULL': np.nan, 'NA': np.nan}, inplace=True)

    df.dropna(subset=['in_shazam_charts'], inplace=True)
    df.dropna(subset=['streams'], inplace=True)

    df['released_year_real'] = df['released_date'].dt.year

    return df
