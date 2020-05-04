import datetime
from pytz import timezone
from yahoo_earnings_calendar import YahooEarningsCalendar

def get_next_earnings_date(ticker):
	yec = YahooEarningsCalendar()
	
	'''
	timestamp = yec.get_next_earnings_date(ticker)
	print(datetime.datetime.fromtimestamp(timestamp))
	'''

	earnings = yec.get_earnings_of(ticker)

	next_earnings_datetime = datetime.datetime.now();
	delta_min = datetime.timedelta.max;
	for earning in earnings:
		startdatetime = earning['startdatetime']
		#print(startdatetime)
		startdatetime = startdatetime[:-1]
		isodatetime = datetime.datetime.fromisoformat(startdatetime)
		#print(isodatetime)
		
		est = timezone('US/Eastern').localize(isodatetime);
		pst = est.astimezone(timezone('US/Pacific'))
		
		isodatetime = pst.replace(tzinfo=None)
		now = datetime.datetime.now()
		delta = isodatetime - now;
		
		if (delta.total_seconds() > 0 and delta < delta_min):
			delta_min = delta
			next_earnings_datetime = isodatetime
		
	print(next_earnings_datetime)
	return next_earnings_datetime

if __name__ == "__main__":
	get_next_earnings_date('aapl')