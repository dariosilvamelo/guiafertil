import os
import random
import time
from datetime import datetime

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scikeras
import tensorflow as tf
from PySide6.QtWidgets import QApplication
from scikeras.wrappers import KerasRegressor
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score,
                             root_mean_squared_error)
from sklearn.model_selection import (GridSearchCV, cross_val_predict,
                                     cross_val_score, train_test_split, KFold)
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.svm import SVR
from tensorflow.keras import backend as k
from tensorflow.keras.models import Sequential

from tools import message, validates_float


class Neural_Network():
    def __init__(self, analysis_panel):
        self.register = analysis_panel
        self.base = None
        self.x_scaler = None
        self.y_scaler = None
        self.regressor = None
        self.neural_network_structure = None

    def set_seed(self, seed_value=42):
        # Fix seeds for all sources of randomness
        random.seed(seed_value)
        np.random.seed(seed_value)
        tf.random.set_seed(seed_value)

    def enable_deterministic_operations(self):
        # Configuration for deterministic operations
        #os.environ['TF_DETERMINISTIC_OPS'] = '1'  
        tf.config.experimental.enable_op_determinism()

    def processing_data(self):
        self.register.analysis_data.export_data_csv()
        result = pd.read_csv('./csv/data.csv')

        #converting numeric values ​​in the format '0,00' to '0.00'
        for col in result.columns:
            if col != 'planting_system_analysis' and result[col].dtype == 'object':
                result[col] = result[col].str.replace(',', '.').astype(float)

        result = result.drop('ph_H2O_analysis', axis=1)
        result = result.drop('P_rem_analysis', axis=1)
        result = result.drop('Na_analysis', axis=1)
        result = result.drop('K_mg_analysis', axis=1)

        result = result.drop('Al_analysis', axis=1)
        result = result.drop('H_Al_analysis', axis=1)

        result['N'] = result['pre_sowing_N_analysis_kg'] + result['seeding_N_analysis_kg'] + result['top_dressing_N_analysis_kg']
        result['P2O5'] = result['pre_sowing_P2O5_analysis_kg'] + result['seeding_P2O5_analysis_kg'] + result['top_dressing_P2O5_analysis_kg']
        result['K2O'] = result['pre_sowing_K2O_analysis_kg'] + result['seeding_K2O_analysis_kg'] + result['top_dressing_K2O_analysis_kg']

        result = result.drop('pre_sowing_N_analysis_kg', axis=1)
        result = result.drop('pre_sowing_P2O5_analysis_kg', axis=1)
        result = result.drop('pre_sowing_K2O_analysis_kg', axis=1)

        result = result.drop('seeding_N_analysis_kg', axis=1)
        result = result.drop('seeding_P2O5_analysis_kg', axis=1)
        result = result.drop('seeding_K2O_analysis_kg', axis=1)

        result = result.drop('top_dressing_N_analysis_kg', axis=1)
        result = result.drop('top_dressing_P2O5_analysis_kg', axis=1)
        result = result.drop('top_dressing_K2O_analysis_kg', axis=1)

        co_average = result['CO_analysis'][result['CO_analysis'] > 0].mean()
        s_average = result['S_SO4_analysis'][result['S_SO4_analysis'] > 0].mean()

        result.loc[result['CO_analysis'] == 0, 'CO_analysis'] = co_average
        result.loc[result['S_SO4_analysis'] == 0, 'S_SO4_analysis'] = s_average

        return result

    def fetch_input_attributes(self, data):
        if data is not None:
            x = data.drop(data.columns[2], axis=1).values
            onehotencoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
            x = onehotencoder.fit_transform(x)
            """
                'CONVENCIONAL - IRRIGADO'	    1.0	 0.0  0.0  0.0
                'CONVENCIONAL - SEQUEIRO'	    0.0	 1.0  0.0  0.0
                'PLANTIO DIRETO - IRRIGADO'  	0.0	 0.0  1.0  0.0
                'PLANTIO DIRETO - SEQUEIRO'	    0.0	 0.0  0.0  1.0
            """
            return x
        else:
            return None

    def fetch_output_attributes(self, data):
        if data is not None:
            y = data['average_productivity_analysis'].values
            return y
        else:
            return None

    def create_neural_network(self):
        seed = int(self.register.edt_seed_neural_network.text())
        self.set_seed(seed)
        self.enable_deterministic_operations()
        k.clear_session()

        network = Sequential([
            tf.keras.layers.InputLayer(shape = (26,)),
            tf.keras.layers.Dense(units=30,
                                  activation='relu',
                                  kernel_initializer=tf.keras.initializers.RandomUniform(seed=seed),
                                  bias_initializer=tf.keras.initializers.Zeros()),
            tf.keras.layers.Dense(units=30,
                                  activation='relu',
                                  kernel_initializer=tf.keras.initializers.RandomUniform(seed=seed),
                                  bias_initializer=tf.keras.initializers.Zeros()),
            tf.keras.layers.Dense(units=1, activation='linear')])

        optimizer = tf.optimizers.Adam(learning_rate=validates_float(self.register.edt_learning_rate.text()))

        network.compile(optimizer=optimizer,
                        loss=tf.keras.losses.MeanAbsoluteError(),
                        metrics=[tf.keras.metrics.MeanAbsoluteError()])        
        return network

    def perform_training(self):
        if self.validate_parameters():
            self.base = self.processing_data()

            x = np.array(self.fetch_input_attributes(self.base), dtype=float)
            y = np.array(self.fetch_output_attributes(self.base), dtype=float)

            test = 100.00 - float(self.register.edt_training.text())

            x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=(test/100))

            self.x_scaler = StandardScaler()
            self.y_scaler = StandardScaler()

            x_training_scaled = self.x_scaler.fit_transform(x_training)
            y_training_scaled = self.y_scaler.fit_transform(y_training.reshape(-1, 1))
            x_test_scaled = self.x_scaler.transform(x_test)

            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S:')
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Processando o treinamento com '+str(100.00-test)+'(%) dos dados e '+str(test)+'(%) para testar'+'....')
            self.register.edt_process.append(' ')
            QApplication.processEvents()
            time.sleep(1)

            self.regressor = KerasRegressor(model=self.create_neural_network(), epochs=int(self.register.edt_epochs.text()), batch_size=int(self.register.edt_batch_size.text()))

            self.regressor.fit(x_training_scaled, y_training_scaled.ravel())

            prediction = self.regressor.predict(x_test_scaled).reshape(-1,1)
            prediction_inverse = self.y_scaler.inverse_transform(prediction)

            self.plot_scatter(y_test, prediction_inverse)

            prediction_average = str(prediction_inverse.mean())
            y_test_average = str(y_test.mean())
            mae_test = str(mean_absolute_error(y_test, prediction_inverse))
            rmse_test = str(root_mean_squared_error(y_test, prediction_inverse))
            r2_test = str(r2_score(y_test, prediction_inverse))
            return x_test, str(prediction_inverse), str(y_test), prediction_average, y_test_average, mae_test, rmse_test, r2_test

    '''
    def cross_validation(self):
        if self.validate_parameters():

            self.base = self.processing_data()
            x = np.array(self.fetch_input_attributes(self.base), dtype=float)
            y = np.array(self.fetch_output_attributes(self.base), dtype=float)

            self.x_scaler = StandardScaler()
            self.y_scaler = StandardScaler()

            x_training_scaled = self.x_scaler.fit_transform(x)
            y_training_scaled = self.y_scaler.fit_transform(y.reshape(-1, 1))

            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S:')
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Processando a Validação Cruzada....')
            self.register.edt_process.append(' ')
            QApplication.processEvents()
            time.sleep(1)

            self.create_neural_network()

            self.regressor = KerasRegressor(model=self.create_neural_network(),
                                            epochs=int(self.register.edt_epochs.text()),
                                            batch_size=int(self.register.edt_batch_size.text()))

            y_prediction_scaled = cross_val_predict(estimator=self.regressor,
                                                    X=x_training_scaled,
                                                    y=y_training_scaled.ravel(),
                                                    cv=int(self.register.edt_cv.text()))

            y_prediction_inverse = self.y_scaler.inverse_transform(y_prediction_scaled.reshape(-1, 1))
            mean_prediction = str(y_prediction_inverse.flatten().mean())
            mean_y = str(y.mean())
            mae = str(mean_absolute_error(y, y_prediction_inverse.flatten()))
            rmse = str(root_mean_squared_error(y, y_prediction_inverse.flatten()))
            std = str(np.std(y - y_prediction_inverse.flatten()))
            r2 = str(r2_score(y, y_prediction_inverse.flatten()))

            self.register.edt_process.append('Respostas esperadas com os dados de entrada..................: ' + str(y))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Previsões obtidas com os dados de entrada....................: ' + str(y_prediction_inverse.flatten()))
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das previsões obtidas com os dados de entrada..........: ' + mean_prediction)
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Média das respostas esperadas com os dados de entrada........: ' + mean_y)
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Erro absoluto médio (Mean Absolute Error - MAE)..............: ' + mae)
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ' + rmse)
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Desvio padrão................................................: ' + std)
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: ' + r2)
            self.register.edt_process.append(' ')
    '''
    def cross_validation(self):
        if self.validate_parameters():
            self.base = self.processing_data()
            x = np.array(self.fetch_input_attributes(self.base), dtype=float)
            y = np.array(self.fetch_output_attributes(self.base), dtype=float)

            self.x_scaler = StandardScaler()
            self.y_scaler = StandardScaler()

            x_scaled = self.x_scaler.fit_transform(x)
            y_scaled = self.y_scaler.fit_transform(y.reshape(-1, 1))

            kf = KFold(n_splits=int(self.register.edt_cv.text()), shuffle=True, random_state=42)
            mae_list = []
            rmse_list = []
            r2_list = []

            self.register.edt_process.append('================================================================================================================================')
            self.register.edt_process.append('R E D E S    N E U R A I S:')
            self.register.edt_process.append(' ')
            self.register.edt_process.append('Processando a Validação Cruzada....')
            self.register.edt_process.append(' ')
            QApplication.processEvents()
            time.sleep(1)

            for train_index, test_index in kf.split(x_scaled):
                x_train, x_test = x_scaled[train_index], x_scaled[test_index]
                y_train, y_test = y_scaled[train_index], y_scaled[test_index]

                # Criar e treinar a rede neural
                model = self.create_neural_network()
                model.fit(x_train, y_train, epochs=int(self.register.edt_epochs.text()), batch_size=int(self.register.edt_batch_size.text()))

                # Previsões
                predictions = model.predict(x_test)
                predictions_inverse = self.y_scaler.inverse_transform(predictions)

                # Calcular métricas
                mae = mean_absolute_error(y_test, predictions_inverse)
                rmse = np.sqrt(mean_squared_error(y_test, predictions_inverse))
                r2 = r2_score(y_test, predictions_inverse)

                mae_list.append(mae)
                rmse_list.append(rmse)
                r2_list.append(r2)

            # Média das métricas
            self.register.edt_process.append('Média dos resultados da Validação Cruzada:')
            self.register.edt_process.append('MAE: ' + str(np.mean(mae_list)))
            self.register.edt_process.append('RMSE: ' + str(np.mean(rmse_list)))
            self.register.edt_process.append('R²: ' + str(np.mean(r2_list)))
            self.register.edt_process.append(' ')

            #return np.mean(mae_list), np.mean(rmse_list), np.mean(r2_list)

    
    def neural_network(self):
        x_test, prediction, y_test, prediction_average, y_test_average, mae_test, rmse_test, r2_test = self.perform_training()
        x_test = str(np.array([[f"{float(j):.2f}" for j in i] for i in x_test]))
        self.register.edt_process.append('Resultados: ')
        self.register.edt_process.append('')
        self.register.edt_process.append('Atributos preditivos utilizados foram:')
        self.register.edt_process.append('')
        self.register.edt_process.append('Altitude, sistema de plantio, temperatura mínima, temperatura máxima, chuva no vegetativo, chuva no reprodutivo, pH em CaCl2, teor de argila, MO, CO, K, Ca, Mg, P, S, B, Cu, Fe, Mn, Zn, adubação de N, adubação de P2O5 e adubação de K2O.')
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
        self.register.edt_process.append('Raiz do erro quadrático médio (Root Mean Squared Error-RMSE).: ' + rmse_test)
        self.register.edt_process.append(' ')
        self.register.edt_process.append('Coeficiente de determinação R² (R-squared)...................: ' + r2_test)

    def save_model(self):
        if self.regressor is not None and self.x_scaler is not None and self.y_scaler is not None:
            now = datetime.now()
            n = now.strftime('%H%M%S')            
            if isinstance(self.regressor, SVR):
                joblib.dump(self.regressor, f'./model/svm/regressors/svm_regressor_{n}.pkl')
                joblib.dump(self.x_scaler, f'./model/svm/schedulers/x_scaler_{n}.pkl')
                joblib.dump(self.y_scaler, f'./model/svm/schedulers/y_scaler_{n}.pkl')
                message('ok',"O regressor SVR e seus escalonadores foram salvos com sucesso!.")
            elif isinstance(self.regressor, RandomForestRegressor):
                joblib.dump(self.regressor, f'./model/random_forest/regressors/random_forest_regressor_{n}.pkl')
                joblib.dump(self.x_scaler, f'./model/random_forest/schedulers/x_scaler_{n}.pkl')
                joblib.dump(self.y_scaler, f'./model/random_forest/schedulers/y_scaler_{n}.pkl')
                message('ok',"O regressor Random Forest e seus escalonadores foram salvos com sucesso!")
            elif isinstance(self.regressor, KerasRegressor):
                joblib.dump(self.regressor, f'./model/neural_network/regressors/network_regressor_{n}.pkl')
                joblib.dump(self.x_scaler, f'./model/neural_network/schedulers/x_scaler_{n}.pkl')
                joblib.dump(self.y_scaler, f'./model/neural_network/schedulers/y_scaler_{n}.pkl')
                message('ok',"O regressor da Rede Neural e seus escalonadores foram salvos com sucesso!.")
            elif isinstance(self.regressor, LinearRegression):
                joblib.dump(self.regressor, f'./model/linear_regression/regressors/linear_regression_regressor_{n}.pkl')
                joblib.dump(self.x_scaler, f'./model/linear_regression/schedulers/x_scaler_{n}.pkl')
                joblib.dump(self.y_scaler, f'./model/linear_regression/schedulers/y_scaler_{n}.pkl')
                message('ok',"O regressor da Regressão Linear e seus escalonadores foram salvos com sucesso!.")
            else:
                message('ok',"Regressor desconhecido.")
            self.base = None
            self.x_scaler = None
            self.y_scaler = None
            self.regressor = None
            self.load_files()   
        else:
            message('erro', 'Erro: O modelo ou os escalonadores ainda não foram configurados.')

    def load_files(self):
        directory = './model/neural_network/regressors'
        if directory:
            self.register.list_network.clear()
            try:
                for filename in os.listdir(directory):
                    self.register.list_network.addItem(filename)
            except Exception as e:
                self.register.list_network.addItem(f"Erro: {str(e)}")

    def validate_parameters(self):
        try:
            epochs = int(self.register.edt_epochs.text())
            batch_size = int(self.register.edt_batch_size.text())
            training = int(self.register.edt_training.text())
            cv = int(self.register.edt_cv.text())
            learning_rate = float(self.register.edt_learning_rate.text().replace(',', '.'))
        except Exception as e:
            message('erro', 'As épocas, o batch size, o percentual de dados para treinamento, o n° de Folds e a taxa de aprendizagem devem ser preenchidos!' + str(e))
            return False
        return True 

    def plot_scatter(self, y_test, prediction_inverse):
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, prediction_inverse, color='blue', alpha=0.6, label='Predicted vs Actual')
        plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Ideal Fit')
        plt.title('Gráfico de Dispersão: Valores Reais vs Previstos')
        plt.xlabel('Valores Reais')
        plt.ylabel('Valores Previstos')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.show()
