from gcalendar import *
from list_calendars import *
import sys

def delete_calendar(calendar, calendar_id):
	result = calendar.calendars().delete(calendarId=calendar_id).execute()
	
	
if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	delete_calendar(calendar, sys.argv[1])
	list_calendars(calendar)