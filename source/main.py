import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import os
from datetime import datetime
from source.model_training.train_by_company import Train_By_Company
from source.data_access.stock_data import Stock_Data

import warnings
warnings.filterwarnings("ignore")

sd = Stock_Data()
data = sd.data

def testTrainByCompany():
    tbc = Train_By_Company('MSFT')
    tbc.visualizeResults()

def testAndSampleData():
    print(data.shape)
    print(data.sample(7))

def dataInfo():
    data['date'] = pd.to_datetime(data['date'])
    data.info()

def main():
    testTrainByCompany()

if __name__ == '__main__':
    main()