import pandas as pd
from datetime import datetime

def count_id_sample_true(df, months):
    return df[(df['Special Price'] == 'TRUE') &
               df['Tanggal Pickup'].notna() &
               df['RS/Klinik'].notna() &
               df['Tanggal Pickup'].dt.month.isin(months)]['ID Sample'].nunique()

def count_tabel_harga_special(df, months):
    df['Tanggal Mulai'] = pd.to_datetime(df['Tanggal Mulai'], format='%d/%m/%Y')
    return df[df['Tanggal Mulai'].notna() &
               df['Tanggal Mulai'].dt.month.isin(months)]['Tabel Harga Special'].nunique()
