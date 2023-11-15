from src.sample_summary import SampleSummary

# Using the SampleSummary class to generate summary and export to Excel
keyfile = 'key.json'
sample_sheet_id = '4.1. Generik - Sample'
sample_worksheet_name = 'Data Sampel'
output_filename = 'summary_special_paket.xlsx'

sample_summary = SampleSummary(keyfile, sample_sheet_id, sample_worksheet_name)
data = sample_summary.get_data()
summary = sample_summary.generate_summary(data)
sample_summary.export_to_excel(summary, output_filename)
