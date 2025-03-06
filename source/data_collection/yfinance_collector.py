import yfinance as yf
import pandas as pd
import os

# Modify these
csv_name = 'yf_5year_1day.csv'
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'IBM']
period = '5y'
interval = '1d'

base_path = 'C:/Users/isaac/Winter25/stocks/data'
save_path = os.path.join(base_path, csv_name)

data_array = []

# Ensure data is not overwritten
if os.path.exists(save_path):
    user_input = input(f'WARNING: {csv_name} already exists.\n(y) to continue, any other key to abort: ').strip().lower()
    if user_input != 'y':
        print("Aborted. File was not overwritten.")
        exit()

for ticker in tickers:
    data_set = yf.Ticker(ticker).history(period='10y', interval='1d')
    for date, row in data_set.iterrows():
        open_price = row['Open']
        close_price = row['Close']
        volume = row['Volume']
        
        # Create a list of the current stock information
        cur_stock_data = [ticker, open_price, close_price, volume, date]
        data_array.append(cur_stock_data)

print('Pulling data from yfinance...')
df = pd.DataFrame(data_array, columns=['Name', 'open', 'close', 'volume', 'date'])
df.to_csv(save_path, index=False)

print(f'{csv_name} was created and saved')