import pandas as pd

def generate_summary(special_price_false, matching_rs_klinik):
    summary = []
    for index, row in special_price_false.iterrows():
        pickup_date = row['Tanggal Pickup']
        matching_rs = matching_rs_klinik[matching_rs_klinik['Nama Instansi'] == row['RS/Klinik']]
        for _, match_row in matching_rs.iterrows():
            start_date = pd.to_datetime(match_row['Tanggal Mulai'], format='%d/%m/%Y')
            end_date = pd.to_datetime(match_row['Tanggal Selesai'], format='%d/%m/%Y')
            if not pd.isnull(start_date) and not pd.isnull(end_date) and start_date <= pickup_date <= end_date:
                summary.append({
                    'ID Sample': row['ID Sample'],
                    'Tanggal Pickup': pickup_date,
                    'RS/Klinik': row['RS/Klinik'],
                    'Tanggal Mulai': match_row['Tanggal Mulai'],
                    'Nama Instansi':match_row['Nama Instansi'],
                    'Tabel Harga': match_row['Tabel Harga']
                })

    return pd.DataFrame(summary)

def export_to_excel(summary_df, output_filename):
    try:
        summary_df.to_excel(output_filename, index=False)
        print(f"Summary data successfully exported to {output_filename}")
    except Exception as e:
        print(f"Error while exporting to Excel: {str(e)}")
