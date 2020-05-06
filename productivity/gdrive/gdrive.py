'''
Prerequisites

pip install gspread oauth2client
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import io
from googleapiclient.http import MediaIoBaseDownload
from apiclient.discovery import build
from httplib2 import Http


def gspread_login(filename):
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
	return client.open(filename).worksheets()
	
def export_csv(worksheet, filename):
	# Export values in the current sheet to a csv file
	rows = worksheet.get_all_values()
	
	with open(filename, mode='w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',')
		for row in rows:
			print(row)
			filewriter.writerow(row)
	
def export_xlsx(worksheets, filename):
	# Export all sheets into an Excel file

def gdrive_login():
	scope = ['https://www.googleapis.com/auth/drive']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	
	http_auth = credentials.authorize(Http())
	drive = build('drive', 'v3', http=http_auth)
	return drive
	
def get_file_id(drive, filename):
	# Return the file_id of the first filename match
	request = drive.files().list().execute()
	files = request['files']
	for f in files:
		print(f)
		if f['name'] == finename:
			return f['id']
			
	return None
	
def download_file(fileid, format, filename):
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	drive_service = GoogleDrive(gauth)
	
	request = drive_service.files().export_media(fileId=file_id,
												 mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	fh = io.BytesIO()
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
		status, done = downloader.next_chunk()
		print("Download %d%%." % int(status.progress() * 100))

if __name__ == "__main__":
	client = login('client_secret.json')
	
	sheet = get_sheet(client, "Asset Allocation", "Airlines")
	'''
	# Extract and print all of the values
	list_of_hashes = sheet.get_all_records()
	print(list_of_hashes)
	'''
	
	#sheet.update_cell(3, 1, "hey")
	
	#export_csv(sheet, "test.csv")
	
	'''
	sheets = get_all_sheets(client, "Asset Allocation")
	for sheet in sheets:
		print(sheet.title)
		print(sheet.id)
		#contents = sheet.get_all_records()
		#print(contents)
	'''
	
	
	
	# https://developers.google.com/drive/api/v3/ref-export-formats
	request = drive.files().export_media(fileId=file_id,
												 mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	fh = io.FileIO('test.xlsx', 'wb')
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
		status, done = downloader.next_chunk()
		print("Download %d%%." % int(status.progress() * 100))
	
	
	