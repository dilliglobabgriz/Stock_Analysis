import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import os
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

def main():
    if os.path.exists(stocks_file_path):
        dataInfo()
    else:
        print(f'File: {stocks_file_path} Not Found')

if __name__ == '__main__':
    main()