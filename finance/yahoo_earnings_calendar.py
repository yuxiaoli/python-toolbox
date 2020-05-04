import datetime
from scraper import YahooEarningsCalendar

date_from = datetime.datetime.strptime(
    'May 5 2017  10:00AM', '%b %d %Y %I:%M%p')
date_to = datetime.datetime.strptime(
    'May 8 2017  1:00PM', '%b %d %Y %I:%M%p')
yec = YahooEarningsCalendar()
dt = yec.get_next_earnings_date('amzn')
print(dt)
print(datetime.datetime.fromtimestamp(dt))