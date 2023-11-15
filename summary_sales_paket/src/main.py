import gspread
import pandas as pd
from src.functions import count_id_sample_true, count_tabel_harga_special

try:
    # Autentikasi dan akses "spreadsheet generik sample"
    sheet_service = gspread.service_account(filename='key.json')
    sample_worksheet = sheet_service.open('4.1. Generik - Sample')
    sheet_ds = sample_worksheet.worksheet('Data Sampel')
    sample_data = pd.DataFrame(sheet_ds.get_all_records())
    sample_data['Tanggal Pickup'] = pd.to_datetime(sample_data['Tanggal Pickup'], format='%d/%m/%Y')

    # Autentikasi dan akses "spreadsheet generik finance"
    finance_worksheet = sheet_service.open('4.2. Generik - Finance')
    sheet_variasi = finance_worksheet.worksheet('Variasi Special Pricing_Paket')
    finance_data = pd.DataFrame(sheet_variasi.get_all_records())

    # Tentukan bulan-bulan yang diinginkan
    selected_months = [7, 8, 9, 10]

    # Hitung jumlah 'id sample' dengan 'special price' TRUE dan jumlah 'tabel harga special' untuk bulan-bulan tertentu
    id_sample_count = count_id_sample_true(sample_data, selected_months)
    tabel_harga_special_count = count_tabel_harga_special(finance_data, selected_months)

    # Hitung hasil akhir
    result = id_sample_count * tabel_harga_special_count

    # Export ke Excel
    result_df = pd.DataFrame({
        'Data Sample Paket': [id_sample_count],
        'Tabel Harga Special': [tabel_harga_special_count],
        'Result': [result]
    })
    result_df.to_excel('summary_sales_paket.xlsx', index=False)

    print("Summary data successfully exported to summary_sales_paket.xlsx")
except Exception as e:
    print(f"An error occurred: {e}")
