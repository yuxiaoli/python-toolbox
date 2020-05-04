import sys
sys.path.append('../..')

from finance.yahoo_fin import *
from productivity.gdrive import gdrive


def get_col_num(col):
	return ord(col) - 96

def update_daily(sheet, tickers):
	for ticker in tickers:
		price = get_stock_price(ticker)
		print(price)
		if (str(price).lower() != "nan"):
			row = tickers[ticker][0]
			col = get_col_num(tickers[ticker][1])
			sheet.update_cell(row, col, price)
		
def update_weekly(sheet, tickers):
	for ticker in tickers:
		col = get_col_num(tickers[ticker][1])
		quote_table = get_quote_table(ticker)
		print(quote_table["Market Cap"])
		print(quote_table["PE Ratio (TTM)"])
		
		if (str(quote_table["Market Cap"]).lower() != "nan"):
			row = 1
			sheet.update_cell(row, col, quote_table["Market Cap"])
		
		if (str(quote_table["PE Ratio (TTM)"]).lower() != "nan"):
			row = 2
			sheet.update_cell(row, col, quote_table["PE Ratio (TTM)"])
		

def update_gspread(arg):
	#print(get_stock_price('aapl'))
	
	main = {
		"^dji": (2, 'i'),
		"^ixic": (3, 'i'),
		"^gspc": (4, 'i')
	}
	
	row = 4
	airlines = {
		"ual": (row, 'd'),
		"dal": (row, 'e'),
		"aal": (row, 'f'),
		"alk": (row, 'g'),
		"luv": (row, 'h'),
		"save": (row, 'i'),
		"ba": (row, 'j')
	}
	
	hotels = {
		"mgm": (row, 'd'),
		"hlt": (row, 'e'),
		"mar": (row, 'f')
	}
	
	retails = {
		"sbux": (row, 'd'),
		"dis": (row, 'e'),
		"stz": (row, 'f'),
		"ko": (row, 'g'),
		"v": (row, 'h')
	}
	
	tech = {
		"amzn": (row, 'd'),
		"googl": (row, 'e'),
		"fb": (row, 'f'),
		"sq": (row, 'g'),
		"yelp": (row, 'h'),
		"tsla": (row, 'i'),
		"snap": (row, 'j'),
		"nvda": (row, 'k'),
		"hubs": (row, 'l')
	}
	
	crude = {
		"vlo": (row, 'd'),
		"cvx": (row, 'e'),
		"rds-b": (row, 'f'),
		"epd": (row, 'g'),
		"psx": (row, 'h'),
		"bp": (row, 'i'),
		"ceo": (row, 'j'),
		"pba": (row, 'k'),
		"enb": (row, 'l'),
		"su": (row, 'm')
	}
	
	finance = {
		"bx": (row, 'd'),
		"cg": (row, 'e'),
		"kkr": (row, 'f'),
		"apo": (row, 'g')
	}
	
	sheets = {
		"Main": main,
		"Airlines": airlines,
		"Hotels": hotels,
		"Retails": retails,
		"Tech": tech,
		"Crude Oil": crude,
		"Finance": finance
	}
	
	fname = "Asset Allocation"
	
	client = gdrive.login("client_secret.json")
	
	if (arg == "daily"):
		for sheetname in sheets:
			sheet = gdrive.get_sheet(client, fname, sheetname)
			update_daily(sheet, sheets[sheetname])
				
	elif (arg == "weekly"):
		for sheetname in sheets:
			if (sheetname == "Main"):
				continue
			sheet = gdrive.get_sheet(client, fname, sheetname)
			update_weekly(sheet, sheets[sheetname])
		
	

if __name__ == "__main__":
	arg = sys.argv[1]
	update_gspread(arg)