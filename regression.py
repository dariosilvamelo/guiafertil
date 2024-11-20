import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             root_mean_squared_error)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from yellowbrick.target import FeatureCorrelation


class Regression():
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

        regressor = LinearRegression()
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
        regressor = LinearRegression()
        regressor.fit(x_training_scaled, y_training_scaled.ravel())
        prediction = regressor.predict(data_scaled).reshape(-1,1)
        prediction_inverse = self.y_scaler.inverse_transform(prediction)
        return prediction_inverse

if (__name__ == '__main__'):
    data_base = pd.read_csv('./network/network.csv')
    data_base = data_base.drop('ph_H2O_analysis', axis=1) 
    data_base = data_base.drop('planting_system_analysis', axis=1) 
    #apos 1ª avaliação
    data_base = data_base.drop('CO_analysis', axis=1) 
    data_base = data_base.drop('P_rem_analysis', axis=1) 
    data_base = data_base.drop('Na_analysis', axis=1) 
    data_base = data_base.drop('K_mg_analysis', axis=1)
    data_base = data_base.drop('pre_sowing_N_analysis_kg', axis=1)
    data_base = data_base.drop('top_dressing_P2O5_analysis_kg', axis=1) 
    data_base2 = data_base
    #apos 2ª avaliação:
    data_base = data_base.drop('minimum_temperature_analysis', axis=1)
    data_base = data_base.drop('maximum_temperature_analysis', axis=1)
    data_base = data_base.drop('rain_reproductive_analysis', axis=1)
    data_base = data_base.drop('Mg_analysis', axis=1)
    data_base = data_base.drop('Al_analysis', axis=1)
    data_base = data_base.drop('H_Al_analysis', axis=1)
    data_base = data_base.drop('S_SO4_analysis', axis=1)
    data_base = data_base.drop('B_analysis', axis=1)
    data_base = data_base.drop('Fe_analysis', axis=1)
    data_base = data_base.drop('Mn_analysis', axis=1)
    data_base = data_base.drop('pre_sowing_P2O5_analysis_kg', axis=1)
    data_base = data_base.drop('pre_sowing_K2O_analysis_kg', axis=1)
    data_base = data_base.drop('top_dressing_K2O_analysis_kg', axis=1)
    #apos 3ª avaliação:
    data_base = data_base.drop('clay_analysis', axis=1)
    data_base = data_base.drop('Ca_analysis', axis=1)
    data_base = data_base.drop('Zn_analysis', axis=1)
    data_base = data_base.drop('seeding_P2O5_analysis_kg', axis=1)
    data_base = data_base.drop('seeding_K2O_analysis_kg', axis=1)
    data_base = data_base.drop('top_dressing_N_analysis_kg', axis=1)

    print(data_base.columns)

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

    plt.hist(y)
    plt.show()

    f, ax = plt.subplots(3,3)
    ax[0, 0].hist(x[0]) # 0 'altitude_analysis'
    ax[0, 1].hist(x[1]) # 1 'rain_vegetative_analysis'
    ax[0, 2].hist(x[2]) # 2 'ph_CaCl2_analysis'
    ax[1, 0].hist(x[3]) # 3 'MO_analysis'
    ax[1, 1].hist(x[4]) # 4 'K_cmolc_analysis'
    ax[1, 2].hist(x[5]) # 5 'P_meh_analysis'
    ax[2, 0].hist(x[6]) # 6 'Cu_analysis'
    ax[2, 1].hist(x[7]) # 7 'seeding_N_analysis_kg'
    plt.show()

    """
    f, ax = plt.subplots(6,6)
    ax[0, 0].hist(x[0])        #  0  'altitude_analysis'
    ax[0, 1].hist(x[1])        #  1  'minimum_temperature_analysis'
    ax[0, 2].hist(x[2])        #  2  'maximum_temperature_analysis'
    ax[0, 3].hist(x[3])        #  3  'rain_vegetative_analysis'
    ax[0, 4].hist(x[4])        #  4  'rain_reproductive_analysis'
    ax[0, 5].hist(x[5])        #  5  'ph_CaCl2_analysis'
    ax[1, 0].hist(x[6])        #  6  'clay_analysis'
    ax[1, 1].hist(x[7])        #  7  'MO_analysis'
    ax[1, 2].hist(x[9])        #  8  'K_cmolc_analysis'
    ax[1, 3].hist(x[10])       #  9  'Ca_analysis'
    ax[1, 4].hist(x[11])       #  10 'Mg_analysis'
    ax[1, 5].hist(x[12])       #  11 'Al_analysis'
    ax[2, 0].hist(x[13])       #  12 'H_Al_analysis'
    ax[2, 1].hist(x[14])       #  13 'P_meh_analysis'
    ax[2, 2].hist(x[18])       #  14 'S_SO4_analysis'
    ax[2, 3].hist(x[19])       #  15 'B_analysis'
    ax[2, 4].hist(x[20])       #  16 'Cu_analysis'
    ax[2, 5].hist(x[21])       #  17 'Fe_analysis'
    ax[3, 0].hist(x[22])       #  18 'Mn_analysis'
    ax[3, 1].hist(x[23])       #  19 'Zn_analysis'
    ax[3, 2].hist(x[24])       #  20 'pre_sowing_P2O5_analysis_kg'
    ax[3, 3].hist(x[25])       #  21 'pre_sowing_K2O_analysis_kg'
    ax[3, 4].hist(x[26])       #  22 'seeding_N_analysis_kg'
    ax[3, 5].hist(x[27])       #  23 'seeding_P2O5_analysis_kg'
    ax[4, 0].hist(x[28])       #  24 'seeding_K2O_analysis_kg'
    ax[4, 1].hist(x[29])       #  25 'top_dressing_N_analysis_kg'
    ax[4, 2].hist(x[30])       #  26 'top_dressing_K2O_analysis_kg'
    plt.show()
    """   
    lr = Regression(None, x, y)
    (x_test,
     prediction,
     y_test,
     prediction_average,
     y_test_average,
     mae_test,
     mse_test,
     rmse_test,
     r2_test) = lr.create_regressor()

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

    #correlação das variaveis preditoras
    grafico = FeatureCorrelation()
    grafico.fit(np.asarray(lr.x, dtype=np.float64), np.asarray(lr.y, dtype=np.float64))
    grafico.show()

    #correlação das variaveis preditoras
    x = np.array(data_base2)
    for i in range(len(x)):
        for j in range(len(x[i])):
            if isinstance(x[i][j], str): 
                try:
                        x[i][j] = float(x[i][j].replace(',', '.'))
                except ValueError:
                    pass
    d = pd.DataFrame(x)
    d = d.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]]
    d.columns = ["Alt.",  # 0  'altitude_analysis'
                 "Méd.",  # 1  'average_productivity_analysis'
                 "T Mín", # 2  'minimum_temperature_analysis'
                 "T Máx", # 3  'maximum_temperature_analysis'
                 "C V",   # 4  'rain_vegetative_analysis'
                 "C R",   # 5  'rain_reproductive_analysis'
                 "pH",    # 6  'ph_CaCl2_analysis'
                 "Arg",   # 7  'clay_analysis'
                 "MO",    # 8  'MO_analysis'
                 "K",     # 9  'K_cmolc_analysis'
                 "Ca",    # 10 'Ca_analysis'
                 "Mg",    # 11 'Mg_analysis'
                 "Al",    # 12 'Al_analysis'
                 "H-Al",  # 13 'H_Al_analysis'
                 "P",     # 14 'P_meh_analysis'
                 "S",     # 15 'S_SO4_analysis'
                 "B",     # 16 'B_analysis'
                 "Cu",    # 17 'Cu_analysis'
                 "Fe",    # 18 'Fe_analysis'
                 "Mn",    # 19 'Mn_analysis'
                 "Zn",    # 20 'Zn_analysis'
                 "Pre_P", # 21 'pre_sowing_P2O5_analysis_kg'
                 "Pre_K", # 22 'pre_sowing_K2O_analysis_kg'
                 "Pla_N", # 23 'seeding_N_analysis_kg'
                 "Pla_P", # 24 'seeding_P2O5_analysis_kg'
                 "Pla_K", # 25 'seeding_K2O_analysis_kg'
                 "Pos_N", # 26 'top_dressing_N_analysis_kg'
                 "Pos_K"  # 27 'top_dressing_K2O_analysis_kg'
                 ]

    fig, ax = plt.subplots(figsize=(25, 25))
    heatmap = sns.heatmap(d.corr(),
                          annot = True,
                          xticklabels = d.columns,
                          yticklabels = d.columns, 
                          annot_kws = {"fontsize": 7},
                          cbar_kws={"shrink": .7},
                          linewidths=1,
                          linecolor='black'
                          )
    
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=7)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', fontsize=7)
    
    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=8)

    plt.show()
