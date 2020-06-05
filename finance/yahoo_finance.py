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

'''
quote_table = {
	'1y Target Est': 316.95,
	'52 Week Range': '182.15 - 327.85',
	'Ask': '0.00 x 800',
	'Avg. Volume': 46732107.0,
	'Beta (5Y Monthly)': 1.24,
	'Bid': '0.00 x 1300',
	"Day's Range": '320.83 - 325.62',
	'EPS (TTM)': 11.89,
	'Earnings Date': 'Jul 28, 2020 - Aug 03, 2020',
	'Ex-Dividend Date': 'May 08, 2020',
	'Forward Dividend & Yield': '3.28 (1.01%)',
	'Market Cap': '1.397T',
	'Open': 324.39,
	'PE Ratio (TTM)': 27.11,
	'Previous Close': 325.12,
	'Quote Price': 322.32000732421875,
	'Volume': 21890091.0}
'''
def get_quote_table(ticker):
	return si.get_quote_table(ticker)
	
def get_next_earnings_date(ticker):
	yec = YahooEarningsCalendar()
	
	'''
	timestamp = yec.get_next_earnings_date(ticker)
	print(datetime.datetime.fromtimestamp(timestamp))
	'''

	earnings = yec.get_earnings_of(ticker)

	next_earnings_datetime = None
	delta_min = datetime.timedelta.max;
	for earning in earnings:
		startdatetime = earning['startdatetime']
		#print(startdatetime)
		startdatetime = startdatetime[:-1]
		isodatetime = datetime.datetime.fromisoformat(startdatetime)
		#print(isodatetime)
		
		est = timezone('US/Eastern').localize(isodatetime);
		#pst = est.astimezone(timezone('US/Pacific'))
		utc = est.astimezone(timezone('UTC'))
		
		isodatetime = utc.replace(tzinfo=None)
		now = datetime.datetime.utcnow()
		delta = isodatetime - now;
		
		if (delta.total_seconds() > 0 and delta < delta_min):
			delta_min = delta
			next_earnings_datetime = isodatetime
	
	if (not next_earnings_datetime):
		return
		
	utc = timezone('UTC').localize(next_earnings_datetime)
	est = utc.astimezone(timezone('US/Eastern'))
	next_earnings_datetime = est.replace(tzinfo=None)
	# print(next_earnings_datetime)
	return next_earnings_datetime

yahoo_tickers = {
	".DJI":		"^DJI",
	".IXIC":	"^IXIC",
	".INX":		"^GSPC",
	"RDS.B":	"RDS-B",
	"BRK.A":	"BRK-A"
}
	
def get_yahoo_ticker(google_ticker):
	if (not google_ticker):
		return ""

	if google_ticker in yahoo_tickers:
		return yahoo_tickers[google_ticker]
	else:
		yahoo_ticker = google_ticker.replace('.', '-')
		if (yahoo_ticker[0] == '-'):
			yahoo_ticker = yahoo_ticker.replace('-', '^', 1)
		return yahoo_ticker
	
if __name__ == "__main__":
	ticker = "aapl"
	print(get_stock_price(ticker))
	print(get_quote_table(ticker))
	get_next_earnings_date(ticker)

