import os
import random
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import tensorflow as tf
from PySide6.QtWidgets import QApplication
from scikeras.wrappers import KerasRegressor
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score,
                             root_mean_squared_error)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from tensorflow.keras import backend as k
from tensorflow.keras.models import Sequential

from random_forest import RandomForest
from regression import Regression
from support_vectors import SupportVectors
from tools import message, validates_float


class Neural_Network():
    def __init__(self, analysis_panel):
        self.register = analysis_panel
        self.x_scaler = StandardScaler()
        self.y_scaler = StandardScaler()
        self.base = self.processing_data()
        self.neural_network_structure = self.create_neural_network()
        self.regressor = KerasRegressor(model = self.neural_network_structure , epochs = int(self.register.edt_epochs.text()), batch_size = int(self.register.edt_batch_size.text()))

    def processing_data(self):
        self.register.analysis_data.export_neural_network_csv()
        result = pd.read_csv('./network/network.csv')
        result = result.drop('ph_H2O_analysis', axis=1)
        result = result.drop('P_rem_analysis', axis=1) 
        result = result.drop('Na_analysis', axis=1) 
        result = result.drop('top_dressing_P2O5_analysis_kg', axis=1) 
        return result

    def fetch_input_attributes(self):
        x = self.base.drop(self.base.columns[2], axis=1).values
        for i in range(len(x)):
            for j in range(len(x[i])):
                if isinstance(x[i][j], str): 
                    try:
                        x[i][j] = float(x[i][j].replace(',', '.'))
                    except ValueError:
                        pass
   
        onehotencoder = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
        x = onehotencoder.fit_transform(x)
        """
           'CONVENCIONAL - IRRIGADO'	    1.0	 0.0  0.0  0.0
           'CONVENCIONAL - SEQUEIRO'	    0.0	 1.0  0.0  0.0
           'PLANTIO DIRETO - IRRIGADO'  	0.0	 0.0  1.0  0.0
           'PLANTIO DIRETO - SEQUEIRO'	    0.0	 0.0  0.0  1.0
        """
        return x

    def fetch_output_attributes(self):
        y = self.base['average_productivity_analysis'].values
        for i in range(len(y)):
            if isinstance(y[i], str):
                    try:
                        y[i] = float(y[i].replace(',', '.'))
                    except ValueError:
                        pass
        return y

    def create_neural_network(self):
        k.clear_session()

        network = Sequential([
            tf.keras.layers.InputLayer(shape = (34,)),
            tf.keras.layers.Dense(units = 18, activation = 'relu', kernel_initializer='random_uniform'),
            tf.keras.layers.Dense(units = 18, activation = 'relu', kernel_initializer='random_uniform'),
            tf.keras.layers.Dense(units = 1, activation  = 'linear')])

        optimizer = tf.optimizers.Adam(learning_rate=validates_float(self.register.edt_learning_rate.text()))# 0.0001, 0.001, 0.01 
        network.compile(optimizer = optimizer, loss='mean_absolute_error', metrics = ['mean_absolute_error'])

        return network

    def cross_validation(self):
        if self.validate_parameters() ==  True:
            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S:')
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Processando a Validação Cruzada....')
            self.register.edt_process.append(' ')
            QApplication.processEvents()  
            time.sleep(2) 

            x = self.fetch_input_attributes() 
            y = self.fetch_output_attributes()

            x_s = self.x_scaler.fit_transform(x)
            y_s = self.y_scaler.fit_transform(y.reshape(-1,1))
            print(x_s)
            print(y_s)
        
            self.regressor = KerasRegressor(model = self.neural_network_structure , epochs = int(self.register.edt_epochs.text()), batch_size = int(self.register.edt_batch_size.text()))
            
            result = cross_val_score(estimator = self.regressor, X = x_s, y = y_s.ravel(), cv=int(self.register.edt_cv.text()), scoring='neg_mean_absolute_error')

            self.register.edt_process.append('Validação Cruzada....:' + str(abs(result)))
            self.register.edt_process.append('Média de variação....:' + str(abs(result.mean())))
            self.register.edt_process.append('Desvio Padrão........:' + str(result.std()))



    def training_testing(self):
        if self.validate_parameters() ==  True:
            test = 100.00 - float(self.register.edt_training.text())
             
            x_training, x_test, y_training, y_test = train_test_split(self.fetch_input_attributes(), self.fetch_output_attributes(), test_size=(test/100))
       
            x_training_scaled = self.x_scaler.fit_transform(x_training)
            y_training_scaled = self.y_scaler.fit_transform(y_training.reshape(-1,1))
            x_test_scaled = self.x_scaler.fit_transform(x_test)
            y_test_scaled = self.y_scaler.fit_transform(y_test.reshape(-1,1))

            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S:')
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Processando o treinamento com '+str(100.00-test)+'(%) dos dados e '+str(test)+'(%) para testar'+'....')
            self.register.edt_process.append(' ')
            QApplication.processEvents()  
            time.sleep(2)  
            self.regressor = KerasRegressor(model = self.neural_network_structure , epochs = int(self.register.edt_epochs.text()), batch_size = int(self.register.edt_batch_size.text()))
            
            self.regressor.fit(x_training_scaled, y_training_scaled.ravel())
            prediction = self.regressor.predict(x_test_scaled).reshape(-1,1)
            prediction_inverse = self.y_scaler.inverse_transform(prediction)

            self.register.edt_process.append('Atributos preditivos utilizados foram:') 
            self.register.edt_process.append('')
            self.register.edt_process.append('Altitude, sistema de plantio, temperatura mínima, temperatura máxima, chuva no vegetativo, chuva no reprodutivo, ph CaCl2, teor de argila, MO, CO, K-cmolc, Ca, Mg, Al, H Al, P, k-mg, S-SO4, B, Cu, Fe, Mn, Zn, adubação no pré-plantio de N, adubação no pré-plantio de P, adubação no pré-plantio de K, adubação no plantio de N, adubação no plantio de P, adubação no plantio de K, adubação no pós-plantio de N e adubação no pós-plantio de K.')
            self.register.edt_process.append('')
            self.register.edt_process.append('Dados de entrada para a realização do teste..................: '+ str(x_test))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: '+ str(prediction_inverse))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: '+ str(y_test))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: '+ str(prediction_inverse.mean()))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: '+ str(y_test.mean()))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: '+ str(mean_absolute_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Erro quadrático médio (Mean Squared Error-MSE)...............: '+ str(mean_squared_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: '+ str(root_mean_squared_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: '+ str(r2_score(y_test, prediction_inverse)))

    def validate_parameters(self):
        try:
            epochs = int(self.register.edt_epochs.text())
            batch_size = int(self.register.edt_batch_size.text())
            training = int(self.register.edt_training.text())
            cv = int(self.register.edt_cv.text())
        except Exception as e:
            message('erro', 'Todos os campos devem conter números inteiros..:' + str(e))            
            return False
        return True 

    def save_regressor(self):
        random_integer = random.randint(1, 5000)
        if hasattr(self.regressor, 'model_'):
            self.regressor.model_.save('./network/saved_regressors/regressor'+str(random_integer)+'.keras')
            self.load_files()
        else:
            message('erro', 'O modelo não foi treinado. Execute o treinamento antes de salvar.')

    def load_files(self):
        directory = './network/saved_regressors'
        if directory:
            self.register.list_network.clear()
            try:
                for filename in os.listdir(directory):
                    self.register.list_network.addItem(filename)
            except Exception as e:
                self.register.list_network.addItem(f"Erro: {str(e)}")

    def delete_regressor(self):
        directory = './network/saved_regressors'
        selected_regressor = self.register.list_network.currentItem()
        index = self.register.list_network.row(selected_regressor)
        if selected_regressor is not None:
            file = selected_regressor.text()
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                self.register.list_network.takeItem(index)
                message('ok','Regressor '+file+' apagado com sucesso!')            
            else:
                message('erro', 'O regressor não existe.')
        else:
            message('erro', 'Nenhum regressor foi selecionado.')  

    def predict_productivity(self, data, saved_regressor):
        regressor = tf.keras.models.load_model(saved_regressor)
        prediction = regressor.predict(data)
        return prediction

    def measures_regressor(self):
        file = self.register.list_network.currentItem()
        if file is not None:
            saved_regressor = './network/saved_regressors/'+file.text()
            selected_regressor = tf.keras.models.load_model(saved_regressor)

            test = 100.00 - float(self.register.edt_training.text())

            x_training, x_test, y_training, y_test = train_test_split(self.fetch_input_attributes(), self.fetch_output_attributes(), test_size=(test/100))
            x_training_scaled = self.x_scaler.fit_transform(x_training)
            y_training_scaled = self.y_scaler.fit_transform(y_training.reshape(-1,1))
            x_test_scaled = self.x_scaler.fit_transform(x_test)
            y_test_scaled = self.y_scaler.fit_transform(y_test.reshape(-1,1))

            #x_test_prediction = np.array(x_test, dtype=np.float32)

            prediction = selected_regressor.predict(x_test_scaled).reshape(-1,1)
            prediction_inverse = self.y_scaler.inverse_transform(prediction)
            
            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S: '+file.text())
            self.register.edt_process.append('')
            self.register.edt_process.append('Atributos preditivos utilizados foram:') 
            self.register.edt_process.append('')
            self.register.edt_process.append('Altitude, sistema de plantio, temperatura mínima, temperatura máxima, chuva no vegetativo, chuva no reprodutivo, ph CaCl2, teor de argila, MO, CO, K-cmolc, Ca, Mg, Al, H Al, P, k-mg, S-SO4, B, Cu, Fe, Mn, Zn, adubação no pré-plantio de N, adubação no pré-plantio de P, adubação no pré-plantio de K, adubação no plantio de N, adubação no plantio de P, adubação no plantio de K, adubação no pós-plantio de N e adubação no pós-plantio de K.')
            self.register.edt_process.append('')
            self.register.edt_process.append('Dados de entrada para a realização do teste..................: '+ str(x_test))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: '+ str(prediction_inverse))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: '+ str(y_test))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: '+ str(prediction_inverse.mean()))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: '+ str(y_test.mean()))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: '+ str(mean_absolute_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Erro quadrático médio (Mean Squared Error-MSE)...............: '+ str(mean_squared_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: '+ str(root_mean_squared_error(y_test, prediction_inverse)))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: '+ str(r2_score(y_test, prediction_inverse)))
        else:
            message('erro', 'Nenhum regressor selecionado.') 

    def regression_pre_processing(self):
        data_base = self.base
        data_base2 = data_base
        data_base = data_base.drop('K_mg_analysis', axis=1)
        data_base = data_base.drop('planting_system_analysis', axis=1) 
        data_base = data_base.drop('minimum_temperature_analysis', axis=1)
        data_base = data_base.drop('maximum_temperature_analysis', axis=1)
        data_base = data_base.drop('rain_reproductive_analysis', axis=1)
        data_base = data_base.drop('CO_analysis', axis=1) 
        data_base = data_base.drop('Mg_analysis', axis=1)
        data_base = data_base.drop('Al_analysis', axis=1)
        data_base = data_base.drop('H_Al_analysis', axis=1)
        data_base = data_base.drop('S_SO4_analysis', axis=1)
        data_base = data_base.drop('B_analysis', axis=1)
        data_base = data_base.drop('Fe_analysis', axis=1)
        data_base = data_base.drop('Mn_analysis', axis=1)
        data_base = data_base.drop('clay_analysis', axis=1)
        data_base = data_base.drop('Ca_analysis', axis=1)
        data_base = data_base.drop('Zn_analysis', axis=1)
        data_base = data_base.drop('pre_sowing_N_analysis_kg', axis=1)
        data_base = data_base.drop('pre_sowing_P2O5_analysis_kg', axis=1)
        data_base = data_base.drop('pre_sowing_K2O_analysis_kg', axis=1)
        data_base = data_base.drop('seeding_P2O5_analysis_kg', axis=1)
        data_base = data_base.drop('seeding_K2O_analysis_kg', axis=1)
        data_base = data_base.drop('top_dressing_N_analysis_kg', axis=1)
        data_base = data_base.drop('top_dressing_K2O_analysis_kg', axis=1)

        x = data_base.drop(data_base.columns[1], axis=1).values
        for i in range(len(x)):
            for j in range(len(x[i])):
                if isinstance(x[i][j], str): 
                    try:
                        x[i][j] = float(x[i][j].replace(',', '.'))
                    except ValueError:
                        pass

        #x = np.array(x, dtype=np.float64)
        #x = np.log(x + 1e-10)            
                        
        y = data_base['average_productivity_analysis'].values
        for i in range(len(y)):
            if isinstance(y[i], str):
                try:
                    y[i] = float(y[i].replace(',', '.'))
                except ValueError:
                    pass
        #y = np.array(y, dtype=np.float64)        

        return data_base2, x, y

    def refression(self):
        data_base, x, y = self.regression_pre_processing()
        r = Regression(self.register, x, y)
        x_test, prediction, y_test, prediction_average, y_test_average, mae_test, mse_test, rmse_test, r2_test = r.create_regressor()
        self.register.edt_process.append('================================================================================================================================')
        self.register.edt_process.append('R E G R E S S Ã O    L I N E A R: ')
        self.register.edt_process.append('')
        self.register.edt_process.append('Atributos preditivos utilizados foram:') 
        self.register.edt_process.append('')
        self.register.edt_process.append('Altitude, chuva no perído vegetativo, pH, MO, k(cmolc), P, Cu e adubação de N no plantio.')
        self.register.edt_process.append('')
        self.register.edt_process.append('Dados de entrada para a realização do teste..................: ' + x_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: ' + prediction)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: ' + y_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: ' + prediction_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: ' + y_test_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: ' + mae_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro quadrático médio (Mean Squared Error-MSE)...............: ' + mse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ' + rmse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: ' + r2_test)

        #correlação das variaveis preditoras
        x = np.array(data_base)
        for i in range(len(x)):
            for j in range(len(x[i])):
                if isinstance(x[i][j], str): 
                    try:
                        x[i][j] = float(x[i][j].replace(',', '.'))
                    except ValueError:
                        pass
        
        label_encoder = LabelEncoder()
        x[:, 1] = label_encoder.fit_transform(x[:, 1])
        
        d = pd.DataFrame(x)
        d = d.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
        d.columns = ["Alt.",  # 0  'altitude_analysis'
                     "Sist.", # 1  'planting_system_analysis'
                     "Méd.",  # 2  'average_productivity_analysis'
                     "T Mín", # 3  'minimum_temperature_analysis'
                     "T Máx", # 4  'maximum_temperature_analysis'
                     "C V",   # 5  'rain_vegetative_analysis'
                     "C R",   # 6  'rain_reproductive_analysis'
                     "pH",    # 7  'ph_CaCl2_analysis'
                     "Arg",   # 8  'clay_analysis'
                     "MO",    # 9  'MO_analysis'
                     "CO",    # 10 'CO_analysis'
                     "K",     # 11 'K_cmolc_analysis'
                     "Ca",    # 12 'Ca_analysis'
                     "Mg",    # 13 'Mg_analysis'
                     "Al",    # 14 'Al_analysis'
                     "H-Al",  # 15 'H_Al_analysis'
                     "P",     # 16 'P_meh_analysis'
                     "k-mg",  # 17 'K_mg_analysis'
                     "S",     # 18 'S_SO4_analysis'
                     "B",     # 19 'B_analysis'
                     "Cu",    # 20 'Cu_analysis'
                     "Fe",    # 21 'Fe_analysis'
                     "Mn",    # 22 'Mn_analysis'
                     "Zn",    # 23 'Zn_analysis'
                     "Pre_N", # 24 'pre_sowing_N_analysis_kg'
                     "Pre_P", # 25 'pre_sowing_P2O5_analysis_kg'
                     "Pre_K", # 26 'pre_sowing_K2O_analysis_kg'
                     "Pla_N", # 27 'seeding_N_analysis_kg'
                     "Pla_P", # 28 'seeding_P2O5_analysis_kg'
                     "Pla_K", # 29 'seeding_K2O_analysis_kg'
                     "Pos_N", # 30 'top_dressing_N_analysis_kg'
                     "Pos_K"  # 31 'top_dressing_K2O_analysis_kg'
                     ]

        fig, ax = plt.subplots(figsize=(40, 40))
        heatmap = sns.heatmap(d.corr(),
                              annot = True,
                              fmt=".2f",
                              xticklabels = d.columns,
                              yticklabels=d.columns, 
                              annot_kws={"fontsize": 7, "va": "center", "ha": "center"},
                              cbar_kws={"shrink": .9},
                              linewidths=2,
                              linecolor='black')
    
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=7)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', fontsize=7)
    
        cbar = heatmap.collections[0].colorbar
        cbar.ax.tick_params(labelsize=8)

        plt.show()

        r=None

    def sv_pre_processing(self):
        data_base = self.base
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
        return data_base, x, y

    def sv(self):
        data_base, x, y = self.sv_pre_processing()
        svr = SupportVectors(self.register, x, y)
        x_test, prediction, y_test, prediction_average, y_test_average, mae_test, mse_test, rmse_test, r2_test = svr.create_regressor()
        self.register.edt_process.append('================================================================================================================================')
        self.register.edt_process.append('S V R  (Suporte à regressão vetorial): ')
        self.register.edt_process.append('')
        self.register.edt_process.append('Atributos preditivos utilizados foram:') 
        self.register.edt_process.append('')
        self.register.edt_process.append('Altitude, sistema de plantio, temperatura mínima, temperatura máxima, chuva no vegetativo, chuva no reprodutivo, ph CaCl2, teor de argila, MO, CO, K-cmolc, Ca, Mg, Al, H Al, P, k-mg, S-SO4, B, Cu, Fe, Mn, Zn, adubação no pré-plantio de N, adubação no pré-plantio de P, adubação no pré-plantio de K, adubação no plantio de N, adubação no plantio de P, adubação no plantio de K, adubação no pós-plantio de N e adubação no pós-plantio de K.')
        self.register.edt_process.append('')
        self.register.edt_process.append('Dados de entrada para a realização do teste..................: ' + x_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: ' + prediction)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: ' + y_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: ' + prediction_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: ' + y_test_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: ' + mae_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro quadrático médio (Mean Squared Error-MSE)...............: ' + mse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ' + rmse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: ' + r2_test)

    def random_forest_pre_processing(self):
        data_base = self.base
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
        return data_base, x, y

    def random_forest(self):
        data_base, x, y = self.random_forest_pre_processing()
        rf = RandomForest(self.register, x, y)
        x_test, prediction, y_test, prediction_average, y_test_average, mae_test, mse_test, rmse_test, r2_test = rf.create_regressor()
        self.register.edt_process.append('================================================================================================================================')
        self.register.edt_process.append('S V R  (Suporte à regressão vetorial): ')
        self.register.edt_process.append('')
        self.register.edt_process.append('Atributos preditivos utilizados foram:') 
        self.register.edt_process.append('')
        self.register.edt_process.append('Altitude, sistema de plantio, temperatura mínima, temperatura máxima, chuva no vegetativo, chuva no reprodutivo, ph CaCl2, teor de argila, MO, CO, K-cmolc, Ca, Mg, Al, H Al, P, k-mg, S-SO4, B, Cu, Fe, Mn, Zn, adubação no pré-plantio de N, adubação no pré-plantio de P, adubação no pré-plantio de K, adubação no plantio de N, adubação no plantio de P, adubação no plantio de K, adubação no pós-plantio de N e adubação no pós-plantio de K.')
        self.register.edt_process.append('')
        self.register.edt_process.append('Dados de entrada para a realização do teste..................: ' + x_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: ' + prediction)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: ' + y_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: ' + prediction_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: ' + y_test_average)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: ' + mae_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Erro quadrático médio (Mean Squared Error-MSE)...............: ' + mse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ' + rmse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: ' + r2_test)
