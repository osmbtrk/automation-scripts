import time

import random

import pandas as pd

import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("lucid-course-213904-12e886932af1.json", scope)
client = gspread.authorize(creds)
sheetr = client.open("Untitled spreadsheet").get_worksheet(0)  # Open the spreadhseet

print(' Successfullyy opening file keyword Analysis!')
# Initialize an empty list to store the row indices and an empty dictionary to store the unique names

colF = sheetr.col_values(6, value_render_option='FORMULA')
colG = sheetr.col_values(7, value_render_option='FORMULA')

valuess = [colF,colG]
transposed_valuess = list(map(list, zip(*valuess)))
sheetr.batch_update([{
    'range': f'F1:G{len(colF)}',
    'values': transposed_valuess,
}],value_input_option="USER_ENTERED")
print(' Successfullyy data save!')
