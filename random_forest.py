import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             root_mean_squared_error)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class RandomForest():
    def  __init__(self, analysis_panel, input_attributes, output_attributes):
        self.register = analysis_panel
        self.x = input_attributes
        self.y = output_attributes
        self.x_scaler = StandardScaler()
        self.y_scaler = StandardScaler()

    def create_regressor(self):
        x_training, x_test, y_training, y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=1)
        
        x_training_scaled = self.x_scaler.fit_transform(x_training)
        y_training_scaled = self.y_scaler.fit_transform(y_training.reshape(-1,1))
        
        x_test_scaled = self.x_scaler.fit_transform(x_test)
        y_test_scaled = self.y_scaler.fit_transform(y_test.reshape(-1,1))
        
        regressor = RandomForestRegressor(n_estimators = int(self.register.edt_n_tree.text()))
        regressor.fit(x_training_scaled, y_training_scaled.ravel())

        prediction = regressor.predict(x_test_scaled).reshape(-1,1)
        prediction_inverse = self.y_scaler.inverse_transform(prediction)
                
        prediction_average = str(prediction_inverse.mean())
        y_test_average = str(y_test.mean())
        mae_test = str(mean_absolute_error(y_test, prediction_inverse))
        mse_test = str(mean_squared_error(y_test, prediction_inverse))
        rmse_test = str(root_mean_squared_error(y_test, prediction_inverse))
        r2_test = str(regressor.score(x_test_scaled, y_test_scaled))

        return str(x_test), str(prediction_inverse), str(y_test), prediction_average, y_test_average, mae_test, mse_test, rmse_test, r2_test
    
    def predict_productivity(self, data):
        x_training, x_test, y_training, y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=1)
        
        x_training_scaled = self.x_scaler.fit_transform(x_training)
        y_training_scaled = self.y_scaler.fit_transform(y_training.reshape(-1,1))
        data_scaled = self.x_scaler.fit_transform(data)

        regressor = RandomForestRegressor(n_estimators=80)
        regressor.fit(x_training_scaled, y_training_scaled.ravel())

        prediction = regressor.predict(data_scaled).reshape(-1,1)
        prediction_inverse = self.y_scaler.inverse_transform(prediction)

        return prediction_inverse

if (__name__ == '__main__'):
    data_base = pd.read_csv('./network/network.csv')

    data_base = data_base.drop('ph_H2O_analysis', axis=1)
 
    x = data_base.drop(data_base.columns[2], axis=1).values
    for i in range(len(x)):
        for j in range(len(x[i])):
            if isinstance(x[i][j], str): 
                try:
                    x[i][j] = float(x[i][j].replace(',', '.'))
                except ValueError:
                    pass
   
    onehotencoder = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
    x = onehotencoder.fit_transform(x)

    y = data_base['average_productivity_analysis'].values
    for i in range(len(y)):
        if isinstance(y[i], str):
            try:
                y[i] = float(y[i].replace(',', '.'))
            except ValueError:
                   pass
    x = np.array(x)
    y = np.array(y) 
    print('X = ', x)
    print('')          
    print('y = ', y)
    
    rf = RandomForest(x, y)

    (x_test,
    prediction,
    y_test,
    prediction_average,
    y_test_average,
    mae_test,
    mse_test,
    rmse_test,
    r2_test) = rf.create_regressor()

    print('Dados de entrada para a realização do teste..................: ', x_test)
    print(' ')
    print('Previsões obtidas com os dados de entrada....................: ', prediction)
    print(' ')
    print('Respostas esperadas com os dados de entrada..................: ', y_test)
    print(' ')
    print('Média das previsões obtidas com os dados de entrada..........: ', prediction_average)
    print(' ')
    print('Média das respostas esperadas com os dados de entrada........: ', y_test_average)
    print(' ')
    print('Erro absoluto médio (Mean Absolute Error - MAE)..............: ',mae_test)
    print(' ')
    print('Erro quadrático médio (Mean Squared Error-MSE)...............: ',mse_test)
    print(' ')
    print('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ',rmse_test)
    print(' ')
    print('Coeficiente de determinação R² (R-squared)...................: ',r2_test)


