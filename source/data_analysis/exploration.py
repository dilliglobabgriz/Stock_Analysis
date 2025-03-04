import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"     # Hiding the oneDNN warning message
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

base_project_path: str = 'C:/Users/isaac/Winter25/stocks'

stocks_file_path = os.path.join(base_project_path, 'data/all_stocks_5yr.csv')


def testAndSampleData():
    data = pd.read_csv(stocks_file_path, delimiter=',', on_bad_lines='skip')
    print(data.shape)
    print(data.sample(7))

def dataInfo():
    data = pd.read_csv(stocks_file_path, delimiter=',', on_bad_lines='skip')
    data['date'] = pd.to_datetime(data['date'])
    data.info()

def exploration():
    data = pd.read_csv(stocks_file_path, delimiter=',', on_bad_lines='skip')
    data['date'] = pd.to_datetime(data['date'])

    # Company list to track
    companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'IBM']

    # Create graph of open/close prices for last 5 years
    plt.figure(figsize=(15, 8))
    for index, company in enumerate(companies, 1):
        plt.subplot(3, 3, index)
        c = data[data['Name'] == company]
        plt.plot(c['date'], c['close'], c="r", label="close", marker="+")
        plt.plot(c['date'], c['open'], c="g", label="open", marker="^")
        plt.title(company)
        plt.legend()
        plt.tight_layout()
        
    #plt.show()

    # Trading volume as a function of time
    plt.figure(figsize=(15,8))
    for index, company in enumerate(companies, 1):
        plt.subplot(3, 3, index)
        c = data[data['Name'] == company]
        plt.plot(c['date'], c['volume'], c='purple', marker='*')
        plt.title(f'{company} Volume')
        plt.tight_layout()

    plt.show()

def main():
    if os.path.exists(stocks_file_path):
        exploration()
    else:
        print(f'File: {stocks_file_path} Not Found')

main()