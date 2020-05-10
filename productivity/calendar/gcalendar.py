from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
import pickle
import datetime
import pprint

# Timezone
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

def gcalendar_login(filename):
	scopes = ['https://www.googleapis.com/auth/calendar']
	credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
	service = build('calendar', 'v3', credentials=credentials)
	return service

# https://developers.google.com/calendar/v3/reference/events
def create_event(calendar, calendar_id, startdatetime, summary, duration=1, description="", location="", timezone="America/Los_Angeles"):
	start_date_time = datetime.datetime.fromisoformat(startdatetime)
	end_date_time = start_date_time + datetime.timedelta(hours=duration)
				
	event = {
		'summary': summary,
		'location': location,
		'description': description,
		'start': {
			'dateTime': start_date_time.strftime("%Y-%m-%dT%H:%M:%S"),
			'timeZone': timezone,
		},
		'end': {
			'dateTime': end_date_time.strftime("%Y-%m-%dT%H:%M:%S"),
			'timeZone': timezone,
		},
		'''
		'attendees': [
			{'email':attendees },
		],
		'''
		'reminders': {
			'useDefault': False,
			'overrides': [
				{'method': 'email', 'minutes': 24 * 60},
				{'method': 'popup', 'minutes': 10},
			],
		},
	}
	
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint('''*** %r event added: 
	Start: %s
	End:   %s''' % (summary.encode('utf-8'),
		#attendees,
		start_date_time, end_date_time))
		
	return calendar.events().insert(calendarId=calendar_id, body=event,sendNotifications=True).execute()
	
def list_events(calendar, calendar_id):
	calendar_list_entry = calendar.calendarList().get(calendarId=calendar_id).execute()
	print(calendar_list_entry['summary'])
	
if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	calendar_id = "0cpo4ke0ehi7dbr7td4h49e3jc@group.calendar.google.com"
	
	list_events(calendar, calendar_id)
	
	create_event(calendar,
				calendar_id,
				"2020-05-09 11:59:00",
				"Test Meeting using CreateFunction Method",
				0.5,
				"This is a test description"
				"Test Description",
				"",
				"America/New_York")