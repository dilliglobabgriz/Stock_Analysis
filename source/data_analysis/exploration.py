import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"     # Hiding the oneDNN warning message
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
from datetime import datetime
from source.data_access.stock_data import Stock_Data

import warnings
warnings.filterwarnings("ignore")

stock_data = Stock_Data()
data = stock_data.data


def testAndSampleData():
    print(data.shape)
    print(data.sample(7))

def dataInfo():
    data.info()

def exploration():

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

    # plt.show()

    # Open-close data for selected company
    selected_company = 'MSFT'
    company_data = data[data['Name'] == selected_company]

    # Verify date range for MSFT
    #print(company_data['date'].min(), company_data['date'].max())

    # Filter data for prediction range
    prediction_range = company_data.loc[(company_data['date'] > datetime(2013, 1, 1))
                                        & (company_data['date'] < datetime(2018, 1, 1))]
    
    if not prediction_range.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(prediction_range['date'], prediction_range['close'])
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title(f'{selected_company} Stock Prices')
        plt.xticks(rotation=45)  # Rotate x-axis labels for readability
        plt.tight_layout()
        plt.show()
    else:
        print("No data to plot for the specified date range.")

def main():
    exploration()

main()