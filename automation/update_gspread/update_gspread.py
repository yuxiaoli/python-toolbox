import sys
sys.path.append('../..')

from finance.yahoo_finance import *
from productivity.gdrive import gdrive
from productivity.calendar import gcalendar

# input - uppercase col
def col_char_to_num(col_char):
	return ord(col_char) - ord('A') + 1

# return - uppercase col
def num_to_col_char(num):
	return chr(num + ord('A') - 1)
		
def get_col_num(col_str):
	col_num = 0
	for power, char in enumerate(reversed(col_str.upper())):
		col_num += col_char_to_num(char) * (26 ** power)
		
	return col_num;

def get_col_str(num):
	col_str = "";
	remainder = 0;
	quotient = num;
	while (quotient != 0):
		remainder = (quotient - 1) % 26
		quotient = (quotient - 1) // 26
		col_str = num_to_col_char(remainder + 1) + col_str
		
	return col_str
	
def get_next_col(col_str):
	col_num = get_col_num(col_str)
	col_num = col_num + 1
	return get_col_str(col_num)
	
def is_future_datetime(isodatetime_str):
	isodatetime = datetime.datetime.fromisoformat(isodatetime_str)
	est = timezone('US/Eastern').localize(isodatetime);
	utc = est.astimezone(timezone('UTC'))
	
	isodatetime = utc.replace(tzinfo=None)
	now = datetime.datetime.utcnow()
	
	if (isodatetime > now):
		return True
	return False

def create_event_discription(company_name, next_earnings_date, marketcap, pe):
	discription = company_name + "'s estimated earnings date is " + next_earnings_date.strftime("%B %d, %Y at %H:%M EST\n")
	discription = discription + "Market Cap: " + marketcap + "\n" + "P/E: " + pe;
	return discription

def update_daily(gspread):
	row = 3
	col = 'E'
	ticker = "abc"
	while (ticker):
		ticker = gspread.getCell(row, get_col_num(col))
		yahoo_ticker = get_yahoo_ticker(ticker)
		print(yahoo_ticker)
		if (yahoo_ticker):
			# Update 1y target
			target = get_1y_target(yahoo_ticker)
			print(target)
			if (target and (str(target).lower() != "nan")):
				gspread.updateCell(12, get_col_num(col), target)
			
			# Update analyst rating
			rating = get_analyst_rating(yahoo_ticker)
			print(rating)
			if (rating != 6):
				gspread.updateCell(13, get_col_num(col), rating)
			
			est_table = get_est_table(yahoo_ticker)
			print(est_table)
			if (est_table):
				# Update valuation and discount
				valuation = est_table['Valuation']
				if (valuation):
					gspread.updateCell(14, get_col_num(col), valuation.lower())
				
				discount = est_table['Discount']
				if (discount):
					gspread.updateCell(15, get_col_num(col), discount)
				
				# Update short, mid, long term outlook
				shortTermOutlook = est_table.get('Short Term Outlook')
				if (shortTermOutlook):
					gspread.updateCell(16, get_col_num(col), shortTermOutlook)
				
				intermediateTermOutlook = est_table.get('Mid Term Outlook')
				if (intermediateTermOutlook):
					gspread.updateCell(17, get_col_num(col), intermediateTermOutlook)
				
				longTermOutlook = est_table.get('Long Term Outlook')
				if (longTermOutlook):
					gspread.updateCell(18, get_col_num(col), longTermOutlook)
				
				# Update support, resistance, resistance
				support = est_table['Support']
				if (support):
					gspread.updateCell(19, get_col_num(col), float(support))
				
				resistance = est_table['Resistance']
				if (resistance):
					gspread.updateCell(20, get_col_num(col), float(resistance))
				
				stopLoss = est_table['Stop Loss']
				if (stopLoss):
					gspread.updateCell(21, get_col_num(col), float(stopLoss))
		
		col = get_next_col(col)
	
	
def update_weekly(gspread, calendar):
	calendar_id = "5pr0h98mkvafbd7qp9nt4s6hdg@group.calendar.google.com"
	
	row = 3
	col = 'E'
	ticker = "abc"
	while (ticker):
		ticker = gspread.getCell(row, get_col_num(col))
		yahoo_ticker = get_yahoo_ticker(ticker)
		print(yahoo_ticker)
		if (yahoo_ticker):
			print(get_stock_price(yahoo_ticker))
			
			next_earnings_date = get_next_earnings_date(yahoo_ticker)
			print(next_earnings_date)
			
			if (not next_earnings_date):
				col = get_next_col(col)
				continue
			next_earnings_date_str = next_earnings_date.replace(microsecond=0).isoformat(' ')
			
			company_name = gspread.getCell(2, get_col_num(col)) + " (" + ticker + ")"
			summary = company_name + " " + next_earnings_date_str # Concatenate timestamp to make it unique
			marketcap = gspread.getCell(4, get_col_num(col))
			pe = gspread.getCell(5, get_col_num(col))
			discription = create_event_discription(company_name, next_earnings_date, marketcap, pe)
			print(discription.encode("utf-8"))
			
			cell_value = gspread.getCell(23, get_col_num(col))
			if (cell_value):
				if (cell_value == next_earnings_date_str):
					col = get_next_col(col)
					continue
					
				if (is_future_datetime(cell_value)):
					# Delete event in calendar
					old_summary = company_name + " " + cell_value
					event_id = calendar.findEvent(calendar_id, old_summary)
					calendar.deleteEvent(calendar_id, event_id)
				else:
					gspread.updateCell(22, get_col_num(col), cell_value)
					
			gspread.updateCell(23, get_col_num(col), next_earnings_date_str)
			
			# Create event in calendar
			calendar.createEvent(calendar_id,
							next_earnings_date.isoformat(),
							summary,
							1,
							discription,
							"",
							"America/New_York")
			
		col = get_next_col(col)
	return

	for ticker in tickers:
		price = get_stock_price(ticker)
		print(price)
		if (str(price).lower() != "nan"):
			row = tickers[ticker][0]
			col = get_col_num(tickers[ticker][1])
			gspread.updateCell(row, col, price)

def update_gspread(arg):
	#print(get_stock_price('aapl'))
	
	main = {
		"^dji": (3, 'l'),
		"^ixic": (4, 'l'),
		"^gspc": (5, 'l')
	}
	
	ticker_row = 3
	price_row = 6
	col = 'e'
	
	sheets = [
		"Aviation",
		"Cruise",
		"Hotel",
		"Retail",
		"Fashion",
		"Tech",
		"Petroleum",
		"Banking",
		"Investment",
		"Delivery",
		"Pharmaceutical",
		"Machine",
		"Arms",
		"Construction",
		"Others"
	]
	
	fname = "portfolio_public"
	
	gspread = gdrive.GSpread("client_secret.json")
	calendar = gcalendar.GCalendar("client_secret.json")
	
	for sheetname in sheets:
		print(sheetname)
		gspread.setSheet(fname, sheetname)
		if (arg == "daily"):
			update_daily(gspread)
		elif (arg == "weekly"):
			update_weekly(gspread, calendar)
	

if __name__ == "__main__":
	arg = sys.argv[1]
	update_gspread(arg)
	