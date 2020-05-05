'''
Prerequisites

pip install gspread oauth2client
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def login(filename):
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)
	return gspread.authorize(creds)

def get_sheet(client, filename, sheetname):
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	return client.open(filename).worksheet(sheetname)
	
def get_all_sheets(client, filename):
	# Return a list of all sheets in the Google Sheets file
	
def export_csv(worksheet, outfname):
	# Export values in the current sheet to a csv file
	
def export_xlsx(file, outfname):
	# Export all sheets into an Excel file

if __name__ == "__main__":
	client = login('client_secret.json')
	
	sheet = get_sheet(client, "Asset Allocation", "Airlines")

	# Extract and print all of the values
	list_of_hashes = sheet.get_all_records()
	print(list_of_hashes)
	
	#sheet.update_cell(3, 1, "hey")
	