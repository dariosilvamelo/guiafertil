import os
import re
import sys

from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from sklearn.model_selection import GridSearchCV

import constants as c
from analysis_functions import Analysis
from bean_technology import BeanTechnology
from data_base_analysis import DataBaseAnalysis
from data_base_producer import DataBaseProducer
from data_base_user import DataBaseUser
from general_consultation import General_consultation
from guia_fertil_ui import Ui_win_guia_fertil
from limestone_plaster_soy import LimestonePlasterSoy
from login import Login
from neural_network_functions import Neural_Network
from npk_wheat import NpkWheat
from predict_productivity import Predict_Productivity
from producer_functions import Producer
from random_forest import RandomForest
from regression import Regression
from succession_planting import SuccessionPlanting
from support_vectors import SupportVectors
from tools import format_value, message, numeric_field, validates_float
from user_functions import User


class GuiaFertil(QMainWindow, Ui_win_guia_fertil):

    def __init__(self):
        super(GuiaFertil, self).__init__()
        self.setupUi(self)
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()
        self.code_user = 0
        self.name_user = ''

        self.log = Login()
        self.log.btn_login.clicked.connect(self.authentication)

        self.producer_data = DataBaseProducer(c.DATABASE_ADDRESS)
        self.user_data = DataBaseUser(c.DATABASE_ADDRESS)
        self.analysis_data = DataBaseAnalysis(c.DATABASE_ADDRESS)

        self.producer = Producer(self)
        self.user = User(self)
        self.analysis = Analysis(self)
        self.neural_network = Neural_Network(self)
        self.support_vectors = SupportVectors(self)
        self.random_forest = RandomForest(self)
        self.linear_regression = Regression(self)
        self.general_consultation = General_consultation(c.DATABASE_ADDRESS)
        self.bean_technology = BeanTechnology()
        self.succession_planting = SuccessionPlanting()
        self.npk_wheat = NpkWheat()
        self.limestone_plaster_soy = LimestonePlasterSoy()
        self.model_predictions = Predict_Productivity()

        # events: main menu
        self.btn_home.clicked.connect(self.animation_menu)
        self.btn_menu_home.clicked.connect(
            lambda: self.stk_pag.setCurrentWidget(self.pag_home))
        self.btn_menu_user.clicked.connect(lambda: self.open_user_window())
        self.btn_menu_producer.clicked.connect(
            lambda: self.open_producer_window())
        self.btn_menu_analysis.clicked.connect(
            lambda: self.open_analysis_window())
        self.btn_menu_about.clicked.connect(
            lambda: self.stk_pag.setCurrentWidget(self.pag_about))
        self.btn_menu_neural_network.clicked.connect(
            lambda: self.open_neural_network_window())

        # capture where the focus was last
        self.last_focused_widget = None
        self.list_network.focusInEvent = self.capture_focus(self.list_network)
        self.list_linear_regression.focusInEvent = self.capture_focus(
            self.list_linear_regression)
        self.list_random_forest.focusInEvent = self.capture_focus(
            self.list_random_forest)
        self.list_svm.focusInEvent = self.capture_focus(self.list_svm)

        # exploratory analysis
        self.btn_SVR.clicked.connect(lambda: self.support_vectors.sv())
        self.btn_save_regressor_SVM.clicked.connect(
            lambda: self.support_vectors.save_model())
        self.btn_random_forest.clicked.connect(
            lambda: self.random_forest.random_forest())
        self.btn_save_regressor_RF.clicked.connect(
            lambda: self.random_forest.save_model())
        self.btn_linear_regression.clicked.connect(
            lambda: self.linear_regression.linear_regression())
        self.btn_save_regressor_RL.clicked.connect(
            lambda: self.linear_regression.save_model())
        self.btn_neural_network.clicked.connect(
            lambda: self.neural_network.neural_network())
        self.btn_save_regressor.clicked.connect(
            lambda: self.neural_network.save_model())
        self.btn_cross_validation_neural_network.clicked.connect(
            lambda: self.neural_network.cross_validation())
        self.btn_cross_validation_linear_regression.clicked.connect(
            lambda: self.linear_regression.cross_validation())
        self.btn_cross_validation_SVR.clicked.connect(
            lambda: self.support_vectors.cross_validation())
        self.btn_cross_validation_random_forest.clicked.connect(
            lambda: self.random_forest.cross_validation())
        self.btr_delete_regressor.clicked.connect(
            lambda: self.delete_regressor())
        self.btn_correlation_between_attributes.clicked.connect(
            lambda: self.correlation_between_attributes())

        # events: producer registration
        self.btn_insert_producer.clicked.connect(
            lambda: self.producer.insert_new_producer())
        self.btn_update_producer.clicked.connect(
            lambda: self.producer.update_changes_producer())
        self.btn_cancelar_producer.clicked.connect(
            lambda: self.producer.cancel_edit_producer())
        self.btn_save_producer.clicked.connect(
            lambda: self.producer.save_new_producer(self.code_user))
        self.btn_save_change_producer.clicked.connect(
            lambda: self.producer.save_changes_producer(self.code_user))
        self.btn_delete_producer.clicked.connect(
            lambda: self.producer.delete_record_producer())
        self.btn_excel_producer.clicked.connect(
            lambda: self.producer.export_excel_producer())
        self.btn_pdf_report_producer.clicked.connect(
            lambda: self.producer.report_pdf_producer())
        self.btn_search_producer.clicked.connect(
            lambda: self.producer.consult_producer())
        self.edt_query_producer.textChanged.connect(
            lambda: self.producer.consult_producer())
        self.edt_cpf_cnpj_producer.editingFinished.connect(
            lambda: self.producer.cpf_cnpj())
        self.table_grid_producer.currentItemChanged.connect(
            lambda: self.producer.dataset_producer())

        # events: user registration
        self.btn_insert_user.clicked.connect(
            lambda: self.user.insert_new_user())
        self.btn_update_user.clicked.connect(
            lambda: self.user.update_changes_user())
        self.btn_cancelar_user.clicked.connect(
            lambda: self.user.cancel_edit_user())
        self.btn_save_user.clicked.connect(lambda: self.user.save_new_user())
        self.btn_save_change_user.clicked.connect(
            lambda: self.user.save_changes_user())
        self.btn_delete_user.clicked.connect(
            lambda: self.user.delete_record_user())
        self.btn_excel_user.clicked.connect(
            lambda: self.user.export_excel_user())
        self.btn_pdf_report_user.clicked.connect(
            lambda: self.user.report_pdf_user())
        self.btn_search_user.clicked.connect(lambda: self.user.consult_user())
        self.edt_query_user.textChanged.connect(
            lambda: self.user.consult_user())
        self.edt_cpf_user.editingFinished.connect(lambda: self.user.cpf_cnpj())
        self.table_grid_user.currentItemChanged.connect(
            lambda: self.user.dataset_user())

        # events: analysis registration
        self.btn_insert_analysis.clicked.connect(
            lambda: self.analysis.insert_new_analysis())
        self.btn_update_analysis.clicked.connect(
            lambda: self.analysis.update_changes_analysis())
        self.btn_consult_analysis.clicked.connect(
            lambda: self.analysis.consult_producer())
        self.btn_cancelar_analysis.clicked.connect(
            lambda: self.analysis.cancel_edit_analysis())
        self.btn_save_analysis.clicked.connect(
            lambda: self.analysis.save_new_analysis(self.code_user))
        self.btn_save_change_analysis.clicked.connect(
            lambda: self.analysis.save_changes_analysis(self.code_user))
        self.btn_delete_analysis.clicked.connect(
            lambda: self.analysis.delete_record_analysis())
        self.btn_excel_analysis.clicked.connect(
            lambda: self.analysis.export_excel_analysis())
        self.btn_pdf_report_analysis.clicked.connect(
            lambda: self.analysis.report_pdf_analysis())
        self.btn_search_analysis.clicked.connect(
            lambda: self.analysis.consult_analysis())
        self.btn_Interpretation_analysis.clicked.connect(
            lambda: self.analysis.run_interpretation())
        self.btn_productivity_prediction.clicked.connect(
            lambda: self.predict_productivity())
        self.edt_code_producer.editingFinished.connect(
            lambda: self.analysis.consult_producer_code())
        self.edt_query_analysis.textChanged.connect(
            lambda: self.analysis.consult_analysis())
        self.table_grid_analysis.currentItemChanged.connect(
            lambda: self.analysis.dataset_analysis())

       # calculate bases
        self.edt_K_cmolc_analysis.textChanged.connect(
            lambda: self.analysis.calculate_bases())
        self.edt_Ca_analysis.textChanged.connect(
            lambda: self.analysis.calculate_bases())
        self.edt_Mg_analysis.textChanged.connect(
            lambda: self.analysis.calculate_bases())
        self.edt_Al_analysis.textChanged.connect(
            lambda: self.analysis.calculate_bases())
        self.edt_T_analysis.textChanged.connect(
            lambda: self.analysis.calculate_bases())

       # calculate the npk quantity according to the type of fertilizer and dosage
        self.edt_pre_sowing_fertilizer_analysis.textChanged.connect(lambda: self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(
        ), self.edt_pre_sowing_N_analysis.text(), self.edt_pre_sowing_P2O5_analysis.text(), self.edt_pre_sowing_K2O_analysis.text(), 'pre_sowing'))
        self.edt_pre_sowing_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(
        ), self.edt_pre_sowing_N_analysis.text(), self.edt_pre_sowing_P2O5_analysis.text(), self.edt_pre_sowing_K2O_analysis.text(), 'pre_sowing'))
        self.edt_pre_sowing_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(
        ), self.edt_pre_sowing_N_analysis.text(), self.edt_pre_sowing_P2O5_analysis.text(), self.edt_pre_sowing_K2O_analysis.text(), 'pre_sowing'))
        self.edt_pre_sowing_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(
        ), self.edt_pre_sowing_N_analysis.text(), self.edt_pre_sowing_P2O5_analysis.text(), self.edt_pre_sowing_K2O_analysis.text(), 'pre_sowing'))
        self.edt_planting_fertilizer_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(
        ), self.edt_planting_fertilizer_N_analysis.text(), self.edt_planting_fertilizer_P2O5_analysis.text(), self.edt_planting_fertilizer_K2O_analysis.text(), 'planting'))
        self.edt_planting_fertilizer_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(
        ), self.edt_planting_fertilizer_N_analysis.text(), self.edt_planting_fertilizer_P2O5_analysis.text(), self.edt_planting_fertilizer_K2O_analysis.text(), 'planting'))
        self.edt_planting_fertilizer_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(
        ), self.edt_planting_fertilizer_N_analysis.text(), self.edt_planting_fertilizer_P2O5_analysis.text(), self.edt_planting_fertilizer_K2O_analysis.text(), 'planting'))
        self.edt_planting_fertilizer_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(
        ), self.edt_planting_fertilizer_N_analysis.text(), self.edt_planting_fertilizer_P2O5_analysis.text(), self.edt_planting_fertilizer_K2O_analysis.text(), 'planting'))
        self.edt_top_dressing_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(
        ), self.edt_top_dressing_N_analysis.text(), self.edt_top_dressing_P2O5_analysis.text(), self.edt_top_dressing_K2O_analysis.text(), 'top_dressing'))
        self.edt_top_dressing_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(
        ), self.edt_top_dressing_N_analysis.text(), self.edt_top_dressing_P2O5_analysis.text(), self.edt_top_dressing_K2O_analysis.text(), 'top_dressing'))
        self.edt_top_dressing_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(
        ), self.edt_top_dressing_N_analysis.text(), self.edt_top_dressing_P2O5_analysis.text(), self.edt_top_dressing_K2O_analysis.text(), 'top_dressing'))
        self.edt_top_dressing_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(
        ), self.edt_top_dressing_N_analysis.text(), self.edt_top_dressing_P2O5_analysis.text(), self.edt_top_dressing_K2O_analysis.text(), 'top_dressing'))

        self.edt_micro_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_zn_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_b_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_cu_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_mn_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_mo_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_co_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_ca_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))
        self.edt_micro_s_analysis.textChanged.connect(lambda: self.analysis.micro_calculation(self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(
        ), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text()))

        # configuring numeric fields in the Neural_Network
        self.edt_epochs.textChanged.connect(
            lambda: numeric_field(self.edt_epochs))
        self.edt_batch_size.textChanged.connect(
            lambda: numeric_field(self.edt_batch_size))
        self.edt_training.textChanged.connect(
            lambda: numeric_field(self.edt_training))
        self.edt_cv.textChanged.connect(lambda: numeric_field(self.edt_cv))
        self.edt_degree.textChanged.connect(
            lambda: numeric_field(self.edt_degree))
        self.edt_n_tree.textChanged.connect(
            lambda: numeric_field(self.edt_n_tree))
        self.edt_learning_rate.textChanged.connect(
            lambda: numeric_field(self.edt_learning_rate))
        self.edt_seed_neural_network.textChanged.connect(
            lambda: numeric_field(self.edt_seed_neural_network))
        self.edt_seed_linear_regression.textChanged.connect(
            lambda: numeric_field(self.edt_seed_linear_regression))
        self.edt_seed_SVR.textChanged.connect(
            lambda: numeric_field(self.edt_seed_SVR))
        self.edt_seed_random_forest.textChanged.connect(
            lambda: numeric_field(self.edt_seed_random_forest))

        # configuring numeric fields in the analysis registration
        self.edt_average_productivity_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_average_productivity_analysis))
        self.edt_area_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_area_analysis))
        self.edt_rain_vegetative_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_rain_vegetative_analysis))
        self.edt_rain_reproductive_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_rain_reproductive_analysis))
        self.edt_maximum_temperature_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_maximum_temperature_analysis))
        self.edt_minimum_temperature_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_minimum_temperature_analysis))
        self.edt_initial_depth_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_initial_depth_analysis))
        self.edt_final_depth_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_final_depth_analysis))
        self.edt_ph_H2O_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_ph_H2O_analysis))
        self.edt_ph_CaCl2_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_ph_CaCl2_analysis))
        self.edt_clay_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_clay_analysis))
        self.edt_K_cmolc_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_K_cmolc_analysis))
        self.edt_Ca_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Ca_analysis))
        self.edt_Mg_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Mg_analysis))
        self.edt_Al_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Al_analysis))
        self.edt_H_Al_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_H_Al_analysis))
        self.edt_SB_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_SB_analysis))
        self.edt_t_effective_CTC_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_t_effective_CTC_analysis))
        self.edt_T_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_T_analysis))
        self.edt_V_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_V_analysis))
        self.edt_m_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_m_analysis))
        self.edt_MO_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_MO_analysis))
        self.edt_CO_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_CO_analysis))
        self.edt_P_meh_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_P_meh_analysis))
        self.edt_P_rem_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_P_rem_analysis))
        self.edt_Na_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Na_analysis))
        self.edt_K_mg_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_K_mg_analysis))
        self.edt_S_SO4_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_S_SO4_analysis))
        self.edt_B_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_B_analysis))
        self.edt_Cu_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Cu_analysis))
        self.edt_Fe_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Fe_analysis))
        self.edt_Mn_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Mn_analysis))
        self.edt_Zn_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_Zn_analysis))
        self.edt_limestone_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_limestone_analysis))
        self.edt_plaster_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_plaster_analysis))
        self.edt_pre_sowing_fertilizer_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_fertilizer_analysis))
        self.edt_pre_sowing_N_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_N_analysis))
        self.edt_pre_sowing_P2O5_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_P2O5_analysis))
        self.edt_pre_sowing_K2O_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_K2O_analysis))
        self.edt_pre_sowing_N_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_N_analysis_KG))
        self.edt_pre_sowing_P2O5_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_P2O5_analysis_KG))
        self.edt_pre_sowing_K2O_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_pre_sowing_K2O_analysis_KG))
        self.edt_planting_fertilizer_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_analysis))
        self.edt_planting_fertilizer_N_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_N_analysis))
        self.edt_planting_fertilizer_P2O5_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_P2O5_analysis))
        self.edt_planting_fertilizer_K2O_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_K2O_analysis))
        self.edt_planting_fertilizer_N_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_N_analysis_KG))
        self.edt_planting_fertilizer_P2O5_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_P2O5_analysis_KG))
        self.edt_planting_fertilizer_K2O_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_planting_fertilizer_K2O_analysis_KG))
        self.edt_top_dressing_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_analysis))
        self.edt_top_dressing_N_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_N_analysis))
        self.edt_top_dressing_P2O5_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_P2O5_analysis))
        self.edt_top_dressing_K2O_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_K2O_analysis))
        self.edt_top_dressing_N_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_N_analysis_KG))
        self.edt_top_dressing_P2O5_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_P2O5_analysis_KG))
        self.edt_top_dressing_K2O_analysis_KG.textChanged.connect(
            lambda: numeric_field(self.edt_top_dressing_K2O_analysis_KG))
        self.edt_micro_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_analysis))
        self.edt_micro_zn_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_zn_analysis))
        self.edt_micro_b_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_b_analysis))
        self.edt_micro_cu_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_cu_analysis))
        self.edt_micro_mn_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_mn_analysis))
        self.edt_micro_mo_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_mo_analysis))
        self.edt_micro_co_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_co_analysis))
        self.edt_micro_ca_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_ca_analysis))
        self.edt_micro_s_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_micro_s_analysis))
        self.edt_micro_zn_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_zn_analysis_kg))
        self.edt_micro_b_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_b_analysis_kg))
        self.edt_micro_cu_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_cu_analysis_kg))
        self.edt_micro_mn_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_mn_analysis_kg))
        self.edt_micro_mo_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_mo_analysis_kg))
        self.edt_micro_co_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_co_analysis_kg))
        self.edt_micro_ca_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_ca_analysis_kg))
        self.edt_micro_s_analysis_kg.textChanged.connect(
            lambda: numeric_field(self.edt_micro_s_analysis_kg))
        self.edt_prnt_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_prnt_analysis))
        self.edt_tca_analysis.textChanged.connect(
            lambda: numeric_field(self.edt_tca_analysis))
        self.edt_average_productivity_analysis.editingFinished.connect(
            lambda: format_value(self.edt_average_productivity_analysis))
        self.edt_altitude_analysis.editingFinished.connect(
            lambda: format_value(self.edt_altitude_analysis))
        self.edt_area_analysis.editingFinished.connect(
            lambda: format_value(self.edt_area_analysis))
        self.edt_rain_vegetative_analysis.editingFinished.connect(
            lambda: format_value(self.edt_rain_vegetative_analysis))
        self.edt_rain_reproductive_analysis.editingFinished.connect(
            lambda: format_value(self.edt_rain_reproductive_analysis))
        self.edt_maximum_temperature_analysis.editingFinished.connect(
            lambda: format_value(self.edt_maximum_temperature_analysis))
        self.edt_minimum_temperature_analysis.editingFinished.connect(
            lambda: format_value(self.edt_minimum_temperature_analysis))
        self.edt_initial_depth_analysis.editingFinished.connect(
            lambda: format_value(self.edt_initial_depth_analysis))
        self.edt_final_depth_analysis.editingFinished.connect(
            lambda: format_value(self.edt_final_depth_analysis))
        self.edt_ph_H2O_analysis.editingFinished.connect(
            lambda: format_value(self.edt_ph_H2O_analysis))
        self.edt_ph_CaCl2_analysis.editingFinished.connect(
            lambda: format_value(self.edt_ph_CaCl2_analysis))
        self.edt_clay_analysis.editingFinished.connect(
            lambda: format_value(self.edt_clay_analysis))
        self.edt_K_cmolc_analysis.editingFinished.connect(
            lambda: format_value(self.edt_K_cmolc_analysis))
        self.edt_Ca_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Ca_analysis))
        self.edt_Mg_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Mg_analysis))
        self.edt_Al_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Al_analysis))
        self.edt_H_Al_analysis.editingFinished.connect(
            lambda: format_value(self.edt_H_Al_analysis))
        self.edt_SB_analysis.editingFinished.connect(
            lambda: format_value(self.edt_SB_analysis))
        self.edt_t_effective_CTC_analysis.editingFinished.connect(
            lambda: format_value(self.edt_t_effective_CTC_analysis))
        self.edt_T_analysis.editingFinished.connect(
            lambda: format_value(self.edt_T_analysis))
        self.edt_V_analysis.editingFinished.connect(
            lambda: format_value(self.edt_V_analysis))
        self.edt_m_analysis.editingFinished.connect(
            lambda: format_value(self.edt_m_analysis))
        self.edt_MO_analysis.editingFinished.connect(
            lambda: format_value(self.edt_MO_analysis))
        self.edt_CO_analysis.editingFinished.connect(
            lambda: format_value(self.edt_CO_analysis))
        self.edt_P_meh_analysis.editingFinished.connect(
            lambda: format_value(self.edt_P_meh_analysis))
        self.edt_P_rem_analysis.editingFinished.connect(
            lambda: format_value(self.edt_P_rem_analysis))
        self.edt_Na_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Na_analysis))
        self.edt_K_mg_analysis .editingFinished.connect(
            lambda: format_value(self.edt_K_mg_analysis))
        self.edt_S_SO4_analysis.editingFinished.connect(
            lambda: format_value(self.edt_S_SO4_analysis))
        self.edt_B_analysis.editingFinished.connect(
            lambda: format_value(self.edt_B_analysis))
        self.edt_Cu_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Cu_analysis))
        self.edt_Fe_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Fe_analysis))
        self.edt_Mn_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Mn_analysis))
        self.edt_Zn_analysis.editingFinished.connect(
            lambda: format_value(self.edt_Zn_analysis))
        self.edt_limestone_analysis.editingFinished.connect(
            lambda: format_value(self.edt_limestone_analysis))
        self.edt_plaster_analysis.editingFinished.connect(
            lambda: format_value(self.edt_plaster_analysis))
        self.edt_pre_sowing_fertilizer_analysis.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_fertilizer_analysis))
        self.edt_pre_sowing_N_analysis.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_N_analysis))
        self.edt_pre_sowing_P2O5_analysis.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_P2O5_analysis))
        self.edt_pre_sowing_K2O_analysis.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_K2O_analysis))
        self.edt_pre_sowing_N_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_N_analysis_KG))
        self.edt_pre_sowing_P2O5_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_P2O5_analysis_KG))
        self.edt_pre_sowing_K2O_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_pre_sowing_K2O_analysis_KG))
        self.edt_planting_fertilizer_analysis.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_analysis))
        self.edt_planting_fertilizer_N_analysis.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_N_analysis))
        self.edt_planting_fertilizer_P2O5_analysis.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_P2O5_analysis))
        self.edt_planting_fertilizer_K2O_analysis.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_K2O_analysis))
        self.edt_planting_fertilizer_N_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_N_analysis_KG))
        self.edt_planting_fertilizer_P2O5_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_P2O5_analysis_KG))
        self.edt_planting_fertilizer_K2O_analysis_KG .editingFinished.connect(
            lambda: format_value(self.edt_planting_fertilizer_K2O_analysis_KG))
        self.edt_top_dressing_analysis.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_analysis))
        self.edt_top_dressing_N_analysis.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_N_analysis))
        self.edt_top_dressing_P2O5_analysis.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_P2O5_analysis))
        self.edt_top_dressing_K2O_analysis.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_K2O_analysis))
        self.edt_top_dressing_N_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_N_analysis_KG))
        self.edt_top_dressing_P2O5_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_P2O5_analysis_KG))
        self.edt_top_dressing_K2O_analysis_KG.editingFinished.connect(
            lambda: format_value(self.edt_top_dressing_K2O_analysis_KG))
        self.edt_micro_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_analysis))
        self.edt_micro_zn_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_zn_analysis))
        self.edt_micro_b_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_b_analysis))
        self.edt_micro_cu_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_cu_analysis))
        self.edt_micro_mn_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_mn_analysis))
        self.edt_micro_mo_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_mo_analysis))
        self.edt_micro_co_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_co_analysis))
        self.edt_micro_ca_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_ca_analysis))
        self.edt_micro_s_analysis.editingFinished.connect(
            lambda: format_value(self.edt_micro_s_analysis))
        self.edt_micro_zn_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_zn_analysis_kg))
        self.edt_micro_b_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_b_analysis_kg))
        self.edt_micro_cu_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_cu_analysis_kg))
        self.edt_micro_mn_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_mn_analysis_kg))
        self.edt_micro_mo_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_mo_analysis_kg))
        self.edt_micro_co_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_co_analysis_kg))
        self.edt_micro_ca_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_ca_analysis_kg))
        self.edt_micro_s_analysis_kg.editingFinished.connect(
            lambda: format_value(self.edt_micro_s_analysis_kg))
        self.edt_prnt_analysis.editingFinished.connect(
            lambda: format_value(self.edt_prnt_analysis))
        self.edt_tca_analysis .editingFinished.connect(
            lambda: format_value(self.edt_tca_analysis))

    def authentication(self):
        result = self.log.login_data.authenticate_user(
            self.log.edt_user.text(), self.log.edt_password.text())
        if len(result) == 1:
            self.lbl_user.setText(result[0][2])
            self.code_user = int(result[0][0])
            self.name_user = result[0][1]

            message('ok', 'Usuário Válido!')
            self.log = None
            self.show()
        else:
            message('erro', 'Usuário não cadastrado!')

    def center_window(self):
        window_geometry = self.frameGeometry()
        screens = QApplication.screens()
        if screens:
            primary_screen = screens[0]
            screen_geometry = primary_screen.availableGeometry().center()
            window_geometry.moveCenter(screen_geometry)
            window_geometry.moveTop(window_geometry.top() - 28)
            self.move(window_geometry.topLeft())

    def open_user_window(self):
        if self.code_user == 1:
            self.user.button_enablements('save_or_cancel')
            self.user.read_only_user_fields(True)
            self.user.clear_fields_user_register()
            self.user.consult_user()
            self.stk_pag.setCurrentWidget(self.pag_user)
            self.table_grid_user.setFocus()
            self.edt_query_user.setFocus()
        else:
            message('erro', 'Acesso restrito ao "Administrador do Sistema".')

    def open_producer_window(self):
        self.producer.button_enablements('save_or_cancel')
        self.producer.read_only_producer_fields(True)
        self.producer.clear_fields_producer_register()
        self.producer.consult_producer()
        self.stk_pag.setCurrentWidget(self.pag_producer)
        self.table_grid_producer.setFocus()
        self.edt_query_producer.setFocus()

    def open_analysis_window(self):
        self.analysis.button_enablements('save_or_cancel')
        self.analysis.read_only_analysis_fields(True)
        self.analysis.clear_fields_analysis_register()
        self.analysis.consult_analysis()
        self.stk_pag.setCurrentWidget(self.pag_analysis)
        self.table_grid_analysis.setFocus()
        self.edt_query_analysis.setFocus()

    def open_neural_network_window(self):
        self.stk_pag.setCurrentWidget(self.pag_network)

        self.neural_network.processing_data()
        self.edt_epochs.setFocus()

        self.neural_network.load_files()
        self.support_vectors.load_files()
        self.random_forest.load_files()
        self.linear_regression.load_files()

    def predict_productivity(self):
        dataset = []
        dataset_linear_regression = []
        """
                CONVENCIONAL - IRRIGADO   → 1.0	 0.0  0.0  0.0
                CONVENCIONAL - SEQUEIRO   → 0.0	 1.0  0.0  0.0
                PLANTIO DIRETO - IRRIGADO →	0.0	 0.0  1.0  0.0
                PLANTIO DIRETO - SEQUEIRO →	0.0	 0.0  0.0  1.0

                CONVENCIONAL - IRRIGADO   → 0
                CONVENCIONAL - SEQUEIRO   → 1
                PLANTIO DIRETO - IRRIGADO → 2
                PLANTIO DIRETO - SEQUEIRO → 3.
        """
        if self.cbx_planting_system_analysis.currentText() == 'CONVENCIONAL - IRRIGADO':
            dataset.append(float(1.0))
            dataset.append(float(0.0))
            dataset.append(float(0.0))
            dataset.append(float(0.0))
        elif self.cbx_planting_system_analysis.currentText() == 'CONVENCIONAL - SEQUEIRO':
            dataset.append(float(0.0))
            dataset.append(float(1.0))
            dataset.append(float(0.0))
            dataset.append(float(0.0))
        elif self.cbx_planting_system_analysis.currentText() == 'PLANTIO DIRETO - IRRIGADO':
            dataset.append(float(0.0))
            dataset.append(float(0.0))
            dataset.append(float(1.0))
            dataset.append(float(0.0))
        elif self.cbx_planting_system_analysis.currentText() == 'PLANTIO DIRETO - SEQUEIRO':
            dataset.append(float(0.0))
            dataset.append(float(0.0))
            dataset.append(float(0.0))
            dataset.append(float(1.0))

        dataset.append(validates_float(self.edt_altitude_analysis.text()))
        dataset.append(validates_float(
            self.edt_minimum_temperature_analysis.text()))
        dataset.append(validates_float(
            self.edt_maximum_temperature_analysis.text()))
        dataset.append(validates_float(
            self.edt_rain_vegetative_analysis.text()))
        dataset.append(validates_float(
            self.edt_rain_reproductive_analysis.text()))
        dataset.append(validates_float(self.edt_ph_CaCl2_analysis.text()))
        dataset.append(validates_float(self.edt_clay_analysis.text()))
        dataset.append(validates_float(self.edt_MO_analysis.text()))
        dataset.append(validates_float(self.edt_CO_analysis.text()))
        dataset.append(validates_float(self.edt_K_cmolc_analysis.text()))
        dataset.append(validates_float(self.edt_Ca_analysis.text()))
        dataset.append(validates_float(self.edt_Mg_analysis.text()))
        dataset.append(validates_float(self.edt_P_meh_analysis.text()))
        dataset.append(validates_float(self.edt_S_SO4_analysis.text()))
        dataset.append(validates_float(self.edt_B_analysis.text()))
        dataset.append(validates_float(self.edt_Cu_analysis.text()))
        dataset.append(validates_float(self.edt_Fe_analysis.text()))
        dataset.append(validates_float(self.edt_Mn_analysis.text()))
        dataset.append(validates_float(self.edt_Zn_analysis.text()))

        dataset_linear_regression.append(
            validates_float(self.edt_altitude_analysis.text()))
        if self.cbx_planting_system_analysis.currentText() == 'CONVENCIONAL - IRRIGADO':
            dataset_linear_regression.append(0)
        elif self.cbx_planting_system_analysis.currentText() == 'CONVENCIONAL - SEQUEIRO':
            dataset_linear_regression.append(1)
        elif self.cbx_planting_system_analysis.currentText() == 'PLANTIO DIRETO - IRRIGADO':
            dataset_linear_regression.append(2)
        elif self.cbx_planting_system_analysis.currentText() == 'PLANTIO DIRETO - SEQUEIRO':
            dataset_linear_regression.append(3)
        dataset_linear_regression.append(validates_float(
            self.edt_minimum_temperature_analysis.text()))
        dataset_linear_regression.append(validates_float(
            self.edt_maximum_temperature_analysis.text()))
        dataset_linear_regression.append(validates_float(
            self.edt_rain_vegetative_analysis.text()))
        dataset_linear_regression.append(validates_float(
            self.edt_rain_reproductive_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_ph_CaCl2_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_clay_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_MO_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_CO_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_K_cmolc_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Ca_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Mg_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_P_meh_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_S_SO4_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_B_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Cu_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Fe_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Mn_analysis.text()))
        dataset_linear_regression.append(
            validates_float(self.edt_Zn_analysis.text()))

        n = (validates_float(self.edt_pre_sowing_N_analysis_KG.text()) +
             validates_float(self.edt_planting_fertilizer_N_analysis_KG.text()) +
             validates_float(self.edt_top_dressing_N_analysis_KG.text()))

        p2o5 = (validates_float(self.edt_pre_sowing_P2O5_analysis_KG.text()) +
                validates_float(self.edt_planting_fertilizer_P2O5_analysis_KG.text()) +
                validates_float(self.edt_top_dressing_P2O5_analysis_KG.text()))

        k2o = (validates_float(self.edt_pre_sowing_K2O_analysis_KG.text()) +
               validates_float(self.edt_planting_fertilizer_K2O_analysis_KG.text()) +
               validates_float(self.edt_top_dressing_K2O_analysis_KG.text()))

        dataset.append(n)
        dataset.append(p2o5)
        dataset.append(k2o)

        dataset_linear_regression.append(n)
        dataset_linear_regression.append(p2o5)
        dataset_linear_regression.append(k2o)

        self.model_predictions.predictive_attributes.clear()
        self.model_predictions.predictive_attributes.append(dataset)
        self.model_predictions.predictive_attributes_linear_regression.clear()
        self.model_predictions.predictive_attributes_linear_regression.append(
            dataset_linear_regression)

        self.model_predictions.exec()

    def capture_focus(self, widget):
        def _focus_event(event):
            self.last_focused_widget = widget
            QWidget.focusInEvent(widget, event)
        return _focus_event

    def select_model(self):
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        if self.last_focused_widget == self.list_network:
            file = self.list_network.currentItem()
            if file is not None:
                result1 = './model/neural_network/regressors/'+file.text()
                result2 = './model/neural_network/schedulers/x_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/neural_network/schedulers/y_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result4 = 'neural_network'
        elif self.last_focused_widget == self.list_linear_regression:
            file = self.list_linear_regression.currentItem()
            if file is not None:
                result1 = './model/linear_regression/regressors/'+file.text()
                result2 = './model/linear_regression/schedulers/x_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/linear_regression/schedulers/y_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result4 = 'linear_regression'

        elif self.last_focused_widget == self.list_random_forest:
            file = self.list_random_forest.currentItem()
            if file is not None:
                result1 = './model/random_forest/regressors/'+file.text()
                result2 = './model/random_forest/schedulers/x_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/random_forest/schedulers/y_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result4 = 'random_forest'
        elif self.last_focused_widget == self.list_svm:
            file = self.list_svm.currentItem()
            if file is not None:
                result1 = './model/svm/regressors/'+file.text()
                result2 = './model/svm/schedulers/x_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/svm/schedulers/y_scaler_' + \
                    re.search(r'\d+', file.text()).group()+'.pkl'
                result4 = 'svm'

        return result1, result2, result3, result4

    def delete_regressor(self):
        path_regressor, path_scheduler_x, path_scheduler_y, list_box = self.select_model()

        if (path_regressor is not None) and (path_scheduler_x is not None) and (path_scheduler_y is not None):
            if os.path.isfile(path_regressor):
                os.remove(path_regressor)
                if list_box == 'neural_network':
                    self.list_network.takeItem(self.list_network.currentRow())
                elif list_box == 'linear_regression':
                    self.list_linear_regression.takeItem(
                        self.list_linear_regression.currentRow())
                elif list_box == 'random_forest':
                    self.list_random_forest.takeItem(
                        self.list_random_forest.currentRow())
                elif list_box == 'svm':
                    self.list_svm.takeItem(self.list_svm.currentRow())
                message('ok', 'Regressor apagado com sucesso!')
            else:
                message('erro', 'O regressor não existe.')

            if os.path.isfile(path_scheduler_x):
                os.remove(path_scheduler_x)
            else:
                message('erro', 'O Escalonador X não existe.')

            if os.path.isfile(path_scheduler_y):
                os.remove(path_scheduler_y)
            else:
                message('erro', 'O Escalonador y não existe.')
        else:
            message('erro', 'Nenhum regressor foi selecionado.')

    def correlation_between_attributes(self):
        data = self.linear_regression.processing_data()
        self.linear_regression.correlation_between_attributes(data)

    def animation_menu(self):
        length = self.frm_left.width()

        if length == 0:
            new_length = 255

        else:
            new_length = 0

        self.animation = QtCore.QPropertyAnimation(
            self.frm_left, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(length)
        self.animation.setEndValue(new_length)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == '__main__':

    guia_fertil = QApplication(sys.argv)
    g = GuiaFertil()
    g.log.show()
    guia_fertil.exec()
