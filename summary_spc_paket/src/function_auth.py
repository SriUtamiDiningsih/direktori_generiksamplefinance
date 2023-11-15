import gspread
import pandas as pd

def load_data(keyfile, sample_sheet_id, finance_sheet_id, sample_worksheet_name, layanan_worksheet_name, finance_worksheet_name):
    sheet_service = gspread.service_account(filename=keyfile)
    sample_worksheet = sheet_service.open(sample_sheet_id)
    finance_worksheet = sheet_service.open(finance_sheet_id)

    sample_data = pd.DataFrame(sample_worksheet.worksheet(sample_worksheet_name).get_all_records())
    layanan_data = pd.DataFrame(sample_worksheet.worksheet(layanan_worksheet_name).get_all_records())
    finance_data = pd.DataFrame(finance_worksheet.worksheet(finance_worksheet_name).get_all_records())

    sample_data['Tanggal Pickup'] = pd.to_datetime(sample_data['Tanggal Pickup'], format='%d/%m/%Y')

    return sample_data, layanan_data, finance_data

def filter_special_price(sample_data):
    return sample_data[sample_data['Special Price'] == 'TRUE']

def match_rs_klinik(special_price_true, finance_data):
    sample_rs_klinik = special_price_true['RS/Klinik'].unique()
    return finance_data[finance_data['Nama Instansi'].isin(sample_rs_klinik)]
