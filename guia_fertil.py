
import sys

from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

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
from succession_planting import SuccessionPlanting
from tools import format_value, message, numeric_field
from user_functions import User


class GuiaFertil(QMainWindow, Ui_win_guia_fertil):

    def __init__(self):
        super(GuiaFertil, self).__init__()
        self.setupUi(self)
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()
        self.code_user=0
        self.name_user=''

        self.log = Login()
        self.log.btn_login.clicked.connect(self.authentication)

        self.producer_data = DataBaseProducer(c.DATABASE_ADDRESS)
        self.user_data = DataBaseUser(c.DATABASE_ADDRESS)
        self.analysis_data = DataBaseAnalysis(c.DATABASE_ADDRESS)

        self.producer = Producer(self)
        self.user = User(self)
        self.analysis = Analysis(self)
        self.neural_network = Neural_Network(self)

        self.general_consultation = General_consultation(c.DATABASE_ADDRESS)
        self.predict_productivity = Predict_Productivity(self)
        self.bean_technology = BeanTechnology()
        self.succession_planting = SuccessionPlanting()
        self.npk_wheat = NpkWheat()
        self.limestone_plaster_soy = LimestonePlasterSoy()


        # events: main menu
        self.btn_home.clicked.connect(self.animation_menu)
        self.btn_menu_home.clicked.connect(lambda: self.stk_pag.setCurrentWidget(self.pag_home))
        self.btn_menu_user.clicked.connect(lambda: self.open_user_window())
        self.btn_menu_producer.clicked.connect(lambda: self.open_producer_window())
        self.btn_menu_analysis.clicked.connect(lambda: self.open_analysis_window())
        self.btn_menu_about.clicked.connect(lambda: self.stk_pag.setCurrentWidget(self.pag_about))
        self.btn_menu_neural_network.clicked.connect(lambda: self.open_neural_network_window())

        # events: neural network
        self.btn_cross_validation.clicked.connect(lambda: self.neural_network.cross_validation())
        self.btn_training_testing.clicked.connect(lambda: self.neural_network.training_testing())
        self.btn_save_regressor.clicked.connect(lambda: self.neural_network.save_regressor())
        self.btr_delete_regressor.clicked.connect(lambda: self.neural_network.delete_regressor())
        self.btn_measures_regressor.clicked.connect(lambda: self.neural_network.measures_regressor())
        self.btn_linear_regression.clicked.connect(lambda: self.neural_network.refression())
        self.btn_SVR.clicked.connect(lambda: self.neural_network.sv())
        self.btn_random_forest.clicked.connect(lambda: self.neural_network.random_forest())

        # events: producer registration
        self.btn_insert_producer.clicked.connect(lambda: self.producer.insert_new_producer())
        self.btn_update_producer.clicked.connect(lambda: self.producer.update_changes_producer())
        self.btn_cancelar_producer.clicked.connect(lambda: self.producer.cancel_edit_producer())
        self.btn_save_producer.clicked.connect(lambda: self.producer.save_new_producer(self.code_user))
        self.btn_save_change_producer.clicked.connect(lambda: self.producer.save_changes_producer(self.code_user))
        self.btn_delete_producer.clicked.connect(lambda: self.producer.delete_record_producer())
        self.btn_excel_producer.clicked.connect(lambda: self.producer.export_excel_producer())
        self.btn_pdf_report_producer.clicked.connect(lambda: self.producer.report_pdf_producer())
        self.btn_search_producer.clicked.connect(lambda: self.producer.consult_producer())
        self.edt_query_producer.textChanged.connect(lambda: self.producer.consult_producer())
        self.edt_cpf_cnpj_producer.editingFinished.connect(lambda: self.producer.cpf_cnpj())
        self.table_grid_producer.currentItemChanged.connect(lambda: self.producer.dataset_producer())

        # events: user registration
        self.btn_insert_user.clicked.connect(lambda: self.user.insert_new_user())
        self.btn_update_user.clicked.connect(lambda: self.user.update_changes_user())
        self.btn_cancelar_user.clicked.connect(lambda: self.user.cancel_edit_user())
        self.btn_save_user.clicked.connect(lambda: self.user.save_new_user())
        self.btn_save_change_user.clicked.connect(lambda: self.user.save_changes_user())
        self.btn_delete_user.clicked.connect(lambda: self.user.delete_record_user())
        self.btn_excel_user.clicked.connect(lambda: self.user.export_excel_user())
        self.btn_pdf_report_user.clicked.connect(lambda: self.user.report_pdf_user())
        self.btn_search_user.clicked.connect(lambda: self.user.consult_user())
        self.edt_query_user.textChanged.connect(lambda: self.user.consult_user())
        self.edt_cpf_user.editingFinished.connect(lambda: self.user.cpf_cnpj())
        self.table_grid_user.currentItemChanged.connect(lambda: self.user.dataset_user())
        
        # events: analysis registration
        self.btn_insert_analysis.clicked.connect(lambda: self.analysis.insert_new_analysis())
        self.btn_update_analysis.clicked.connect(lambda: self.analysis.update_changes_analysis())
        self.btn_consult_analysis.clicked.connect(lambda: self.analysis.consult_producer())
        self.btn_productivity_prediction.clicked.connect(lambda: self.analysis.predict_productivity())
        self.btn_cancelar_analysis.clicked.connect(lambda: self.analysis.cancel_edit_analysis())
        self.btn_save_analysis.clicked.connect(lambda: self.analysis.save_new_analysis(self.code_user))
        self.btn_save_change_analysis.clicked.connect(lambda: self.analysis.save_changes_analysis(self.code_user))
        self.btn_delete_analysis.clicked.connect(lambda: self.analysis.delete_record_analysis())
        self.btn_excel_analysis.clicked.connect(lambda: self.analysis.export_excel_analysis())
        self.btn_pdf_report_analysis.clicked.connect(lambda: self.analysis.report_pdf_analysis())
        self.btn_search_analysis.clicked.connect(lambda: self.analysis.consult_analysis())
        self.btn_Interpretation_analysis.clicked.connect(lambda: self.analysis.run_interpretation())

        self.edt_code_producer.editingFinished.connect(lambda: self.analysis.consult_producer_code())
        self.edt_query_analysis.textChanged.connect(lambda: self.analysis.consult_analysis())
        self.table_grid_analysis.currentItemChanged.connect(lambda: self.analysis.dataset_analysis())


       #calculate bases
        self.edt_K_cmolc_analysis.textChanged.connect(lambda: self.analysis.calculate_bases())
        self.edt_Ca_analysis.textChanged.connect(lambda: self.analysis.calculate_bases())
        self.edt_Mg_analysis.textChanged.connect(lambda: self.analysis.calculate_bases())
        self.edt_Al_analysis.textChanged.connect(lambda: self.analysis.calculate_bases())
        self.edt_T_analysis.textChanged.connect(lambda: self.analysis.calculate_bases())


       #calculate the npk quantity according to the type of fertilizer and dosage
        self.edt_pre_sowing_fertilizer_analysis.textChanged.connect(lambda: self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(),self.edt_pre_sowing_N_analysis.text(),self.edt_pre_sowing_P2O5_analysis.text(),self.edt_pre_sowing_K2O_analysis.text(),'pre_sowing'))
        self.edt_pre_sowing_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(),self.edt_pre_sowing_N_analysis.text(),self.edt_pre_sowing_P2O5_analysis.text(),self.edt_pre_sowing_K2O_analysis.text(),'pre_sowing'))
        self.edt_pre_sowing_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(),self.edt_pre_sowing_N_analysis.text(),self.edt_pre_sowing_P2O5_analysis.text(),self.edt_pre_sowing_K2O_analysis.text(),'pre_sowing'))
        self.edt_pre_sowing_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_pre_sowing_fertilizer_analysis.text(),self.edt_pre_sowing_N_analysis.text(),self.edt_pre_sowing_P2O5_analysis.text(),self.edt_pre_sowing_K2O_analysis.text(),'pre_sowing'))
        self.edt_planting_fertilizer_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(),self.edt_planting_fertilizer_N_analysis.text(),self.edt_planting_fertilizer_P2O5_analysis.text(),self.edt_planting_fertilizer_K2O_analysis.text(),'planting'))
        self.edt_planting_fertilizer_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(),self.edt_planting_fertilizer_N_analysis.text(),self.edt_planting_fertilizer_P2O5_analysis.text(),self.edt_planting_fertilizer_K2O_analysis.text(),'planting'))
        self.edt_planting_fertilizer_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(),self.edt_planting_fertilizer_N_analysis.text(),self.edt_planting_fertilizer_P2O5_analysis.text(),self.edt_planting_fertilizer_K2O_analysis.text(),'planting'))
        self.edt_planting_fertilizer_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_planting_fertilizer_analysis.text(),self.edt_planting_fertilizer_N_analysis.text(),self.edt_planting_fertilizer_P2O5_analysis.text(),self.edt_planting_fertilizer_K2O_analysis.text(),'planting'))
        self.edt_top_dressing_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(),self.edt_top_dressing_N_analysis.text(),self.edt_top_dressing_P2O5_analysis.text(),self.edt_top_dressing_K2O_analysis.text(),'top_dressing'))
        self.edt_top_dressing_N_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(),self.edt_top_dressing_N_analysis.text(),self.edt_top_dressing_P2O5_analysis.text(),self.edt_top_dressing_K2O_analysis.text(),'top_dressing'))
        self.edt_top_dressing_P2O5_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(),self.edt_top_dressing_N_analysis.text(),self.edt_top_dressing_P2O5_analysis.text(),self.edt_top_dressing_K2O_analysis.text(),'top_dressing'))
        self.edt_top_dressing_K2O_analysis.textChanged.connect(lambda:  self.analysis.npk_calculation(self.edt_top_dressing_analysis.text(),self.edt_top_dressing_N_analysis.text(),self.edt_top_dressing_P2O5_analysis.text(),self.edt_top_dressing_K2O_analysis.text(),'top_dressing'))
        
        self.edt_micro_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_zn_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_b_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_cu_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_mn_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_mo_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_co_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_ca_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))
        self.edt_micro_s_analysis.textChanged.connect(lambda: self.analysis.micro_calculation( self.edt_micro_analysis.text(), self.edt_micro_zn_analysis.text(), self.edt_micro_b_analysis.text(), self.edt_micro_cu_analysis.text(), self.edt_micro_mn_analysis.text(), self.edt_micro_mo_analysis.text(), self.edt_micro_co_analysis.text(), self.edt_micro_ca_analysis.text(), self.edt_micro_s_analysis.text() ))

        # configuring numeric fields in the Neural_Network
        self.edt_epochs.textChanged.connect(lambda: numeric_field(self.edt_epochs))
        self.edt_batch_size.textChanged.connect(lambda: numeric_field(self.edt_batch_size))
        self.edt_training.textChanged.connect(lambda: numeric_field(self.edt_training))
        self.edt_cv.textChanged.connect(lambda: numeric_field(self.edt_cv))
        self.edt_degree.textChanged.connect(lambda: numeric_field(self.edt_degree))
        self.edt_n_tree.textChanged.connect(lambda: numeric_field(self.edt_n_tree))
        self.edt_learning_rate.textChanged.connect(lambda: numeric_field(self.edt_learning_rate))

        # configuring numeric fields in the analysis registration
        self.edt_average_productivity_analysis.textChanged.connect(lambda: numeric_field(self.edt_average_productivity_analysis))
        self.edt_altitude_analysis.textChanged.connect(lambda: numeric_field(self.edt_altitude_analysis))
        self.edt_area_analysis.textChanged.connect(lambda: numeric_field(self.edt_area_analysis))
        self.edt_rain_vegetative_analysis.textChanged.connect(lambda: numeric_field(self.edt_rain_vegetative_analysis))
        self.edt_rain_reproductive_analysis.textChanged.connect(lambda: numeric_field(self.edt_rain_reproductive_analysis))
        self.edt_maximum_temperature_analysis.textChanged.connect(lambda: numeric_field(self.edt_maximum_temperature_analysis))
        self.edt_minimum_temperature_analysis.textChanged.connect(lambda: numeric_field(self.edt_minimum_temperature_analysis))
        self.edt_initial_depth_analysis.textChanged.connect(lambda: numeric_field(self.edt_initial_depth_analysis))
        self.edt_final_depth_analysis.textChanged.connect(lambda: numeric_field(self.edt_final_depth_analysis))
        self.edt_ph_H2O_analysis.textChanged.connect(lambda: numeric_field(self.edt_ph_H2O_analysis))
        self.edt_ph_CaCl2_analysis.textChanged.connect(lambda: numeric_field(self.edt_ph_CaCl2_analysis))
        self.edt_clay_analysis.textChanged.connect(lambda: numeric_field(self.edt_clay_analysis))
        self.edt_K_cmolc_analysis.textChanged.connect(lambda: numeric_field(self.edt_K_cmolc_analysis))
        self.edt_Ca_analysis.textChanged.connect(lambda: numeric_field(self.edt_Ca_analysis))
        self.edt_Mg_analysis.textChanged.connect(lambda: numeric_field(self.edt_Mg_analysis))
        self.edt_Al_analysis.textChanged.connect(lambda: numeric_field(self.edt_Al_analysis))
        self.edt_H_Al_analysis.textChanged.connect(lambda: numeric_field(self.edt_H_Al_analysis))
        self.edt_SB_analysis.textChanged.connect(lambda: numeric_field(self.edt_SB_analysis))
        self.edt_t_effective_CTC_analysis.textChanged.connect(lambda: numeric_field(self.edt_t_effective_CTC_analysis))
        self.edt_T_analysis.textChanged.connect(lambda: numeric_field(self.edt_T_analysis))
        self.edt_V_analysis.textChanged.connect(lambda: numeric_field(self.edt_V_analysis))
        self.edt_m_analysis.textChanged.connect(lambda: numeric_field(self.edt_m_analysis))
        self.edt_MO_analysis.textChanged.connect(lambda: numeric_field(self.edt_MO_analysis))
        self.edt_CO_analysis.textChanged.connect(lambda: numeric_field(self.edt_CO_analysis))
        self.edt_P_meh_analysis.textChanged.connect(lambda: numeric_field(self.edt_P_meh_analysis))
        self.edt_P_rem_analysis.textChanged.connect(lambda: numeric_field(self.edt_P_rem_analysis))
        self.edt_Na_analysis.textChanged.connect(lambda: numeric_field(self.edt_Na_analysis))
        self.edt_K_mg_analysis.textChanged.connect(lambda: numeric_field(self.edt_K_mg_analysis))
        self.edt_S_SO4_analysis.textChanged.connect(lambda: numeric_field(self.edt_S_SO4_analysis))
        self.edt_B_analysis.textChanged.connect(lambda: numeric_field(self.edt_B_analysis))
        self.edt_Cu_analysis.textChanged.connect(lambda: numeric_field(self.edt_Cu_analysis))
        self.edt_Fe_analysis.textChanged.connect(lambda: numeric_field(self.edt_Fe_analysis))
        self.edt_Mn_analysis.textChanged.connect(lambda: numeric_field(self.edt_Mn_analysis))
        self.edt_Zn_analysis.textChanged.connect(lambda: numeric_field(self.edt_Zn_analysis))
        self.edt_limestone_analysis.textChanged.connect(lambda: numeric_field(self.edt_limestone_analysis))
        self.edt_plaster_analysis.textChanged.connect(lambda: numeric_field(self.edt_plaster_analysis))
        self.edt_pre_sowing_fertilizer_analysis.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_fertilizer_analysis))
        self.edt_pre_sowing_N_analysis.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_N_analysis))
        self.edt_pre_sowing_P2O5_analysis.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_P2O5_analysis))
        self.edt_pre_sowing_K2O_analysis.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_K2O_analysis))
        self.edt_pre_sowing_N_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_N_analysis_KG))
        self.edt_pre_sowing_P2O5_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_P2O5_analysis_KG))
        self.edt_pre_sowing_K2O_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_pre_sowing_K2O_analysis_KG))
        self.edt_planting_fertilizer_analysis.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_analysis))
        self.edt_planting_fertilizer_N_analysis.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_N_analysis))
        self.edt_planting_fertilizer_P2O5_analysis.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_P2O5_analysis))
        self.edt_planting_fertilizer_K2O_analysis.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_K2O_analysis))
        self.edt_planting_fertilizer_N_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_N_analysis_KG))
        self.edt_planting_fertilizer_P2O5_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_P2O5_analysis_KG))
        self.edt_planting_fertilizer_K2O_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_planting_fertilizer_K2O_analysis_KG))
        self.edt_top_dressing_analysis.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_analysis))
        self.edt_top_dressing_N_analysis.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_N_analysis))
        self.edt_top_dressing_P2O5_analysis.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_P2O5_analysis))
        self.edt_top_dressing_K2O_analysis.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_K2O_analysis))
        self.edt_top_dressing_N_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_N_analysis_KG))
        self.edt_top_dressing_P2O5_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_P2O5_analysis_KG))
        self.edt_top_dressing_K2O_analysis_KG.textChanged.connect(lambda: numeric_field(self.edt_top_dressing_K2O_analysis_KG))
        self.edt_micro_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_analysis))
        self.edt_micro_zn_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_zn_analysis))
        self.edt_micro_b_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_b_analysis))
        self.edt_micro_cu_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_cu_analysis))
        self.edt_micro_mn_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_mn_analysis))
        self.edt_micro_mo_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_mo_analysis))
        self.edt_micro_co_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_co_analysis))
        self.edt_micro_ca_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_ca_analysis))
        self.edt_micro_s_analysis.textChanged.connect(lambda: numeric_field(self.edt_micro_s_analysis))
        self.edt_micro_zn_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_zn_analysis_kg))
        self.edt_micro_b_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_b_analysis_kg))
        self.edt_micro_cu_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_cu_analysis_kg))
        self.edt_micro_mn_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_mn_analysis_kg))
        self.edt_micro_mo_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_mo_analysis_kg))
        self.edt_micro_co_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_co_analysis_kg))
        self.edt_micro_ca_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_ca_analysis_kg))
        self.edt_micro_s_analysis_kg.textChanged.connect(lambda: numeric_field(self.edt_micro_s_analysis_kg))
        self.edt_prnt_analysis.textChanged.connect(lambda: numeric_field(self.edt_prnt_analysis))
        self.edt_tca_analysis.textChanged.connect(lambda: numeric_field(self.edt_tca_analysis))
        self.edt_average_productivity_analysis.editingFinished.connect(lambda: format_value(self.edt_average_productivity_analysis))
        self.edt_altitude_analysis.editingFinished.connect(lambda: format_value(self.edt_altitude_analysis))
        self.edt_area_analysis.editingFinished.connect(lambda: format_value(self.edt_area_analysis))
        self.edt_rain_vegetative_analysis.editingFinished.connect(lambda: format_value(self.edt_rain_vegetative_analysis))
        self.edt_rain_reproductive_analysis.editingFinished.connect(lambda: format_value(self.edt_rain_reproductive_analysis))
        self.edt_maximum_temperature_analysis.editingFinished.connect(lambda: format_value(self.edt_maximum_temperature_analysis))
        self.edt_minimum_temperature_analysis.editingFinished.connect(lambda: format_value(self.edt_minimum_temperature_analysis))
        self.edt_initial_depth_analysis.editingFinished.connect(lambda: format_value(self.edt_initial_depth_analysis))
        self.edt_final_depth_analysis.editingFinished.connect(lambda: format_value(self.edt_final_depth_analysis))
        self.edt_ph_H2O_analysis.editingFinished.connect(lambda: format_value(self.edt_ph_H2O_analysis))
        self.edt_ph_CaCl2_analysis.editingFinished.connect(lambda: format_value(self.edt_ph_CaCl2_analysis))
        self.edt_clay_analysis.editingFinished.connect(lambda: format_value(self.edt_clay_analysis))
        self.edt_K_cmolc_analysis.editingFinished.connect(lambda: format_value(self.edt_K_cmolc_analysis))
        self.edt_Ca_analysis.editingFinished.connect(lambda: format_value(self.edt_Ca_analysis))
        self.edt_Mg_analysis.editingFinished.connect(lambda: format_value(self.edt_Mg_analysis))
        self.edt_Al_analysis.editingFinished.connect(lambda: format_value(self.edt_Al_analysis))
        self.edt_H_Al_analysis.editingFinished.connect(lambda: format_value(self.edt_H_Al_analysis))
        self.edt_SB_analysis.editingFinished.connect(lambda: format_value(self.edt_SB_analysis))
        self.edt_t_effective_CTC_analysis.editingFinished.connect(lambda: format_value(self.edt_t_effective_CTC_analysis))
        self.edt_T_analysis.editingFinished.connect(lambda: format_value(self.edt_T_analysis))
        self.edt_V_analysis.editingFinished.connect(lambda: format_value(self.edt_V_analysis))
        self.edt_m_analysis.editingFinished.connect(lambda: format_value(self.edt_m_analysis))
        self.edt_MO_analysis.editingFinished.connect(lambda: format_value(self.edt_MO_analysis))
        self.edt_CO_analysis.editingFinished.connect(lambda: format_value(self.edt_CO_analysis))
        self.edt_P_meh_analysis.editingFinished.connect(lambda: format_value(self.edt_P_meh_analysis))
        self.edt_P_rem_analysis.editingFinished.connect(lambda: format_value(self.edt_P_rem_analysis))
        self.edt_Na_analysis.editingFinished.connect(lambda: format_value(self.edt_Na_analysis))
        self.edt_K_mg_analysis .editingFinished.connect(lambda: format_value(self.edt_K_mg_analysis))
        self.edt_S_SO4_analysis.editingFinished.connect(lambda: format_value(self.edt_S_SO4_analysis))
        self.edt_B_analysis.editingFinished.connect(lambda: format_value(self.edt_B_analysis))
        self.edt_Cu_analysis.editingFinished.connect(lambda: format_value(self.edt_Cu_analysis))
        self.edt_Fe_analysis.editingFinished.connect(lambda: format_value(self.edt_Fe_analysis))
        self.edt_Mn_analysis.editingFinished.connect(lambda: format_value(self.edt_Mn_analysis))
        self.edt_Zn_analysis.editingFinished.connect(lambda: format_value(self.edt_Zn_analysis))
        self.edt_limestone_analysis.editingFinished.connect(lambda: format_value(self.edt_limestone_analysis))
        self.edt_plaster_analysis.editingFinished.connect(lambda: format_value(self.edt_plaster_analysis))
        self.edt_pre_sowing_fertilizer_analysis.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_fertilizer_analysis))
        self.edt_pre_sowing_N_analysis.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_N_analysis))
        self.edt_pre_sowing_P2O5_analysis.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_P2O5_analysis))
        self.edt_pre_sowing_K2O_analysis.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_K2O_analysis))
        self.edt_pre_sowing_N_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_N_analysis_KG))
        self.edt_pre_sowing_P2O5_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_P2O5_analysis_KG))
        self.edt_pre_sowing_K2O_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_pre_sowing_K2O_analysis_KG))
        self.edt_planting_fertilizer_analysis.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_analysis))
        self.edt_planting_fertilizer_N_analysis.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_N_analysis))
        self.edt_planting_fertilizer_P2O5_analysis.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_P2O5_analysis))
        self.edt_planting_fertilizer_K2O_analysis.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_K2O_analysis))
        self.edt_planting_fertilizer_N_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_N_analysis_KG))
        self.edt_planting_fertilizer_P2O5_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_P2O5_analysis_KG))
        self.edt_planting_fertilizer_K2O_analysis_KG .editingFinished.connect(lambda: format_value(self.edt_planting_fertilizer_K2O_analysis_KG))
        self.edt_top_dressing_analysis.editingFinished.connect(lambda: format_value(self.edt_top_dressing_analysis))
        self.edt_top_dressing_N_analysis.editingFinished.connect(lambda: format_value(self.edt_top_dressing_N_analysis))
        self.edt_top_dressing_P2O5_analysis.editingFinished.connect(lambda: format_value(self.edt_top_dressing_P2O5_analysis))
        self.edt_top_dressing_K2O_analysis.editingFinished.connect(lambda: format_value(self.edt_top_dressing_K2O_analysis))
        self.edt_top_dressing_N_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_top_dressing_N_analysis_KG))
        self.edt_top_dressing_P2O5_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_top_dressing_P2O5_analysis_KG))
        self.edt_top_dressing_K2O_analysis_KG.editingFinished.connect(lambda: format_value(self.edt_top_dressing_K2O_analysis_KG))
        self.edt_micro_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_analysis))
        self.edt_micro_zn_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_zn_analysis))
        self.edt_micro_b_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_b_analysis))
        self.edt_micro_cu_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_cu_analysis))
        self.edt_micro_mn_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_mn_analysis))
        self.edt_micro_mo_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_mo_analysis))
        self.edt_micro_co_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_co_analysis))
        self.edt_micro_ca_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_ca_analysis))
        self.edt_micro_s_analysis.editingFinished.connect(lambda: format_value(self.edt_micro_s_analysis))
        self.edt_micro_zn_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_zn_analysis_kg))
        self.edt_micro_b_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_b_analysis_kg))
        self.edt_micro_cu_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_cu_analysis_kg))
        self.edt_micro_mn_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_mn_analysis_kg))
        self.edt_micro_mo_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_mo_analysis_kg))
        self.edt_micro_co_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_co_analysis_kg))
        self.edt_micro_ca_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_ca_analysis_kg))
        self.edt_micro_s_analysis_kg.editingFinished.connect(lambda: format_value(self.edt_micro_s_analysis_kg))
        self.edt_prnt_analysis.editingFinished.connect(lambda: format_value(self.edt_prnt_analysis))
        self.edt_tca_analysis .editingFinished.connect(lambda: format_value(self.edt_tca_analysis))

    def authentication(self):
        result = self.log.login_data.authenticate_user(self.log.edt_user.text(),self.log.edt_password.text())
        if len(result)==1:
            self.lbl_user.setText(result[0][2])
            self.code_user=int(result[0][0])
            self.name_user=result[0][1]
            
            message('ok','Usuário Válido!')
            self.log = None
            self.show()
        else:
            message('erro','Usuário não cadastrado!')

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

    def animation_menu(self):
        length = self.frm_left.width()

        if length == 0:
            new_length = 255

        else:
            new_length = 0

        self.animation = QtCore.QPropertyAnimation(self.frm_left, b'maximumWidth')
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
