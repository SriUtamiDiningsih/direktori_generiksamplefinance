from src.function import load_data, filter_special_price, match_rs_klinik
from src.function_export import generate_summary, export_to_excel

try:
    sample_sheet_id = '4.1. Generik - Sample'
    finance_sheet_id = '4.2. Generik - Finance'
    sample_worksheet_name = 'Data Sampel'
    layanan_worksheet_name = 'Data Layanan'
    finance_worksheet_name = 'Variasi Pricing_Satuan'

    # Load data
    sample_data, layanan_data, finance_data = load_data('key.json', sample_sheet_id, finance_sheet_id, sample_worksheet_name, layanan_worksheet_name, finance_worksheet_name)

    # Filter for 'Special Price' being FALSE
    special_price_false = filter_special_price(sample_data)

    # Match 'rs/klinik' in "variasi special pricing paket"
    matching_rs_klinik = match_rs_klinik(special_price_false, finance_data)

    # Generate summary
    summary_df = generate_summary(special_price_false, matching_rs_klinik)

    # Filter for specific months (July, August, September, October)
    selected_months = [7, 8, 9, 10]
    summary_df = summary_df[summary_df['Tanggal Pickup'].dt.month.isin(selected_months)]

    # Export to Excel
    export_to_excel(summary_df, 'summary_Paket_satuan.xlsx')

    print("Summary data successfully exported to summary_Paket_satuan.xlsx")
except Exception as e:
    print(f"An error occurred: {e}")
