from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
import csv
import datetime
import pprint


# Timezone
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

class GCalendar:

	# https://developers.google.com/calendar/v3/reference/acl/insert
	roles = {
		'n': "none",
		'fbr': "freeBusyReader",
		'r': "reader",
		'w': "writer",
		'o': "owner"
	}
	
	def __init__(self, filename):
		self.login(filename)
		self.calendar_id = "";
	
	def login(self, filename):
		scopes = ['https://www.googleapis.com/auth/calendar']
		try:
			credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes)
			self.service = build('calendar', 'v3', credentials=credentials)
		except:
			print("Login failed")
			return
	
	def dialogue(self):
		quit = False
		while (not quit):
			if (not self.calendar_id):
				print('Create calendar: create summary timezone="America/Los_Angeles"')
				print("Delete calendar: delete calendar_id")
				print("List calendars: list")
				print("Select calendar: select calendar_id")
				print("Quit: quit")
				
				cmd = input("> ")
				if (cmd):
					result = csv.reader([cmd], delimiter=' ', skipinitialspace=True)
					args = next(result)
					
					if (args[0] == "create"):
						if (len(args) == 2):
							self.createCalendar(args[1])
						elif (len(args) == 3):
							self.createCalendar(args[1], args[2])
						else:
							print("Invalid command")
						
					elif (args[0] == "delete"):
						if (len(args) == 2):
							self.deleteCalendar(args[1])
						else:
							print("Invalid command")
						
					elif (args[0] == "list"):
						self.listCalendars()
						
					elif (args[0] == "select"):
						if (len(args) == 2):
							self.calendar_id = args[1]
						else:
							print("Invalid command")
						
					elif (args[0] == "quit"):
						quit = True
						
					else:
						print("Unknown command")
						
				else:
					print("No input recorded")
				
			else:
				print("Add acl: add user role")
				print(self.roles)
				print("Delete acl: delete user_id")
				print("List acls: list")
				print("Unselect/Change calendar: back")
				
				cmd = input("> ")
				if (cmd):
					result = csv.reader([cmd], delimiter=' ', skipinitialspace=True)
					args = next(result)
					
					if (args[0] == "add"):
						if (len(args) == 3):
							self.addAcl(args[1], args[2])
						else:
							print("Invalid command")
							
					elif (args[0] == "delete"):
						if (len(args) == 2):
							self.deleteAcl(args[1])
						else:
							print("Invalid command")
							
					elif (args[0] == "list"):
						self.listAcls()
						
					elif (args[0] == "back"):
						self.calendar_id = None
						
					else:
						print("Unknow command")
				
				else:
					print("No input recorded")
			
			print()
			continue
			
	def createCalendar(self, summary, time_zone="America/Los_Angeles"):
		
		new_calendar = {
			'summary': summary,
			'timeZone': time_zone
			}
		
		try:
			created_calendar = self.service.calendars().insert(body=new_calendar).execute()
		except:
			print("Create calendar failed")
			return
			
		print("Created Calendar ID:  ", created_calendar['id'])
			
	def deleteCalendar(self, calendar_id):
		try:
			self.service.calendars().delete(calendarId=calendar_id).execute()
		except:
			print("Delete calendar failed")
			
		self.listCalendars()
			
	def listCalendars(self):
		try:
			calendars = self.service.calendarList().list().execute()
		except:
			return;
			
		for calendar in calendars['items']:
			print("Summary:", calendar['summary'], "Calendar ID:", calendar['id'])
			
	def addAcl(self, user, r):
		rule = {
			'scope': {
				'type': 'user',
				'value': user,
			},
			'role': self.roles[r]
		}
		
		try:
			created_rule = self.service.acl().insert(calendarId=self.calendar_id, body=rule).execute()
		except:
			print("Add ACL failed")
			return
			
		print("Added User:", created_rule['id'])
		
	def deleteAcl(self, rule_id):
		try:
			self.service.acl().delete(calendarId=self.calendar_id, ruleId=rule_id).execute()
		except:
			print("Delete ACL failed")
			
		self.listAcls()
	
	def listAcls(self):
		try:
			result = self.service.acl().list(calendarId=self.calendar_id).execute()
		except:
			return
		
		users = result['items']
		for user in users:
			print(user['id'], user['role'])
	
	def createEvent(self, calendar_id, startdatetime, summary, duration=1, description="", location="", timezone="America/Los_Angeles"):
		# https://developers.google.com/calendar/v3/reference/events
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
			
		return self.service.events().insert(calendarId=calendar_id, body=event,sendNotifications=True).execute()
	
	def deleteEvent(self, calendar_id, event_id):
		# https://developers.google.com/calendar/v3/reference/events/delete#python
		try:
			self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
		except:
			print("Delete event failed")
			return
		return
		
	def listEvents(self, calendar_id):
		# https://developers.google.com/calendar/v3/reference/events/list#python
		page_token = None
		while True:
			events = self.service.events().list(calendarId=calendar_id, pageToken=page_token).execute()
			for event in events['items']:
				print(event['summary'])
			page_token = events.get('nextPageToken')
			if not page_token:
				break
				
	def findEvent(self, calendar_id, summary):
		# Returns event_id whose summary equals summary
		page_token = None
		while True:
			events = self.service.events().list(calendarId=calendar_id, pageToken=page_token).execute()
			for event in events['items']:
				if (event['summary'] == summary):
					return event['id']
			page_token = events.get('nextPageToken')
			if not page_token:
				break


	
if __name__ == "__main__":
	gcalendar = GCalendar("client_secret.json")
	gcalendar.dialogue()
	'''
	calendar_id = "5pr0h98mkvafbd7qp9nt4s6hdg@group.calendar.google.com"
	
	gcalendar.createEvent(calendar_id,
							"2020-05-10 11:59:00",
							"Test Meeting using CreateFunction Method",
							0.5,
							"This is a test description"
							"Test Description",
							"",
							"America/New_York")
							
	gcalendar.listEvents(calendar_id)
	
	event_id = gcalendar.findEvent(calendar_id, "Test Meeting using CreateFunction Method")
	print("Found event:", event_id)
	
	gcalendar.deleteEvent(calendar_id, event_id)
	'''