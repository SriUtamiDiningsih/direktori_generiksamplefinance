import gspread
import pandas as pd

def load_data(keyfile, sheet_id, worksheet_name):
    sheet_service = gspread.service_account(filename=keyfile)
    worksheet = sheet_service.open(sheet_id).worksheet(worksheet_name)
    return pd.DataFrame(worksheet.get_all_records())

def filter_special_price(data):
    return data[(data['Special Price'] == 'TRUE') & data['RS/Klinik'].notnull()]
