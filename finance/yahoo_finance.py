'''
http://theautomatic.net/yahoo_fin-documentation/

Requirements
Yahoo_fin requires the following packages to be installed:

ftplib
io
pandas
requests
requests_html

pip install requests_html
pip install pandas
pip install yahoo_fin
'''
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

'''
pip install yahoo_earnings_calendar
'''
import datetime
from pytz import timezone
from yahoo_earnings_calendar import YahooEarningsCalendar



def get_stock_price(ticker):
	return si.get_live_price(ticker)

def get_quote_table(ticker):
	return si.get_quote_table(ticker)
	
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
	print(get_stock_price("aapl"))
	get_next_earnings_date('aapl')

