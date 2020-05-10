'''
Prerequisites

pip install gspread oauth2client

pip install google-api-python-client
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import datetime
import time

from httplib2 import Http
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload

# https://developers.google.com/drive/api/v3/ref-export-formats
mime_types = {
	'txt': 'text/plain',
	'pdf': 'application/pdf',
	'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
	'csv': 'text/csv',
	'jpeg': 'image/jpeg',
	'png': 'image/png',
	'svg': 'image/svg+xml',
	'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
	'json': 'application/vnd.google-apps.script+json'
}

'''
"Quota exceeded for quota group 'WriteGroup' 
and limit 'Write requests per user per 100 seconds' 
of service 'sheets.googleapis.com' 
for consumer 'project_number:593539420221'."
'''
duration = 100 # in seconds
'''
max_write_request_num = 100
client_history = {}
'''

def gspread_login(filename):
	# use creds to create a client to interact with the Google Drive API
	scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
	client = gspread.authorize(creds)
	#client_history[client] = [];
	return client;

def get_sheet(client, filename, sheetname):
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	return client.open(filename).worksheet(sheetname)
	
def get_all_sheets(client, filename):
	# Return a list of all sheets in the Google Sheets file
	return client.open(filename).worksheets()
	
def update_cell(sheet, row, col, val, depth=0):
	'''
	history = client_history[client]
	if (len(history) == max_write_request_num):
		timedelta = (datetime.datetime.now() - history[0]).total_seconds()
		if (duration > timedelta):
			time.sleep(duration - (timedelta))
		history.pop(0)
	
	sheet.update_cell(row, col, val);
	history.append(datetime.datetime.now())
	'''
	if (depth == 3):
		print("Cell cannot be updated")
		return
		
	try:
		sheet.update_cell(row, col, val);
	except:
		time.sleep(duration)
		update_cell(sheet, row, col, val, depth+1)
	
def export_csv(worksheet, filename):
	# Export values in the current sheet to a csv file
	rows = worksheet.get_all_values()
	
	with open(filename, mode='w', newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',')
		for row in rows:
			filewriter.writerow(row)

def gdrive_login(filename):
	# https://stackoverflow.com/questions/46457093/google-drive-api-with-python-from-serverbackend-without-browser-autentication
	scopes = ['https://www.googleapis.com/auth/drive']
	credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
	
	http_auth = credentials.authorize(Http())
	drive = build('drive', 'v3', http=http_auth)
	return drive
	
def search(drive, filename):
	# Return the file_id of the first filename found
	# https://developers.google.com/drive/api/v3/search-files#python
	page_token = None
	while True:
		response = drive.files().list(q="name='" + filename + "'",
											  spaces='drive',
											  fields='nextPageToken, files(id, name)',
											  pageToken=page_token).execute()
		for file in response.get('files', []):
			# Process change
			print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
			return file['id']
		page_token = response.get('nextPageToken', None)
		if page_token is None:
			break
	
	return None
	
def download_file(drive, fileid, format, filename):
	# https://developers.google.com/drive/api/v3/manage-downloads#python

	# Download a file stored on Google Drive
	#request = drive_service.files().get_media(fileId=file_id)
	
	# Download a Google Document
	request = drive.files().export_media(fileId=file_id, mimeType=mime_types[format])
	#request = drive.files().export(fileId=file_id, mimeType=mime_types[format])
	
	fh = io.FileIO(filename, 'wb')
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
		status, done = downloader.next_chunk()
		print("Download %d%%." % int(status.progress() * 100))

if __name__ == "__main__":
	client = gspread_login('client_secret.json')
	
	sheet = get_sheet(client, "Asset Allocation", "Airlines")
	
	for x in range(50000):
		print(x)
		update_cell(sheet, 1, 1, x)
	
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
	
	'''
	drive = gdrive_login('client_secret.json')
	file_id = search(drive, "Asset Allocation")
	download_file(drive, file_id, 'xlsx', 'test.xlsx')
	
	file_id = search(drive, "5/4")
	download_file(drive, file_id, 'docx', 'May4th.docx')
	'''
	
	
	
	
	
	