from gcalendar import *
import sys

def list_calendars(calendar):
	result = calendar.calendarList().list().execute()
	items = result['items']
	for item in items:
		print("Summary:", item['summary'], "Calendar ID:", item['id'])
	
if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	list_calendars(calendar)