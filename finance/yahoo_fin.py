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
'''

# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

def get_stock_price(ticker):
	return si.get_live_price(ticker)

def get_quote_table(ticker):
	return si.get_quote_table(ticker)

if __name__ == "__main__":
	print(get_stock_price("aapl"))

