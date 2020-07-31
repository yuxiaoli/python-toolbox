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

from urllib.error import HTTPError

class GSpread:
	'''
	"Quota exceeded for quota group 'WriteGroup' 
	and limit 'Write requests per user per 100 seconds' 
	of service 'sheets.googleapis.com' 
	for consumer 'project_number:593539420221'."
	'''
	duration = 100 # in seconds
	#depthMax = 3
	
	def __init__(self, filename):
		self.login(filename)
		self.worksheet = None
	
	def login(self, filename):
		# use creds to create a client to interact with the Google Drive API
		scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		try:
			creds = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
			self.client = gspread.authorize(creds)
		except:
			print("Login failed")
			return
		
	def getClient(self):
		return self.client
	
	def setSheet(self, filename, sheetname, depth=1, depthMax=3):
		try:
			self.worksheet = self.client.open(filename).worksheet(sheetname)
		except:
			if (depth == depthMax):
				print("Cannot open worksheet")
				return
			time.sleep(self.duration)
			self.setSheet(filename, sheetname, depth+1)
			
			
	def getSheet(self):
		return self.worksheet
		
	def printSheet(self):
		# Extract and print all of the values
		list_of_hashes = self.sheet.get_all_records()
		print(list_of_hashes)
		
	def getCell(self, row, col, depth=1, depthMax=3):
		if (self.worksheet == None):
			print("Worksheet is not set")
			return
			
		try:
			return self.worksheet.cell(row, col).value
		except:
			if (depth == depthMax):
				print("Cell cannot be read")
				return
			time.sleep(self.duration)
			return self.getCell(row, col, depth+1)
	
	def updateCell(self, row, col, val, depth=1, depthMax=3):
		if (self.worksheet == None):
			print("Worksheet is not set")
			return
			
		try:
			self.worksheet.update_cell(row, col, val);
		except:
			if (depth == depthMax):
				print("Cell cannot be updated")
				return
			time.sleep(self.duration)
			self.updateCell(row, col, val, depth+1)
			
	def exportCsv(self, filename):
		# Export values in the current sheet to a csv file
		try:
			rows = self.worksheet.get_all_values()
		except:
			print("Cannot read worksheet")
			return
		
		with open(filename, mode='w', newline='') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',')
			for row in rows:
				filewriter.writerow(row)
				
	def getAllSheets(self, filename):
		# Return a list of all sheets in the Google Sheets file
		try:
			return self.client.open(filename).worksheets()
		except:
			return None
	
	def printAllSheets(self, filename):
		sheets = self.getAllSheets(filename)
		for sheet in sheets:
			print(sheet.title)
			print(sheet.id)
			#contents = sheet.get_all_records()
			#print(contents)


			
class GDrive:
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

	def __init__(self, filename):
		self.login(filename)
		
	def login(self, filename):
		# https://stackoverflow.com/questions/46457093/google-drive-api-with-python-from-serverbackend-without-browser-autentication
		scopes = ['https://www.googleapis.com/auth/drive']
		try:
			credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
			http_auth = credentials.authorize(Http())
			self.drive = build('drive', 'v3', http=http_auth)
		except:
			print("Login failed")
			return
			
	def search(self, filename):
		# Return the file_id of the first filename found
		# https://developers.google.com/drive/api/v3/search-files#python
		page_token = None
		while True:
			response = self.drive.files().list(q="name='" + filename + "'",
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
		
		print("File", filename, "not found")
		return None
		
	def downloadFile(self, fileid, format, filename):
		# https://developers.google.com/drive/api/v3/manage-downloads#python

		# Download a file stored on Google Drive
		#request = drive_service.files().get_media(fileId=file_id)
		
		# Download a Google Document
		request = self.drive.files().export_media(fileId=file_id, mimeType=self.mime_types[format])
		#request = drive.files().export(fileId=file_id, mimeType=mime_types[format])
		
		fh = io.FileIO(filename, 'wb')
		downloader = MediaIoBaseDownload(fh, request)
		done = False
		while done is False:
			status, done = downloader.next_chunk()
			print("Download %d%%." % int(status.progress() * 100))



class GMail:
	def __init__(self, filename):
		self.login(filename)
		
	def login(self, filename):
		# https://developers.google.com/gmail/api/auth/scopes
		scopes = ['https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose', 'https://www.googleapis.com/auth/gmail.modify']
		try:
			credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
			http_auth = credentials.authorize(Http())
			self.service = build('gmail', 'v1', http=http_auth)
			
		except:
			print("Login failed")
			return

		# Call the Gmail API
		results = self.service.users().labels().list(userId='me').execute()
		labels = results.get('labels', [])

		if not labels:
			print('No labels found.')
		else:
			print('Labels:')
			for label in labels:
				print(label['name'])

	def send(self, message, user_id="me"):
		"""Send an email message.
		
		Args:
		user_id: User's email address. The special value "me"
		can be used to indicate the authenticated user.
		message: Message to be sent.

		Returns:
		Sent Message.
		"""
		try:
			message = (self.service.users().messages().send(userId="yuxiaoli.bot@gmail.com", body=message).execute())
			print('Message Id: %s' % message['id'])
			return message
		except HTTPError as error:
			print('An error occurred: %s' % error)


if __name__ == "__main__":
	
	gspread = GSpread("client_secret.json")
	gspread.setSheet("Asset Allocation", "Airlines")
	
	for x in range(50000):
		print(x)
		gspread.updateCell(1, 1, x)
	
	
	#gspread.printAllSheets("Asset Allocation")
	
	#gspread.exportCsv("test.csv")
	
	#gspread.printAllSheets("Asset Allocation")
	'''
	gdrive = GDrive("client_secret.json")
	file_id = gdrive.search("Asset Allocation")
	gdrive.downloadFile(file_id, 'xlsx', 'test.xlsx')
	
	file_id = gdrive.search("5/4")
	gdrive.downloadFile(file_id, 'docx', 'May4th.docx')
	'''
	
	
	
	
	
	