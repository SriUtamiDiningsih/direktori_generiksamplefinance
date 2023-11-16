import pandas as pd

def generate_summary(data):
    return data.groupby('RS/Klinik')['ID Sample'].count().reset_index()

def export_to_excel(summary, output_filename):
    try:
        summary.to_excel(output_filename, index=False)
        print(f"Summary data successfully exported to {output_filename}")
    except Exception as e:
        print(f"Error while exporting to Excel: {str(e)}")
