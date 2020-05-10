from gcalendar import *
import sys

# Timezone
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

def create_calendar(calendar, summary, time_zone="America/Los_Angeles"):
	new_calendar = {
		'summary': summary,
		'timeZone': time_zone
		}
	created_calendar = calendar.calendars().insert(body=new_calendar).execute()
	print("Created Calendar ID:  ", created_calendar['id'])

if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	create_calendar(calendar, sys.argv[1], sys.argv[2])