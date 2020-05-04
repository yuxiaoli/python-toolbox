import sys
sys.path.append('../..')

from finance.yahoo_fin import *
from productivity.gdrive import gdrive

def update_sheet(sheet, tickers):
	for ticker in tickers:
		price = get_stock_price(ticker)
		print(price)
		row = tickers[ticker][0]
		col = ord(tickers[ticker][1]) - 96
		sheet.update_cell(row, col, price)

def update_gspread():
	#print(get_stock_price('aapl'))
	
	print("hello, world")
	quote_table = get_quote_table('ba')
	#print(quote_table)
	if (quote_table["Market Cap"]):
		print(quote_table["Market Cap"])
	
	if (str(quote_table["PE Ratio (TTM)"]).lower() != "nan"):
		print(quote_table["PE Ratio (TTM)"])
	
	exit(0)
	
	main = {
		"dji": (2, 'i'),
		"^ixic": (3, 'i'),
		"^gspc": (4, 'i')
	}
	
	row_price = 4
	airlines = {
		"ual": (row_price, 'd'),
		"dal": (row_price, 'e'),
		"aal": (row_price, 'f'),
		"alk": (row_price, 'g'),
		"luv": (row_price, 'h'),
		"save": (row_price, 'i'),
		"ba": (row_price, 'j')
	}
	
	hotels = {
		"mgm": (row_price, 'd'),
		"hlt": (row_price, 'e'),
		"mar": (row_price, 'f')
	}
	
	retails = {
		"sbux": (row_price, 'd'),
		"dis": (row_price, 'e'),
		"stz": (row_price, 'f'),
		"ko": (row_price, 'g'),
		"v": (row_price, 'h')
	}
	
	tech = {
		"amzn": (row_price, 'd'),
		"googl": (row_price, 'e'),
		"fb": (row_price, 'f'),
		"sq": (row_price, 'g'),
		"yelp": (row_price, 'h'),
		"tsla": (row_price, 'i'),
		"snap": (row_price, 'j'),
		"nvda": (row_price, 'k'),
		"hubs": (row_price, 'l')
	}
	
	crude = {
		"vlo": (row_price, 'd'),
		"cvx": (row_price, 'e'),
		"rds-b": (row_price, 'f'),
		"epd": (row_price, 'g'),
		"psx": (row_price, 'h'),
		"bp": (row_price, 'i'),
		"ceo": (row_price, 'j'),
		"pba": (row_price, 'k'),
		"enb": (row_price, 'l'),
		"su": (row_price, 'm')
	}
	
	finance = {
		"bx": (row_price, 'd'),
		"cg": (row_price, 'e'),
		"kkr": (row_price, 'f'),
		"apo": (row_price, 'g')
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
	for sheetname in sheets:
		sheet = gdrive.get_sheet(client, fname, sheetname)
		update_sheet(sheet, sheets[sheetname])
	

if __name__ == "__main__":
	update_gspread()