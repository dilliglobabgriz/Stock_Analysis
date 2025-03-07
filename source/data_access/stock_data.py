import os
import pandas as pd

class Stock_Data:
    def __init__(self, csv_name='all_stocks_5yr.csv'):
        self.csv_name = csv_name
        self.data = self.getData()
        
    def getData(self):
        base_project_path: str = 'C:/Users/isaac/Winter25/stocks/data'

        stocks_file_path = os.path.join(base_project_path, self.csv_name)

        if not os.path.exists(stocks_file_path):
            print(f'File: {stocks_file_path} Not Found')
            return

        data = pd.read_csv(stocks_file_path, delimiter=',', on_bad_lines='skip')

        data['date'] = pd.to_datetime(data['date'])

        return data