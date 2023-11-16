from src.function import load_data, filter_special_price
from src.function_export import generate_summary, export_to_excel
import pandas as pd

try:
    sheet_id = '4.1. Generik - Sample'
    worksheet_name = 'Data Sampel'

    # Load data
    data = load_data('key.json', sheet_id, worksheet_name)

    # Convert 'Tanggal Pickup' to datetime
    data['Tanggal Pickup'] = pd.to_datetime(data['Tanggal Pickup'], format='%d/%m/%Y')

    # Filter for 'Special Price' being True
    special_price_true = filter_special_price(data)

    # Filter for specific months (July, August, September, October)
    selected_months = [7, 8, 9, 10]
    data_filtered = special_price_true[special_price_true['Tanggal Pickup'].dt.month.isin(selected_months)]

    # Generate summary
    summary = generate_summary(special_price_true)

    # Export to Excel
    export_to_excel(summary, 'summary_jumlah_paket.xlsx')

    print("Summary data successfully exported to summary_jumlah_paket.xlsx")
except Exception as e:
    print(f"An error occurred: {e}")
