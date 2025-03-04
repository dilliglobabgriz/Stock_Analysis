from source.data_access.stock_data import Stock_Data
from datetime import datetime
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"     # Hiding the oneDNN warning message
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class Train_By_Company:
    def __init__(self, company):
        self.company = company
        self.data = self.generateData()
        self.selected_company_data = self.data[self.data['Name'] == self.company]
        self.dataset = self.generateDataset()
        self.scaler = MinMaxScaler(feature_range=(0,1))
        self.scaled_data = self.generateScaledData()
        self.training = int(np.ceil(len(self.dataset) * .95))
        

    def generateData(self):
        stock_data = Stock_Data()
        return stock_data.data
    
    def generateDataset(self):
        close_data = self.selected_company_data.filter(['close'])
        dataset = close_data.values
        return dataset
    
    def generateScaledData(self):
        scaled_data = self.scaler.fit_transform(self.dataset)
        return scaled_data
    
    def trainData(self):

        train_data = self.scaled_data[0:int(self.training), :]

        x_train = []
        y_train = []

        for i in range(60, len(train_data)):
            x_train.append(train_data[i-60:i, 0])
            y_train.append(train_data[i, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        model = keras.models.Sequential()
        model.add(keras.layers.LSTM(units=64,
                                    return_sequences=True,
                                    input_shape=(x_train.shape[1], 1)))
        model.add(keras.layers.LSTM(units=64))
        model.add(keras.layers.Dense(32))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(1))
        model.summary()

        model.compile(optimizer='adam',
                      loss='mean_squared_error')
        history = model.fit(x_train,
                            y_train,
                            epochs=10)
        
        x_test, y_test = self.generateTestData()

        # Predictions for test data
        predictions = model.predict(x_test)
        predictions = self.scaler.inverse_transform(predictions)

        # Model eval
        mse = np.mean(((predictions - y_test) ** 2))
        print(f'MSE: {mse}')
        print(f'RMSE: {np.sqrt(mse)}')

        return predictions


        
    def generateTestData(self):             # Return a tuple of x_test and y_test data both arrays
        test_data = self.scaled_data[self.training - 60:, :]
        x_test = []
        y_test = self.dataset[self.training:, :]
        for i in range(60, len(test_data)):
            x_test.append(test_data[i-60:i, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        return (x_test, y_test)
    
    def visualizeResults(self) -> None:
        predictions = self.trainData()
        train = self.selected_company_data[:self.training]
        test = self.selected_company_data[self.training:]
        test['Predictions'] = predictions

        plt.figure(figsize=(10, 8))
        plt.plot(train['date'], train['close'])
        plt.plot(test['date'], test[['close', 'Predictions']])
        plt.title(f'{self.company} Stock Close Price')
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.legend(['Train', 'Test', 'Predictions'])

        plt.show()
        