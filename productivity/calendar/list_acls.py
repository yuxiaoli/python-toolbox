from gcalendar import *
import sys

def list_acls(calendar, calendar_id):
	result = calendar.acl().list(calendarId=calendar_id).execute()
	items = result['items']
	for item in items:
		print(item['id'], item['role'])

if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	list_acls(calendar, sys.argv[1])