from gcalendar import *
import sys

# https://developers.google.com/calendar/v3/reference/acl/insert
roles = {
	'n': "none",
	'fbr': "freeBusyReader",
	'r': "reader",
	'w': "writer",
	'o': "owner"
}

def add_acl(calendar, calendar_id, user, r):
	rule = {
		'scope': {
			'type': 'user',
			'value': user,
		},
		'role': roles[r]
	}
	
	created_rule = calendar.acl().insert(calendarId=calendar_id, body=rule).execute()
	print("Added User:", created_rule['id'])

if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	add_acl(calendar, sys.argv[1], sys.argv[2], sys.argv[3])
	