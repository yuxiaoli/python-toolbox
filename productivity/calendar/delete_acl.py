from gcalendar import *
from list_acls import *
import sys

def delete_acl(calendar, calendar_id, rule_id):
	calendar.acl().delete(calendarId=calendar_id, ruleId=rule_id).execute()
	list_acls(calendar, calendar_id)

if __name__ == "__main__":
	calendar = gcalendar_login("client_secret.json")
	
	delete_acl(calendar, sys.argv[1], sys.argv[2])
	