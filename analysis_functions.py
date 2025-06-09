import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon, QPalette
from PySide6.QtWidgets import (QApplication, QFileDialog, QFrame, QLabel,
                               QLineEdit, QMainWindow, QMessageBox,
                               QPushButton, QTableWidget, QTableWidgetItem)

import constants as c
from fifth_approximation import FifthApproximation
from interpretation_report import InterpretationReport
from tools import format_float, message, message_confirmation, validates_float


class Analysis():
   def __init__(self, analysis_registration):
      self.register = analysis_registration

   def consult_producer(self):
         sql = """SELECT P.code_producer, P.name_producer
                     FROM PRODUCER P
                     WHERE P.name_producer LIKE ?
                     ORDER BY P.name_producer"""
         self.register.general_consultation.sql=sql
         self.register.general_consultation.query()
         self.register.general_consultation.confirm_registration = False
         self.register.general_consultation.exec()
         if self.register.general_consultation.confirm_registration == True:
            current_row = self.register.general_consultation.table_consult.currentRow()
            if current_row == -1:
               current_row = 1
            item = self.register.general_consultation.table_consult.item(current_row, 0)
            if item is not None:
               self.register.edt_code_producer.setText(self.register.general_consultation.table_consult.item(current_row, 0).text())
               self.register.edt_name_producer_analysis.setText(self.register.general_consultation.table_consult.item(current_row, 1).text())
                       
   def consult_producer_code(self):
        sql = """SELECT P.code_producer, P.name_producer FROM PRODUCER P WHERE P.code_producer = ?"""
        self.register.general_consultation.sql=sql
        result = self.register.general_consultation.query_code(self.register.edt_code_producer.text())
        if len(result) != 0:
           self.register.edt_name_producer_analysis.setText(result[0][1])
        else:
           self.register.edt_name_producer_analysis.setText('')
                  
   def npk_calculation(self, amount, n, p2o5, k2o, time_application):
      try:
         _a  = float(amount.replace(',', '.'))
         _n  = float(n.replace(',', '.'))
         _p  = float(p2o5.replace(',', '.'))
         _k  = float(k2o.replace(',', '.'))

         n_kg    = ( _a * _n ) / 100.00 
         p2o5_kg = ( _a * _p)  / 100.00 
         k2o_kg  = ( _a * _k ) / 100.00

         if (time_application=='pre_sowing'):
            self.register.edt_pre_sowing_N_analysis_KG.setText("{:.2f}".format(n_kg).replace('.', ','))
            self.register.edt_pre_sowing_P2O5_analysis_KG.setText("{:.2f}".format(p2o5_kg).replace('.', ','))
            self.register.edt_pre_sowing_K2O_analysis_KG.setText("{:.2f}".format(k2o_kg).replace('.', ','))

         elif (time_application=='planting'):
            self.register.edt_planting_fertilizer_N_analysis_KG.setText("{:.2f}".format(n_kg).replace('.', ','))
            self.register.edt_planting_fertilizer_P2O5_analysis_KG.setText("{:.2f}".format(p2o5_kg).replace('.', ','))
            self.register.edt_planting_fertilizer_K2O_analysis_KG.setText("{:.2f}".format(k2o_kg).replace('.', ','))
         
         elif (time_application=='top_dressing'):
            self.register.edt_top_dressing_N_analysis_KG.setText("{:.2f}".format(n_kg).replace('.', ','))
            self.register.edt_top_dressing_P2O5_analysis_KG.setText("{:.2f}".format(p2o5_kg).replace('.', ','))
            self.register.edt_top_dressing_K2O_analysis_KG.setText("{:.2f}".format(k2o_kg).replace('.', ','))
      except ValueError:
          pass

   def micro_calculation(self, amount, zn, b, cu, mn, mo, co, ca, s):
      try:
         _a   = float(amount.replace(',', '.'))
         _zn  = float(zn.replace(',', '.'))
         _b   = float(b.replace(',', '.'))
         _cu  = float(cu.replace(',', '.'))
         _mn  = float(mn.replace(',', '.'))
         _mo  = float(mo.replace(',', '.'))
         _co  = float(co.replace(',', '.'))
         _ca  = float(ca.replace(',', '.'))
         _s   = float(s.replace(',', '.'))

         zn_kg = ( _a * _zn ) / 100.00 
         b_kg  = ( _a * _b  ) / 100.00 
         cu_kg = ( _a * _cu ) / 100.00
         mn_kg = ( _a * _mn ) / 100.00 
         mo_kg = ( _a * _mo ) / 100.00 
         co_kg = ( _a * _co ) / 100.00
         ca_kg = ( _a * _ca ) / 100.00
         s_kg  = ( _a * _s  ) / 100.00

         self.register.edt_micro_zn_analysis_kg.setText("{:.2f}".format(zn_kg).replace('.', ','))
         self.register.edt_micro_b_analysis_kg.setText("{:.2f}".format(b_kg).replace('.', ','))
         self.register.edt_micro_cu_analysis_kg.setText("{:.2f}".format(cu_kg).replace('.', ','))
         self.register.edt_micro_mn_analysis_kg.setText("{:.2f}".format(mn_kg).replace('.', ','))
         self.register.edt_micro_mo_analysis_kg.setText("{:.2f}".format(mo_kg).replace('.', ','))
         self.register.edt_micro_co_analysis_kg.setText("{:.2f}".format(co_kg).replace('.', ','))
         self.register.edt_micro_ca_analysis_kg.setText("{:.2f}".format(ca_kg).replace('.', ','))
         self.register.edt_micro_s_analysis_kg.setText("{:.2f}".format(s_kg).replace('.', ','))

      except ValueError:
          pass

   def read_only_analysis_fields(self, status):
        self.register.edt_code_producer.setReadOnly(status)
        self.register.edt_agricultural_period_analysis.setReadOnly(status)
        self.register.edt_area_analysis.setReadOnly(status)
        self.register.edt_altitude_analysis.setReadOnly(status)
        self.register.edt_latitude_analysis.setReadOnly(status)
        self.register.edt_longitude_analysis.setReadOnly(status)
        self.register.edt_average_productivity_analysis.setReadOnly(status)
        self.register.edt_minimum_temperature_analysis.setReadOnly(status)
        self.register.edt_maximum_temperature_analysis.setReadOnly(status)
        self.register.edt_rain_vegetative_analysis.setReadOnly(status)
        self.register.edt_rain_reproductive_analysis.setReadOnly(status)
        self.register.edt_initial_depth_analysis.setReadOnly(status)
        self.register.edt_final_depth_analysis.setReadOnly(status)
        self.register.edt_ph_H2O_analysis.setReadOnly(status)
        self.register.edt_ph_CaCl2_analysis.setReadOnly(status)
        self.register.edt_clay_analysis.setReadOnly(status)
        self.register.edt_MO_analysis.setReadOnly(status)
        self.register.edt_CO_analysis.setReadOnly(status)
        self.register.edt_K_cmolc_analysis.setReadOnly(status)
        self.register.edt_Ca_analysis.setReadOnly(status)
        self.register.edt_Mg_analysis.setReadOnly(status)
        self.register.edt_Al_analysis.setReadOnly(status)
        #self.register.edt_H_Al_analysis.setReadOnly(status)
        #self.register.edt_SB_analysis.setReadOnly(status)
        #self.register.edt_t_effective_CTC_analysis.setReadOnly(status)
        self.register.edt_T_analysis.setReadOnly(status)
        #self.register.edt_V_analysis.setReadOnly(status)
        #self.register.edt_m_analysis.setReadOnly(status)
        self.register.edt_P_meh_analysis.setReadOnly(status)
        self.register.edt_P_rem_analysis.setReadOnly(status)
        self.register.edt_Na_analysis.setReadOnly(status)
        self.register.edt_K_mg_analysis.setReadOnly(status)
        self.register.edt_S_SO4_analysis.setReadOnly(status)
        self.register.edt_B_analysis.setReadOnly(status)
        self.register.edt_Cu_analysis.setReadOnly(status)
        self.register.edt_Fe_analysis.setReadOnly(status)
        self.register.edt_Mn_analysis.setReadOnly(status)
        self.register.edt_Zn_analysis.setReadOnly(status)
        self.register.edt_limestone_analysis.setReadOnly(status)
        self.register.edt_plaster_analysis.setReadOnly(status)
        self.register.edt_pre_sowing_fertilizer_analysis.setReadOnly(status)
        self.register.edt_pre_sowing_N_analysis.setReadOnly(status)
        self.register.edt_pre_sowing_P2O5_analysis.setReadOnly(status)
        self.register.edt_pre_sowing_K2O_analysis.setReadOnly(status)
        self.register.edt_planting_fertilizer_analysis.setReadOnly(status)
        self.register.edt_planting_fertilizer_N_analysis.setReadOnly(status)
        self.register.edt_planting_fertilizer_P2O5_analysis.setReadOnly(status)
        self.register.edt_planting_fertilizer_K2O_analysis.setReadOnly(status)
        self.register.edt_top_dressing_analysis.setReadOnly(status)
        self.register.edt_top_dressing_N_analysis.setReadOnly(status)
        self.register.edt_top_dressing_P2O5_analysis.setReadOnly(status)
        self.register.edt_top_dressing_K2O_analysis.setReadOnly(status)
        self.register.edt_sector_analysis.setReadOnly(status)
        self.register.edt_micro_analysis.setReadOnly(status)
        self.register.edt_micro_zn_analysis.setReadOnly(status)
        self.register.edt_micro_b_analysis.setReadOnly(status)
        self.register.edt_micro_cu_analysis.setReadOnly(status)
        self.register.edt_micro_mn_analysis.setReadOnly(status)
        self.register.edt_micro_mo_analysis.setReadOnly(status)
        self.register.edt_micro_co_analysis.setReadOnly(status)
        self.register.edt_micro_ca_analysis.setReadOnly(status)
        self.register.edt_micro_s_analysis.setReadOnly(status)
        self.register.edt_prnt_analysis.setReadOnly(status)
        self.register.edt_tca_analysis.setReadOnly(status)

        if status == True:
            # read
            self.register.cbx_culture_analysis.setEnabled(False)
            self.register.cbx_planting_system_analysis.setEnabled(False)
            self.register.edt_code_producer.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_agricultural_period_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.cbx_culture_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_area_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_altitude_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_latitude_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_longitude_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.cbx_planting_system_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_average_productivity_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_minimum_temperature_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_maximum_temperature_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_rain_vegetative_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_rain_reproductive_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_initial_depth_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_final_depth_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_ph_H2O_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_ph_CaCl2_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_clay_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_MO_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_CO_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_K_cmolc_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Ca_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Mg_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Al_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            #self.register.edt_H_Al_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            #self.register.edt_SB_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            #self.register.edt_t_effective_CTC_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_T_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            #self.register.edt_V_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            #self.register.edt_m_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_P_meh_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_P_rem_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Na_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_K_mg_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_S_SO4_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_B_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Cu_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Fe_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Mn_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_Zn_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_limestone_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_plaster_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_pre_sowing_fertilizer_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_pre_sowing_N_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_pre_sowing_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_pre_sowing_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_planting_fertilizer_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_planting_fertilizer_N_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_planting_fertilizer_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_planting_fertilizer_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_top_dressing_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_top_dressing_N_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_top_dressing_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_top_dressing_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_sector_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_zn_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_b_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_cu_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_mn_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_mo_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_co_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_ca_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_micro_s_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_prnt_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.register.edt_tca_analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
        else:
            self.register.cbx_culture_analysis.setEnabled(True)
            self.register.cbx_planting_system_analysis.setEnabled(True)
            self.register.edt_code_producer.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_agricultural_period_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.cbx_culture_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_area_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_altitude_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_latitude_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_longitude_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.cbx_planting_system_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_average_productivity_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_minimum_temperature_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_maximum_temperature_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_rain_vegetative_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_rain_reproductive_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_initial_depth_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_final_depth_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_ph_H2O_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_ph_CaCl2_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_clay_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_MO_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_CO_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_K_cmolc_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Ca_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Mg_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Al_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            #self.register.edt_H_Al_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            #self.register.edt_SB_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            #self.register.edt_t_effective_CTC_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_T_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            #self.register.edt_V_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            #self.register.edt_m_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_P_meh_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_P_rem_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Na_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_K_mg_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_S_SO4_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_B_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Cu_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Fe_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Mn_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_Zn_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_limestone_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_plaster_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_pre_sowing_fertilizer_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_pre_sowing_N_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_pre_sowing_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_pre_sowing_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_planting_fertilizer_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_planting_fertilizer_N_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_planting_fertilizer_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_planting_fertilizer_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_top_dressing_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_top_dressing_N_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_top_dressing_P2O5_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_top_dressing_K2O_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_sector_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_zn_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_b_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_cu_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_mn_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_mo_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_co_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_ca_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_micro_s_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_prnt_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.register.edt_tca_analysis.setStyleSheet("background-color: rgb(255, 255, 127);")

   def clear_fields_analysis_register(self):
        self.register.lbl_code_analysis.setText('')
        self.register.edt_code_producer.setText('')
        self.register.edt_name_producer_analysis.setText('')
        self.register.lbl_name_user_analysis.setText('')
        self.register.edt_agricultural_period_analysis.setText('')
        self.register.cbx_culture_analysis.setCurrentText('')
        self.register.edt_area_analysis.setText('')
        self.register.edt_altitude_analysis.setText('')
        self.register.edt_latitude_analysis.setText('')
        self.register.edt_longitude_analysis.setText('')
        self.register.cbx_planting_system_analysis.setCurrentText('')
        self.register.edt_average_productivity_analysis.setText('')
        self.register.edt_minimum_temperature_analysis.setText('')
        self.register.edt_maximum_temperature_analysis.setText('')
        self.register.edt_rain_vegetative_analysis.setText('')
        self.register.edt_rain_reproductive_analysis.setText('')
        self.register.edt_initial_depth_analysis.setText('')
        self.register.edt_final_depth_analysis.setText('')
        self.register.edt_ph_H2O_analysis.setText('')
        self.register.edt_ph_CaCl2_analysis.setText('')
        self.register.edt_clay_analysis.setText('')
        self.register.edt_MO_analysis.setText('')
        self.register.edt_CO_analysis.setText('')
        self.register.edt_K_cmolc_analysis.setText('')
        self.register.edt_Ca_analysis.setText('')
        self.register.edt_Mg_analysis.setText('')
        self.register.edt_Al_analysis.setText('')
        self.register.edt_H_Al_analysis.setText('')
        self.register.edt_SB_analysis.setText('')
        self.register.edt_t_effective_CTC_analysis.setText('')
        self.register.edt_T_analysis.setText('')
        self.register.edt_V_analysis.setText('')
        self.register.edt_m_analysis.setText('')
        self.register.edt_P_meh_analysis.setText('')
        self.register.edt_P_rem_analysis.setText('')
        self.register.edt_Na_analysis.setText('')
        self.register.edt_K_mg_analysis.setText('')
        self.register.edt_S_SO4_analysis.setText('')
        self.register.edt_B_analysis.setText('')
        self.register.edt_Cu_analysis.setText('')
        self.register.edt_Fe_analysis.setText('')
        self.register.edt_Mn_analysis.setText('')
        self.register.edt_Zn_analysis.setText('')
        self.register.edt_limestone_analysis.setText('')
        self.register.edt_plaster_analysis.setText('')
        self.register.edt_pre_sowing_fertilizer_analysis.setText('')
        self.register.edt_pre_sowing_N_analysis.setText('')
        self.register.edt_pre_sowing_P2O5_analysis.setText('')
        self.register.edt_pre_sowing_K2O_analysis.setText('')
        self.register.edt_pre_sowing_N_analysis_KG.setText('')
        self.register.edt_pre_sowing_P2O5_analysis_KG.setText('')
        self.register.edt_pre_sowing_K2O_analysis_KG.setText('')
        self.register.edt_planting_fertilizer_analysis.setText('')
        self.register.edt_planting_fertilizer_N_analysis.setText('')
        self.register.edt_planting_fertilizer_P2O5_analysis.setText('')
        self.register.edt_planting_fertilizer_K2O_analysis.setText('')
        self.register.edt_planting_fertilizer_N_analysis_KG.setText('')
        self.register.edt_planting_fertilizer_P2O5_analysis_KG.setText('')
        self.register.edt_planting_fertilizer_K2O_analysis_KG.setText('')
        self.register.edt_top_dressing_analysis.setText('')
        self.register.edt_top_dressing_N_analysis.setText('')
        self.register.edt_top_dressing_P2O5_analysis.setText('')
        self.register.edt_top_dressing_K2O_analysis.setText('')
        self.register.edt_top_dressing_N_analysis_KG.setText('')
        self.register.edt_top_dressing_P2O5_analysis_KG.setText('')
        self.register.edt_top_dressing_K2O_analysis_KG.setText('')
        self.register.edt_sector_analysis.setText('')
        self.register.edt_micro_analysis.setText('')
        self.register.edt_micro_zn_analysis.setText('')
        self.register.edt_micro_b_analysis.setText('')
        self.register.edt_micro_cu_analysis.setText('')
        self.register.edt_micro_mn_analysis.setText('')
        self.register.edt_micro_mo_analysis.setText('')
        self.register.edt_micro_co_analysis.setText('')
        self.register.edt_micro_ca_analysis.setText('')
        self.register.edt_micro_s_analysis.setText('')
        self.register.edt_micro_zn_analysis_kg.setText('')
        self.register.edt_micro_b_analysis_kg.setText('')
        self.register.edt_micro_cu_analysis_kg.setText('')
        self.register.edt_micro_mn_analysis_kg.setText('')
        self.register.edt_micro_mo_analysis_kg.setText('')
        self.register.edt_micro_co_analysis_kg.setText('')
        self.register.edt_micro_ca_analysis_kg.setText('')
        self.register.edt_micro_s_analysis_kg.setText('')
        self.register.edt_prnt_analysis.setText('')
        self.register.edt_tca_analysis.setText('')

   def button_enablements(self, status):
        if status == 'insert':
            self.register.btn_insert_analysis.setEnabled(False)
            self.register.btn_update_analysis.setEnabled(False)
            self.register.btn_consult_analysis.setEnabled(True)
            self.register.btn_cancelar_analysis.setEnabled(True)
            self.register.btn_save_change_analysis.setEnabled(False)
            self.register.btn_save_analysis.setEnabled(True)
        elif status == 'update':
            self.register.btn_insert_analysis.setEnabled(False)
            self.register.btn_update_analysis.setEnabled(False)
            self.register.btn_consult_analysis.setEnabled(True)
            self.register.btn_cancelar_analysis.setEnabled(True)
            self.register.btn_save_change_analysis.setEnabled(True)
            self.register.btn_save_analysis.setEnabled(False)
        elif status == 'save_or_cancel':
            self.register.btn_insert_analysis.setEnabled(True)
            self.register.btn_update_analysis.setEnabled(True)
            self.register.btn_consult_analysis.setEnabled(False)
            self.register.btn_cancelar_analysis.setEnabled(False)
            self.register.btn_save_change_analysis.setEnabled(False)
            self.register.btn_save_analysis.setEnabled(False)

   def insert_new_analysis(self):
        self.button_enablements('insert')
        self.read_only_analysis_fields(False)
        self.clear_fields_analysis_register()
        self.register.cbx_culture_analysis.setCurrentIndex(2)
        self.register.cbx_planting_system_analysis.setCurrentIndex(1)
        self.register.edt_code_producer.setFocus()

   def update_changes_analysis(self):
        code = self.register.edt_code_producer.text()
        if code != '':
            self.button_enablements('update')
            self.read_only_analysis_fields(False)
        self.register.edt_code_producer.setFocus()

   def table_assembly(self, result):
         if result is not None:
            self.register.table_grid_analysis.setAlternatingRowColors(True)
            self.register.table_grid_analysis.clearContents()
            self.register.table_grid_analysis.setRowCount(len(result))

            for row_index, row_text in enumerate(result):
               for column_index, data in enumerate(row_text):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.register.table_grid_analysis.setItem(
                        row_index, column_index, item)
                    
         self.register.table_grid_analysis.setColumnWidth(0, 100)  # code_analysis,
         self.register.table_grid_analysis.setColumnWidth(1, 100)  # code_producer,
         self.register.table_grid_analysis.setColumnWidth(2, 200)  # name_producer,
         self.register.table_grid_analysis.setColumnWidth(3, 200)  # sector_analysis,
         self.register.table_grid_analysis.setColumnWidth(4, 80)   # agricultural_period_analysis,
         self.register.table_grid_analysis.setColumnWidth(5, 80)   # culture_analysis,
         self.register.table_grid_analysis.setColumnWidth(6, 80)   # area_analysis,
         self.register.table_grid_analysis.setColumnWidth(7, 80)   # altitude_analysis,
         self.register.table_grid_analysis.setColumnWidth(8, 100)  # latitude_analysis,
         self.register.table_grid_analysis.setColumnWidth(9, 100)  # longitude_analysis,
         self.register.table_grid_analysis.setColumnWidth(10,200)  # planting_system_analysis,
         self.register.table_grid_analysis.setColumnWidth(11,200)  # average_productivity_analysis,
         self.register.table_grid_analysis.setColumnWidth(12,150)  # minimum_temperature_analysis ,
         self.register.table_grid_analysis.setColumnWidth(13,150)  # maximum_temperature_analysis ,
         self.register.table_grid_analysis.setColumnWidth(14,150)  # rain_vegetative_analysis,
         self.register.table_grid_analysis.setColumnWidth(15,150)  # rain_reproductive_analysis,
         self.register.table_grid_analysis.setColumnWidth(16,150)  # initial_depth_analysis,
         self.register.table_grid_analysis.setColumnWidth(17,150)  # final_depth_analysis,
         self.register.table_grid_analysis.setColumnWidth(18,100)  # ph_H2O_analysis,
         self.register.table_grid_analysis.setColumnWidth(19,100)  # ph_CaCl2_analysis ,
         self.register.table_grid_analysis.setColumnWidth(20,100)  # clay_analysis,
         self.register.table_grid_analysis.setColumnWidth(21,100)  # MO_analysis,
         self.register.table_grid_analysis.setColumnWidth(22,100)  # CO_analysis,
         self.register.table_grid_analysis.setColumnWidth(23,100)  # K_cmolc_analysis,
         self.register.table_grid_analysis.setColumnWidth(24,100)  # Ca_analysis,
         self.register.table_grid_analysis.setColumnWidth(25,100)  # Mg_analysis,
         self.register.table_grid_analysis.setColumnWidth(26,100)  # Al_analysis,
         self.register.table_grid_analysis.setColumnWidth(27,150)  # H_Al_analysis,
         self.register.table_grid_analysis.setColumnWidth(28,100)  # SB_analysis,
         self.register.table_grid_analysis.setColumnWidth(29,100)  # t_effective_CTC_analysis,
         self.register.table_grid_analysis.setColumnWidth(30,100)  # T_analysis,
         self.register.table_grid_analysis.setColumnWidth(31,100)  # V_analysis,
         self.register.table_grid_analysis.setColumnWidth(32,100)  # m_analysis,
         self.register.table_grid_analysis.setColumnWidth(33,100)  # P_meh_analysis ,
         self.register.table_grid_analysis.setColumnWidth(34,100)  # P_rem_analysis ,
         self.register.table_grid_analysis.setColumnWidth(35,100)  # Na_analysis,
         self.register.table_grid_analysis.setColumnWidth(36,100)  # K_mg_analysis,
         self.register.table_grid_analysis.setColumnWidth(37,100)  # S_SO4_analysis,
         self.register.table_grid_analysis.setColumnWidth(38,100)  # B_analysis,
         self.register.table_grid_analysis.setColumnWidth(39,100)  # Cu_analysis,
         self.register.table_grid_analysis.setColumnWidth(40,100)  # Fe_analysis,
         self.register.table_grid_analysis.setColumnWidth(41,100)  # Mn_analysis,
         self.register.table_grid_analysis.setColumnWidth(42,100)  # Zn_analysis,
         self.register.table_grid_analysis.setColumnWidth(43,100)  # limestone_analysis,
         self.register.table_grid_analysis.setColumnWidth(44,100)  # prnt_analysis,
         self.register.table_grid_analysis.setColumnWidth(45,100)  # plaster_analysis,
         self.register.table_grid_analysis.setColumnWidth(46,100)  # tca_analysis,
         self.register.table_grid_analysis.setColumnWidth(47,150)  # pre_sowing_fertilizer_analysis,
         self.register.table_grid_analysis.setColumnWidth(48,100)  # pre_sowing_N_analysis,
         self.register.table_grid_analysis.setColumnWidth(49,100)  # pre_sowing_P2O5_analysis,
         self.register.table_grid_analysis.setColumnWidth(50,100)  # pre_sowing_K2O_analysis,
         self.register.table_grid_analysis.setColumnWidth(51,100)  # pre_sowing_N_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(52,100)  # pre_sowing_P2O5_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(53,100)  # pre_sowing_K2O_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(54,150)  # seeding_fertilizer_analysis,
         self.register.table_grid_analysis.setColumnWidth(55,100)  # seeding_N_analysis,
         self.register.table_grid_analysis.setColumnWidth(56,100)  # seeding_P2O5_analysis,
         self.register.table_grid_analysis.setColumnWidth(57,100)  # seeding_K2O_analysis,
         self.register.table_grid_analysis.setColumnWidth(58,100)  # seeding_N_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(59,100)  # seeding_P2O5_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(60,100)  # seeding_K2O_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(61,150)  # top_dressing_fertilizer_analysis,
         self.register.table_grid_analysis.setColumnWidth(62,100)  # top_dressing_N_analysis,
         self.register.table_grid_analysis.setColumnWidth(63,100)  # top_dressing_P2O5_analysis,
         self.register.table_grid_analysis.setColumnWidth(64,100)  # top_dressing_K2O_analysis,
         self.register.table_grid_analysis.setColumnWidth(65,100)  # top_dressing_N_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(66,100)  # top_dressing_P2O5_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(67,100)  # top_dressing_K2O_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(68,150)  # micro_analysis,
         self.register.table_grid_analysis.setColumnWidth(69,100)  # micro_zn_analysis,
         self.register.table_grid_analysis.setColumnWidth(70,100)  # micro_b_analysis,
         self.register.table_grid_analysis.setColumnWidth(71,100)  # micro_cu_analysis,
         self.register.table_grid_analysis.setColumnWidth(72,100)  # micro_mn_analysis,
         self.register.table_grid_analysis.setColumnWidth(73,100)  # micro_mo_analysis,
         self.register.table_grid_analysis.setColumnWidth(74,100)  # micro_co_analysis,
         self.register.table_grid_analysis.setColumnWidth(75,100)  # micro_ca_analysis,
         self.register.table_grid_analysis.setColumnWidth(76,100)  # micro_s_analysis,
         self.register.table_grid_analysis.setColumnWidth(77,100)  # micro_zn_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(78,100)  # micro_b_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(79,100)  # micro_cu_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(80,100)  # micro_mn_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(81,100)  # micro_mo_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(82,100)  # micro_co_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(83,100)  # micro_ca_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(84,100)  # micro_s_analysis_kg,
         self.register.table_grid_analysis.setColumnWidth(85,200)  # name_user

   def consult_analysis_code(self, code_analysis):
      result = self.register.analysis_data.query_analysis_code(code_analysis)
      self.table_assembly(result)
      self.register.table_grid_analysis.setFocus()
      self.register.edt_query_analysis.setFocus()

   def cancel_edit_analysis(self):
      if self.register.btn_save_analysis.isEnabled() == True:
         self.clear_fields_analysis_register()
      else:
         self.consult_analysis_code(self.register.lbl_code_analysis.text())
      
      self.register.table_grid_analysis.setFocus()
      self.register.edt_query_analysis.setFocus()
      self.button_enablements('save_or_cancel')
      self.read_only_analysis_fields(True)

   def save_new_analysis(self, code_user):
         self.consult_producer_code()
         if self.register.edt_name_producer_analysis.text() !='':
            
            if validates_float(self.register.edt_K_mg_analysis.text()) <= 0:
               self.register.edt_K_mg_analysis.setText(format_float(self.convert_K_cmolc_to_mg_dm3()))
            
            dataset = (  self.register.edt_code_producer.text(),
                        code_user,
                        self.register.edt_agricultural_period_analysis.text(),
                        self.register.cbx_culture_analysis.currentText(),
                        self.register.edt_area_analysis.text(),
                        self.register.edt_altitude_analysis.text(),
                        self.register.edt_latitude_analysis.text(),
                        self.register.edt_longitude_analysis.text(),
                        self.register.cbx_planting_system_analysis.currentText(),
                        self.register.edt_average_productivity_analysis.text(),
                        self.register.edt_minimum_temperature_analysis.text(),
                        self.register.edt_maximum_temperature_analysis.text(),
                        self.register.edt_rain_vegetative_analysis.text(),
                        self.register.edt_rain_reproductive_analysis.text(),
                        self.register.edt_initial_depth_analysis.text(),
                        self.register.edt_final_depth_analysis.text(),
                        self.register.edt_ph_H2O_analysis.text(),
                        self.register.edt_ph_CaCl2_analysis.text(),
                        self.register.edt_clay_analysis.text(),
                        self.register.edt_MO_analysis.text(),
                        self.register.edt_CO_analysis.text(),
                        self.register.edt_K_cmolc_analysis.text(),
                        self.register.edt_Ca_analysis.text(),
                        self.register.edt_Mg_analysis.text(),
                        self.register.edt_Al_analysis.text(),
                        self.register.edt_H_Al_analysis.text(),
                        self.register.edt_SB_analysis.text(),
                        self.register.edt_t_effective_CTC_analysis.text(),
                        self.register.edt_T_analysis.text(),
                        self.register.edt_V_analysis.text(),
                        self.register.edt_m_analysis.text(),
                        self.register.edt_P_meh_analysis.text(),
                        self.register.edt_P_rem_analysis.text(),
                        self.register.edt_Na_analysis.text(),
                        self.register.edt_K_mg_analysis.text(),
                        self.register.edt_S_SO4_analysis.text(),
                        self.register.edt_B_analysis.text(),
                        self.register.edt_Cu_analysis.text(),
                        self.register.edt_Fe_analysis.text(),
                        self.register.edt_Mn_analysis.text(),
                        self.register.edt_Zn_analysis.text(),
                        self.register.edt_limestone_analysis.text(),
                        self.register.edt_plaster_analysis.text(),
                        self.register.edt_pre_sowing_fertilizer_analysis.text(),
                        self.register.edt_pre_sowing_N_analysis.text(),
                        self.register.edt_pre_sowing_P2O5_analysis.text(),
                        self.register.edt_pre_sowing_K2O_analysis.text(),
                        self.register.edt_planting_fertilizer_analysis.text(),
                        self.register.edt_planting_fertilizer_N_analysis.text(),
                        self.register.edt_planting_fertilizer_P2O5_analysis.text(),
                        self.register.edt_planting_fertilizer_K2O_analysis.text(),
                        self.register.edt_top_dressing_analysis.text(),
                        self.register.edt_top_dressing_N_analysis.text(),
                        self.register.edt_top_dressing_P2O5_analysis.text(),
                        self.register.edt_top_dressing_K2O_analysis.text(),   
                        self.register.edt_sector_analysis.text(),
                        self.register.edt_micro_analysis.text(),
                        self.register.edt_micro_zn_analysis.text(),
                        self.register.edt_micro_b_analysis.text(),
                        self.register.edt_micro_cu_analysis.text(),
                        self.register.edt_micro_mn_analysis.text(),
                        self.register.edt_micro_mo_analysis.text(),
                        self.register.edt_micro_co_analysis.text(),
                        self.register.edt_micro_ca_analysis.text(),
                        self.register.edt_micro_s_analysis.text(),
                        self.register.edt_prnt_analysis.text(),
                        self.register.edt_tca_analysis.text())
            self.register.analysis_data.insert_analysis(dataset)
            self.button_enablements('save_or_cancel')
            self.read_only_analysis_fields(True)
            self.clear_fields_analysis_register()
         else:
            message('erro', 'A análise precisa estar relacionada a um produtor.')

   def save_changes_analysis(self,code_user):
      self.consult_producer_code()
      if self.register.edt_name_producer_analysis.text() !='':
         
         if validates_float(self.register.edt_K_mg_analysis.text()) <= 0:
            self.register.edt_K_mg_analysis.setText(format_float(self.convert_K_cmolc_to_mg_dm3()))
         
         code_analysis = self.register.lbl_code_analysis.text()
         dataset = (  code_analysis,
                   self.register.edt_code_producer.text(),
                   str(code_user),
                   self.register.edt_agricultural_period_analysis.text(),
                   self.register.cbx_culture_analysis.currentText(),
                   self.register.edt_area_analysis.text(),
                   self.register.edt_altitude_analysis.text(),
                   self.register.edt_latitude_analysis.text(),
                   self.register.edt_longitude_analysis.text(),
                   self.register.cbx_planting_system_analysis.currentText(),
                   self.register.edt_average_productivity_analysis.text(),
                   self.register.edt_minimum_temperature_analysis.text(),
                   self.register.edt_maximum_temperature_analysis.text(),
                   self.register.edt_rain_vegetative_analysis.text(),
                   self.register.edt_rain_reproductive_analysis.text(),
                   self.register.edt_initial_depth_analysis.text(),
                   self.register.edt_final_depth_analysis.text(),
                   self.register.edt_ph_H2O_analysis.text(),
                   self.register.edt_ph_CaCl2_analysis.text(),
                   self.register.edt_clay_analysis.text(),
                   self.register.edt_MO_analysis.text(),
                   self.register.edt_CO_analysis.text(),
                   self.register.edt_K_cmolc_analysis.text(),
                   self.register.edt_Ca_analysis.text(),
                   self.register.edt_Mg_analysis.text(),
                   self.register.edt_Al_analysis.text(),
                   self.register.edt_H_Al_analysis.text(),
                   self.register.edt_SB_analysis.text(),
                   self.register.edt_t_effective_CTC_analysis.text(),
                   self.register.edt_T_analysis.text(),
                   self.register.edt_V_analysis.text(),
                   self.register.edt_m_analysis.text(),
                   self.register.edt_P_meh_analysis.text(),
                   self.register.edt_P_rem_analysis.text(),
                   self.register.edt_Na_analysis.text(),
                   self.register.edt_K_mg_analysis.text(),
                   self.register.edt_S_SO4_analysis.text(),
                   self.register.edt_B_analysis.text(),
                   self.register.edt_Cu_analysis.text(),
                   self.register.edt_Fe_analysis.text(),
                   self.register.edt_Mn_analysis.text(),
                   self.register.edt_Zn_analysis.text(),
                   self.register.edt_limestone_analysis.text(),
                   self.register.edt_plaster_analysis.text(),
                   self.register.edt_pre_sowing_fertilizer_analysis.text(),
                   self.register.edt_pre_sowing_N_analysis.text(),
                   self.register.edt_pre_sowing_P2O5_analysis.text(),
                   self.register.edt_pre_sowing_K2O_analysis.text(),
                   self.register.edt_planting_fertilizer_analysis.text(),
                   self.register.edt_planting_fertilizer_N_analysis.text(),
                   self.register.edt_planting_fertilizer_P2O5_analysis.text(),
                   self.register.edt_planting_fertilizer_K2O_analysis.text(),
                   self.register.edt_top_dressing_analysis.text(),
                   self.register.edt_top_dressing_N_analysis.text(),
                   self.register.edt_top_dressing_P2O5_analysis.text(),
                   self.register.edt_top_dressing_K2O_analysis.text(),
                   self.register.edt_sector_analysis.text(),
                   self.register.edt_micro_analysis.text(),
                   self.register.edt_micro_zn_analysis.text(),
                   self.register.edt_micro_b_analysis.text(),
                   self.register.edt_micro_cu_analysis.text(),
                   self.register.edt_micro_mn_analysis.text(),
                   self.register.edt_micro_mo_analysis.text(),
                   self.register.edt_micro_co_analysis.text(),
                   self.register.edt_micro_ca_analysis.text(),
                   self.register.edt_micro_s_analysis.text(),
                   self.register.edt_prnt_analysis.text(),
                   self.register.edt_tca_analysis.text())
         self.register.analysis_data.update_analysis(dataset)

         self.consult_analysis_code(code_analysis)
        
         self.register.table_grid_analysis.setFocus()
         self.register.edt_query_analysis.setFocus()
         self.button_enablements('save_or_cancel')
         self.read_only_analysis_fields(True)

      else:
         message('erro', 'A análise precisa estar relacionada a um produtor.')

   def consult_analysis(self):
      result = self.register.analysis_data.query_analysis(self.generate_sql_query())
      self.table_assembly(result)
      self.register.table_grid_analysis.setFocus()
      self.register.edt_query_analysis.setFocus()
   
   def delete_record_analysis(self):
      if self.register.table_grid_analysis.rowCount() >= 1:
         if message_confirmation('Excluir', 'Este registro será excluido.', 'Você tem certeza que deseja continuar?') == 'confirmado':
            code = self.register.lbl_code_analysis.text()
            self.register.analysis_data.delete_analysis(code)
            self.consult_analysis()
            if self.register.table_grid_analysis.rowCount() < 1:
               self.clear_fields_analysis_register()

   def export_excel_analysis(self):
      if self.register.table_grid_analysis.rowCount() >= 1:
         self.register.analysis_data.export_excel(self.generate_sql_query())

   def report_pdf_analysis(self):
        if self.register.table_grid_analysis.rowCount() >= 1:
           self.register.analysis_data.pdf_report(self.generate_sql_query())

   def dataset_analysis(self):
         current_row = self.register.table_grid_analysis.currentRow()
         if current_row == -1:
            current_row = 1

         item = self.register.table_grid_analysis.item(current_row, 0)

         if item is not None:
            self.register.lbl_code_analysis.setText(self.register.table_grid_analysis.item(current_row, 0).text())
            self.register.edt_code_producer.setText(self.register.table_grid_analysis.item(current_row, 1).text())
            self.register.edt_name_producer_analysis.setText(self.register.table_grid_analysis.item(current_row, 2).text())
            self.register.edt_sector_analysis.setText(self.register.table_grid_analysis.item(current_row, 3).text())
            self.register.edt_agricultural_period_analysis.setText(self.register.table_grid_analysis.item(current_row, 4).text())
            self.register.cbx_culture_analysis.setCurrentText(self.register.table_grid_analysis.item(current_row, 5).text())
            self.register.edt_area_analysis.setText(self.register.table_grid_analysis.item(current_row, 6).text())
            self.register.edt_altitude_analysis.setText(self.register.table_grid_analysis.item(current_row, 7).text())
            self.register.edt_latitude_analysis.setText(self.register.table_grid_analysis.item(current_row, 8).text())
            self.register.edt_longitude_analysis.setText(self.register.table_grid_analysis.item(current_row, 9).text())
            self.register.cbx_planting_system_analysis.setCurrentText(self.register.table_grid_analysis.item(current_row, 10).text())
            self.register.edt_average_productivity_analysis.setText(self.register.table_grid_analysis.item(current_row, 11).text())
            self.register.edt_minimum_temperature_analysis.setText(self.register.table_grid_analysis.item(current_row, 12).text())
            self.register.edt_maximum_temperature_analysis.setText(self.register.table_grid_analysis.item(current_row, 13).text())
            self.register.edt_rain_vegetative_analysis.setText(self.register.table_grid_analysis.item(current_row, 14).text())
            self.register.edt_rain_reproductive_analysis.setText(self.register.table_grid_analysis.item(current_row, 15).text())
            self.register.edt_initial_depth_analysis.setText(self.register.table_grid_analysis.item(current_row, 16).text())
            self.register.edt_final_depth_analysis.setText(self.register.table_grid_analysis.item(current_row, 17).text())
            self.register.edt_ph_H2O_analysis.setText(self.register.table_grid_analysis.item(current_row, 18).text())
            self.register.edt_ph_CaCl2_analysis.setText(self.register.table_grid_analysis.item(current_row, 19).text())
            self.register.edt_clay_analysis.setText(self.register.table_grid_analysis.item(current_row, 20).text())
            self.register.edt_MO_analysis.setText(self.register.table_grid_analysis.item(current_row, 21).text())
            self.register.edt_CO_analysis.setText(self.register.table_grid_analysis.item(current_row, 22).text())
            self.register.edt_K_cmolc_analysis.setText(self.register.table_grid_analysis.item(current_row, 23).text())
            self.register.edt_Ca_analysis.setText(self.register.table_grid_analysis.item(current_row, 24).text())
            self.register.edt_Mg_analysis.setText(self.register.table_grid_analysis.item(current_row, 25).text())
            self.register.edt_Al_analysis.setText(self.register.table_grid_analysis.item(current_row, 26).text())
            self.register.edt_H_Al_analysis.setText(self.register.table_grid_analysis.item(current_row, 27).text())
            self.register.edt_SB_analysis.setText(self.register.table_grid_analysis.item(current_row, 28).text())
            self.register.edt_t_effective_CTC_analysis.setText(self.register.table_grid_analysis.item(current_row, 29).text())
            self.register.edt_T_analysis.setText(self.register.table_grid_analysis.item(current_row, 30).text())
            self.register.edt_V_analysis.setText(self.register.table_grid_analysis.item(current_row, 31).text())
            self.register.edt_m_analysis.setText(self.register.table_grid_analysis.item(current_row, 32).text())
            self.register.edt_P_meh_analysis.setText(self.register.table_grid_analysis.item(current_row, 33).text())
            self.register.edt_P_rem_analysis.setText(self.register.table_grid_analysis.item(current_row, 34).text())
            self.register.edt_Na_analysis.setText(self.register.table_grid_analysis.item(current_row, 35).text())
            self.register.edt_K_mg_analysis.setText(self.register.table_grid_analysis.item(current_row, 36).text())
            self.register.edt_S_SO4_analysis.setText(self.register.table_grid_analysis.item(current_row, 37).text())
            self.register.edt_B_analysis.setText(self.register.table_grid_analysis.item(current_row, 38).text())
            self.register.edt_Cu_analysis.setText(self.register.table_grid_analysis.item(current_row, 39).text())
            self.register.edt_Fe_analysis.setText(self.register.table_grid_analysis.item(current_row, 40).text())
            self.register.edt_Mn_analysis.setText(self.register.table_grid_analysis.item(current_row, 41).text())
            self.register.edt_Zn_analysis.setText(self.register.table_grid_analysis.item(current_row, 42).text())
            self.register.edt_limestone_analysis.setText(self.register.table_grid_analysis.item(current_row, 43).text())
            self.register.edt_prnt_analysis.setText(self.register.table_grid_analysis.item(current_row, 44).text())
            self.register.edt_plaster_analysis.setText(self.register.table_grid_analysis.item(current_row, 45).text())
            self.register.edt_tca_analysis.setText(self.register.table_grid_analysis.item(current_row, 46).text())
            self.register.edt_pre_sowing_fertilizer_analysis.setText(self.register.table_grid_analysis.item(current_row, 47).text())
            self.register.edt_pre_sowing_N_analysis.setText(self.register.table_grid_analysis.item(current_row, 48).text())
            self.register.edt_pre_sowing_P2O5_analysis.setText(self.register.table_grid_analysis.item(current_row, 49).text())
            self.register.edt_pre_sowing_K2O_analysis.setText(self.register.table_grid_analysis.item(current_row, 50).text())

            self.register.edt_pre_sowing_N_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 51).text()))
            self.register.edt_pre_sowing_P2O5_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 52).text()))
            self.register.edt_pre_sowing_K2O_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 53).text()))

            self.register.edt_planting_fertilizer_analysis.setText(self.register.table_grid_analysis.item(current_row, 54).text())
            self.register.edt_planting_fertilizer_N_analysis.setText(self.register.table_grid_analysis.item(current_row, 55).text())
            self.register.edt_planting_fertilizer_P2O5_analysis.setText(self.register.table_grid_analysis.item(current_row, 56).text())
            self.register.edt_planting_fertilizer_K2O_analysis.setText(self.register.table_grid_analysis.item(current_row, 57).text())
            
            self.register.edt_planting_fertilizer_N_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 58).text()))
            self.register.edt_planting_fertilizer_P2O5_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 59).text()))
            self.register.edt_planting_fertilizer_K2O_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 60).text()))

            self.register.edt_top_dressing_analysis.setText(self.register.table_grid_analysis.item(current_row, 61).text())
            self.register.edt_top_dressing_N_analysis.setText(self.register.table_grid_analysis.item(current_row, 62).text())
            self.register.edt_top_dressing_P2O5_analysis.setText(self.register.table_grid_analysis.item(current_row, 63).text())
            self.register.edt_top_dressing_K2O_analysis.setText(self.register.table_grid_analysis.item(current_row, 64).text())

            self.register.edt_top_dressing_N_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 65).text()))
            self.register.edt_top_dressing_P2O5_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 66).text()))
            self.register.edt_top_dressing_K2O_analysis_KG.setText(format_float(self.register.table_grid_analysis.item(current_row, 67).text()))

            self.register.edt_micro_analysis.setText(self.register.table_grid_analysis.item(current_row, 68).text())
            self.register.edt_micro_zn_analysis.setText(self.register.table_grid_analysis.item(current_row, 69).text())
            self.register.edt_micro_b_analysis.setText(self.register.table_grid_analysis.item(current_row, 70).text())
            self.register.edt_micro_cu_analysis.setText(self.register.table_grid_analysis.item(current_row, 71).text())
            self.register.edt_micro_mn_analysis.setText(self.register.table_grid_analysis.item(current_row, 72).text())
            self.register.edt_micro_mo_analysis.setText(self.register.table_grid_analysis.item(current_row, 73).text())
            self.register.edt_micro_co_analysis.setText(self.register.table_grid_analysis.item(current_row, 74).text())
            self.register.edt_micro_ca_analysis.setText(self.register.table_grid_analysis.item(current_row, 75).text())
            self.register.edt_micro_s_analysis.setText(self.register.table_grid_analysis.item(current_row, 76).text())

            self.register.edt_micro_zn_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 77).text()))
            self.register.edt_micro_b_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 78).text()))
            self.register.edt_micro_cu_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 79).text()))
            self.register.edt_micro_mn_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 80).text()))
            self.register.edt_micro_mo_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 81).text()))
            self.register.edt_micro_co_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 82).text()))
            self.register.edt_micro_ca_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 83).text()))
            self.register.edt_micro_s_analysis_kg.setText(format_float(self.register.table_grid_analysis.item(current_row, 84).text()))

            if self.register.table_grid_analysis.item(current_row, 85) is not None:
               self.register.lbl_name_user_analysis.setText(self.register.table_grid_analysis.item(current_row, 85).text())
            else:
               self.register.lbl_name_user_analysis.setText('')

   def generate_sql_query(self):
      sql = """        Select
                       a.code_analysis,
                       a.code_producer,
                       p.name_producer,
                       a.sector_analysis,
                       a.agricultural_period_analysis,
                       a.culture_analysis,
                       a.area_analysis,
                       a.altitude_analysis,
                       a.latitude_analysis,
                       a.longitude_analysis,
                       a.planting_system_analysis,
                       a.average_productivity_analysis,
                       a.minimum_temperature_analysis ,
                       a.maximum_temperature_analysis ,
                       a.rain_vegetative_analysis,
                       a.rain_reproductive_analysis,
                       a.initial_depth_analysis,
                       a.final_depth_analysis,
                       a.ph_H2O_analysis,
                       a.ph_CaCl2_analysis ,
                       a.clay_analysis,
                       a.MO_analysis,
                       a.CO_analysis,
                       a.K_cmolc_analysis,
                       a.Ca_analysis,
                       a.Mg_analysis,
                       a.Al_analysis,
                       a.H_Al_analysis,
                       a.SB_analysis,
                       a.t_effective_CTC_analysis,
                       a.T_analysis,
                       a.V_analysis,
                       a.m_analysis,
                       a.P_meh_analysis ,
                       a.P_rem_analysis ,
                       a.Na_analysis,
                       a.K_mg_analysis,
                       a.S_SO4_analysis,
                       a.B_analysis,
                       a.Cu_analysis,
                       a.Fe_analysis,
                       a.Mn_analysis,
                       a.Zn_analysis,
                       a.limestone_analysis,
                       a.prnt_analysis,
                       a.plaster_analysis,
                       a.tca_analysis,
                       a.pre_sowing_fertilizer_analysis,
                       a.pre_sowing_N_analysis,
                       a.pre_sowing_P2O5_analysis,
                       a.pre_sowing_K2O_analysis,
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_N_analysis/100.00)) as pre_sowing_N_analysis_kg,
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_P2O5_analysis/100.00)) as pre_sowing_P2O5_analysis_kg,
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_K2O_analysis/100.00)) as pre_sowing_K2O_analysis_kg,
                       a.seeding_fertilizer_analysis,
                       a.seeding_N_analysis,
                       a.seeding_P2O5_analysis,
                       a.seeding_K2O_analysis,
                       (a.seeding_fertilizer_analysis * (a.seeding_N_analysis/100.00)) as seeding_N_analysis_kg,
                       (a.seeding_fertilizer_analysis * (a.seeding_P2O5_analysis/100.00)) as seeding_P2O5_analysis_kg,
                       (a.seeding_fertilizer_analysis * (a.seeding_K2O_analysis/100.00)) as seeding_K2O_analysis_kg,
                       a.top_dressing_fertilizer_analysis,
                       a.top_dressing_N_analysis,
                       a.top_dressing_P2O5_analysis,
                       a.top_dressing_K2O_analysis,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_N_analysis/100.00)) as top_dressing_N_analysis_kg,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_P2O5_analysis/100.00)) as top_dressing_P2O5_analysis_kg,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_K2O_analysis/100.00)) as top_dressing_K2O_analysis_kg,
                       a.micro_analysis,
                       a.micro_zn_analysis,
                       a.micro_b_analysis,
                       a.micro_cu_analysis,
                       a.micro_mn_analysis,
                       a.micro_mo_analysis,
                       a.micro_co_analysis,
                       a.micro_ca_analysis,
                       a.micro_s_analysis,
                       (a.micro_analysis * (a.micro_zn_analysis/100.00)) as micro_zn_analysis_kg,
                       (a.micro_analysis * (a.micro_b_analysis/100.00)) as micro_b_analysis_kg,
                       (a.micro_analysis * (a.micro_cu_analysis/100.00)) as micro_cu_analysis_kg,
                       (a.micro_analysis * (a.micro_mn_analysis/100.00)) as micro_mn_analysis_kg,
                       (a.micro_analysis * (a.micro_mo_analysis/100.00)) as micro_mo_analysis_kg,
                       (a.micro_analysis * (a.micro_co_analysis/100.00)) as micro_co_analysis_kg,
                       (a.micro_analysis * (a.micro_ca_analysis/100.00)) as micro_ca_analysis_kg,
                       (a.micro_analysis * (a.micro_s_analysis/100.00)) as micro_s_analysis_kg,
                       u.name_user
                       From analysis a left join producer p on a.code_producer = p.code_producer
                                       left join user     u on a.code_user     = u.code_user
                       Where p.name_producer LIKE '"""+self.register.edt_query_analysis.text()+"%'"
      
      harvest, culture, planting_system, ordering = '', '', '', ''
      if (self.register.cbx_query_agricultural_period_analysis.currentText()=='ESPECIFICAR') and (self.register.edt_query_agricultural_period_analysis.text()!='/'):
         harvest = ' and a.agricultural_period_analysis = "'+ self.register.edt_query_agricultural_period_analysis.text() + '"'

      if self.register.cbx_query_culture_analysis.currentText() in ('Feijão','Milho','Soja','Sorgo','Trigo'):
         culture = ' and a.culture_analysis = "'+ self.register.cbx_query_culture_analysis.currentText() + '"'

      if self.register.cbx_query_planting_system_analysis.currentText() in ('CONVENCIONAL - IRRIGADO', 'CONVENCIONAL - SEQUEIRO', 'PLANTIO DIRETO - IRRIGADO', 'PLANTIO DIRETO - SEQUEIRO'):
         planting_system = ' and a.planting_system_analysis = "'+ self.register.cbx_query_planting_system_analysis.currentText() + '"'

      if self.register.cbx_query_ordering_analysis.currentText() == 'CULTURA':
         ordering = ' Order By a.culture_analysis, p.name_producer, a.agricultural_period_analysis, a.planting_system_analysis'
      elif self.register.cbx_query_ordering_analysis.currentText() == 'SAFRA':
         ordering = ' Order By a.agricultural_period_analysis, p.name_producer, a.culture_analysis, a.planting_system_analysis'
      elif self.register.cbx_query_ordering_analysis.currentText() == 'SIST. DE PLANTIO':
         ordering = ' Order By a.planting_system_analysis, p.name_producer, a.culture_analysis, a.agricultural_period_analysis'
      else:
         ordering = ' Order By p.name_producer, a.culture_analysis, a.agricultural_period_analysis, a.planting_system_analysis'

      return sql + harvest + culture + planting_system + ordering

   def run_interpretation(self):
      if validates_float(self.register.edt_clay_analysis.text()) > 0:
         if (validates_float(self.register.edt_final_depth_analysis.text()) > 0) and (validates_float(self.register.edt_final_depth_analysis.text()) > validates_float(self.register.edt_initial_depth_analysis.text())):         
            f = FifthApproximation()
            micros, npk_clay, npk_p_rem, limestone, plaster, saturation = {}, {}, {}, {}, {}, {}
            expected_saturation = 0
            dataset = self.search_attributes_interpreted()

            soil_attributes = self.interpretation_soil_attributes(f, dataset)

            parameters = self.parameterization_attributes(f, dataset, soil_attributes)

            p_rating = [(line[1], line[3]) for line in soil_attributes if line[0][0] == 'P']
            k_rating = [line[1] for line in soil_attributes if line[0][0] == 'K']

            if dataset['CULTURA'] != c.BEAN:
               micros = f.micronutrient_fertilizer(dataset['CULTURA'], soil_attributes)

            if dataset['CULTURA'] == c.WHEAT:
               self.register.npk_wheat.exec()
               if self.register.npk_wheat.confirm_registration == True:
                  npk_clay = self.fertilizer_wheat(f, micros, dataset['CULTURA'], p_rating[0][0], dataset['ARGILA'], dataset['K'], dataset['ALTITUDE'], parameters['rainfed_irrigated'], soil_attributes, c.CLAY)
                  expected_saturation = validates_float(self.register.npk_wheat.edt_V.text())  
                  if self.register.npk_wheat.ckb_limestone_recommendation.isChecked() == True:
                     limestone = self.limestone_recommendation(f, expected_saturation)
                  if self.register.npk_wheat.ckb_plaster_recommendation.isChecked() == True:
                     plaster = self.plaster_recommendation(f, expected_saturation)

            elif dataset['CULTURA'] == c.BEAN:
               self.register.bean_technology.exec()
               if self.register.bean_technology.confirm_registration == True:
                  if 'NT1' in self.register.bean_technology.cbx_technology_level.currentText():
                     technology_level = 'NT1'
                  elif 'NT2' in self.register.bean_technology.cbx_technology_level.currentText():
                     technology_level = 'NT2'
                  elif 'NT3' in self.register.bean_technology.cbx_technology_level.currentText():
                     technology_level = 'NT3'
                  elif 'NT4' in self.register.bean_technology.cbx_technology_level.currentText():
                     technology_level = 'NT4'
                  else:
                     technology_level = 'NT1'
                  micros = f.micronutrient_fertilizer(dataset['CULTURA'], soil_attributes, technology_level)
                  npk_clay = self.fertilizer_bean(f, dataset['CULTURA'], p_rating[0][0], k_rating[0], soil_attributes, c.CLAY, technology_level)

                  if dataset['P-REM'] > 0:
                     npk_p_rem = self.fertilizer_bean(f, dataset['CULTURA'], p_rating[1][0], k_rating[0], soil_attributes, c.P_REM, technology_level)

                  expected_saturation = validates_float(self.register.bean_technology.edt_V.text())  
                  if self.register.bean_technology.ckb_limestone_recommendation.isChecked() == True:
                     limestone = self.limestone_recommendation(f, expected_saturation)
                  if self.register.bean_technology.ckb_plaster_recommendation.isChecked() == True:
                     plaster = self.plaster_recommendation(f, expected_saturation)

            elif dataset['CULTURA'] in (c.CORN, c.SORGHUM):
               self.register.succession_planting.exec()
               if self.register.succession_planting.confirm_registration == True:
                  npk_clay = self.fertilizer_corn_sorghum(f,dataset['CULTURA'], p_rating[0][0], k_rating[0], parameters['planting'], soil_attributes, c.CLAY)

                  if dataset['P-REM'] > 0:
                     npk_p_rem = self.fertilizer_corn_sorghum(f, dataset['CULTURA'], p_rating[1][0], k_rating[0], parameters['planting'], soil_attributes, c.P_REM)

                  expected_saturation = validates_float(self.register.succession_planting.edt_V.text())  
                  if self.register.succession_planting.ckb_limestone_recommendation.isChecked() == True:
                     limestone = self.limestone_recommendation(f, expected_saturation)
                  if self.register.succession_planting.ckb_plaster_recommendation.isChecked() == True:
                     plaster = self.plaster_recommendation(f, expected_saturation)

            else:   
               self.register.limestone_plaster_soy.exec()
               if self.register.limestone_plaster_soy.confirm_registration == True:
                  npk_clay = self.fertilizer_soy(f, dataset['CULTURA'], p_rating[0][0], k_rating[0], parameters['planting'], soil_attributes, c.CLAY)
   
                  if dataset['P-REM'] > 0:
                     npk_p_rem = self.fertilizer_soy(f, dataset['CULTURA'], p_rating[1][0], k_rating[0], parameters['planting'], soil_attributes, c.P_REM)

                  expected_saturation = validates_float(self.register.limestone_plaster_soy.edt_V.text())  
                  if self.register.limestone_plaster_soy.ckb_limestone_recommendation.isChecked() == True:
                     limestone = self.limestone_recommendation(f, expected_saturation)
                  if self.register.limestone_plaster_soy.ckb_plaster_recommendation.isChecked() == True:
                     plaster = self.plaster_recommendation(f, expected_saturation)


            report_header = {}
            report_header['title'] = 'Relatório de interpretação da fertilidade do solo.'
            report_header['producer'] = self.register.edt_name_producer_analysis.text()
            report_header['plots'] = self.register.edt_sector_analysis.text()
            report_header['period'] = self.register.edt_agricultural_period_analysis.text()
            report_header['area'] = self.register.edt_area_analysis.text()
            report_header['altitude'] = self.register.edt_altitude_analysis.text()
            report_header['planting_system'] = self.register.cbx_planting_system_analysis.currentText()

            filename = c.INTERPRETATION_REPORT

            saturation = f.search_saturation(dataset['CULTURA']) 
            if expected_saturation <= 0:
               expected_saturation = saturation['V']

            initial_depth = validates_float(self.register.edt_initial_depth_analysis.text())
            final_depth =  validates_float(self.register.edt_final_depth_analysis.text())
            prnt = validates_float(self.register.edt_prnt_analysis.text())
            tca = validates_float(self.register.edt_tca_analysis.text())

            r = InterpretationReport(initial_depth, final_depth, prnt, tca,
                                     saturation, expected_saturation, soil_attributes, 
                                     filename, micros, npk_clay, npk_p_rem,
                                     limestone, plaster, report_header)
            r.generate_report()
         else:
            message('erro', 'Os campos de profundidade "P. Inicial" e "P. Final" está inconsistente.')
      else:
         message('erro', 'O campo "Argila" é obrigatorio.')

   def search_attributes_interpreted(self):
      dataset = { 'pH-H2O': validates_float(self.register.edt_ph_H2O_analysis.text()),
                  'pH-CaCl2': validates_float(self.register.edt_ph_CaCl2_analysis.text()),
                  'CO': validates_float(self.register.edt_CO_analysis.text()),
                  'MO': validates_float(self.register.edt_MO_analysis.text()),
                  'Ca2+': validates_float(self.register.edt_Ca_analysis.text()),
                  'Mg2+': validates_float(self.register.edt_Mg_analysis.text()),
                  'Al3+': validates_float(self.register.edt_Al_analysis.text()),
                  'SB': validates_float(self.register.edt_SB_analysis.text()),
                  'H+Al': validates_float(self.register.edt_H_Al_analysis.text()),
                  't': validates_float(self.register.edt_t_effective_CTC_analysis.text()),
                  'T': validates_float(self.register.edt_T_analysis.text()),
                  'm': validates_float(self.register.edt_m_analysis.text()),
                  'V': validates_float(self.register.edt_V_analysis.text()),
                  'K': validates_float(self.register.edt_K_mg_analysis.text()),
                  'Zn': validates_float(self.register.edt_Zn_analysis.text()),
                  'Mn': validates_float(self.register.edt_Mn_analysis.text()),
                  'Fe': validates_float(self.register.edt_Fe_analysis.text()),
                  'Cu': validates_float(self.register.edt_Cu_analysis.text()),
                  'B': validates_float(self.register.edt_B_analysis.text()), 
                  'P': validates_float(self.register.edt_P_meh_analysis.text()),
                  'P-REM': validates_float(self.register.edt_P_rem_analysis.text()),
                  'ARGILA': validates_float(self.register.edt_clay_analysis.text())/10,
                  'S': validates_float(self.register.edt_S_SO4_analysis.text()),
                  'CULTURA': self.register.cbx_culture_analysis.currentText(),
                  'ALTITUDE': validates_float(self.register.edt_altitude_analysis.text()),
                  'SISTEMA': self.register.cbx_planting_system_analysis.currentText(),
                  'P-INICIAL': validates_float(self.register.edt_initial_depth_analysis.text()),
                  'P-FINAL': validates_float(self.register.edt_final_depth_analysis.text()),
                  'PRNT': validates_float(self.register.edt_prnt_analysis.text()),
                  'T-Ca': validates_float(self.register.edt_tca_analysis.text()) 
                  }
      return dataset

   def interpretation_soil_attributes(self, f, dataset):
      attributes=[]
      for field, value in dataset.items():
         if field not in ('P', 'P-REM', 'ARGILA', 'S', 'CULTURA', 'ALTITUDE', 'SISTEMA', 'P-INICIAL', 'P-FINAL', 'PRNT', 'T-Ca'):
            attributes.append(f.availability_soil_attributes(field, value))
      return attributes

   def parameterization_attributes(self, f, dataset, soil_attributes):
         parameters = {}
         
         if c.IRRIGATED in (dataset['SISTEMA']):
            parameters['rainfed_irrigated'] = c.IRRIGATED
         else:
            parameters['rainfed_irrigated'] = c.RAINFED    

         if c.DIRECT_PLANTING in (dataset['SISTEMA']):
            parameters['planting'] = c.DIRECT_PLANTING
         else:
            parameters['planting'] = c.CONVENTIONAL_PLANTING   

         if dataset['CULTURA'] == c.WHEAT:
            p_result = f.p_availability_wheat(dataset['ARGILA'], dataset['P'])
            soil_attributes.append(p_result)
         else:
            p_result = f.p_availability(dataset['ARGILA'], dataset['P-REM'], dataset['P'])
            soil_attributes.append(p_result[0])
            if dataset['P-REM'] > 0:
               soil_attributes.append(p_result[1])
      
         if dataset['P-REM'] > 0:
            s_result = f.s_availability(dataset['P-REM'], dataset['S'])
            soil_attributes.append(s_result)
         
         return parameters

   def fertilizer_wheat(self, f, micros, culture, p, clay, k, altitude, rainfed_irrigated, soil_attributes, clay_p_rem):
         if self.register.npk_wheat.cbx_phosphate_fertilizer.currentIndex() == 1:
            phosphate_fertilizer = c.GRADUAL_FERTILIZATION
         else:
            phosphate_fertilizer = c.TOTAL_FERTILIZATION  

         if self.register.npk_wheat.cbx_cultivar_size.currentIndex() == 1:
            cultivar_size = c.LOW_AVAILABILITY
         else:
            cultivar_size = c.HIGH_AVAILABILITY   

         if self.register.npk_wheat.ckb_previous_culture_corn.isChecked() == True:
            previous_culture_corn = c.CONFIRMED
         else:
            previous_culture_corn = c.NOT_CONFIRMED   
  
         npk_fertilizing = f.npk_wheat(phosphate_fertilizer, p, clay, rainfed_irrigated, k, cultivar_size, previous_culture_corn, altitude)

         fertilizing = {}
         fertilizing['N'] = npk_fertilizing[0]
         fertilizing['P'] = npk_fertilizing[1]
         fertilizing['k'] = npk_fertilizing[2]
         
         if npk_fertilizing[3] > 0:
            micros['B'] = npk_fertilizing[3]

         fertilizing['technology_level'] = ''
         fertilizing['clay_p_rem'] = clay_p_rem
         fertilizing['culture'] = culture

         return fertilizing

   def fertilizer_bean(self, f, culture, p, k, soil_attributes, clay_p_rem, technology_level): 
         npk_fertilizing = f.npk(culture, p, k, technology_level, c.NOT_CONFIRMED)
         fertilizing = {}
         fertilizing['N'] = npk_fertilizing[0]
         fertilizing['P'] = npk_fertilizing[1]
         fertilizing['k'] = npk_fertilizing[2]
         fertilizing['technology_level'] = npk_fertilizing[3]
         fertilizing['clay_p_rem'] = clay_p_rem
         fertilizing['culture'] = culture
         return fertilizing

   def fertilizer_corn_sorghum(self, f, culture, p, k, planting, soil_attributes, clay_p_rem):
         if self.register.succession_planting.ckb_succession_planting.isChecked() == True:
            succession_planting = c.CONFIRMED
         else:
            succession_planting = c.NOT_CONFIRMED
  
         npk_fertilizing = f.npk(culture, p, k, planting, succession_planting)
      
         fertilizing = {}
         fertilizing['N'] = npk_fertilizing[0]
         fertilizing['P'] = npk_fertilizing[1]
         fertilizing['k'] = npk_fertilizing[2]
         fertilizing['technology_level'] = ''
         fertilizing['clay_p_rem'] = clay_p_rem
         fertilizing['culture'] = culture

         return fertilizing

   def fertilizer_soy(self, f, culture, p, k, planting, soil_attributes, clay_p_rem):
         npk_fertilizing = f.npk(culture, p, k, planting, c.NOT_CONFIRMED)
         
         fertilizing = {}
         fertilizing['N'] = npk_fertilizing[0]
         fertilizing['P'] = npk_fertilizing[1]
         fertilizing['k'] = npk_fertilizing[2]
         fertilizing['technology_level'] = ''
         fertilizing['clay_p_rem'] = clay_p_rem
         fertilizing['culture'] = culture

         return fertilizing

   def limestone_recommendation(self, f, ve):
      result_amount_limestone = {}
      
      if validates_float(self.register.edt_prnt_analysis.text()) > 0: 

         dataset = self.search_attributes_interpreted()

         saturation = f.search_saturation(dataset['CULTURA'])
         x = saturation['X']
         if ve <= 0:
            ve = saturation['V']
         qc_bs=0
         if (dataset['SB'] > 0) and (dataset['T'] > 0):
            nc_bs = f.base_saturation(dataset['SB'], dataset['T'], ve) 
            qc_bs = f.amount_limestone(nc_bs, 100, dataset['P-INICIAL'], dataset['P-FINAL'], dataset['PRNT'])

         if (dataset['Al3+'] >= 0) and (dataset['m'] >= 0) and (dataset['t'] > 0) and (dataset['Ca2+'] > 0) and (dataset['Mg2+'] > 0):
            nc_clay, nc_p_rem = f.neutralization_Al_elevation_Ca_Mg(dataset['ARGILA'],
                                                                        dataset['P-REM'],
                                                                        dataset['Al3+'],
                                                                        dataset['m'],
                                                                        dataset['t'],
                                                                        x,
                                                                        dataset['Ca2+'],
                                                                        dataset['Mg2+'])

            qc_clay = f.amount_limestone(nc_clay, 100, dataset['P-INICIAL'], dataset['P-FINAL'], dataset['PRNT'])
            qc_p_rem = f.amount_limestone(nc_p_rem, 100, dataset['P-INICIAL'], dataset['P-FINAL'], dataset['PRNT'])
         else:
            qc_clay = 0
            qc_p_rem = 0

         result_amount_limestone[c.CLAY] = qc_clay
         result_amount_limestone[c.P_REM] = qc_p_rem
         result_amount_limestone[c.BASE_SATURATION] = qc_bs
      
      return result_amount_limestone

   def plaster_recommendation(self, f, ve):

      result_amount_plaster = {}
      dataset = self.search_attributes_interpreted()

      ng_clay = f.need_plaster_clay(dataset['ARGILA'])
      qg_clay = f.amount_plaster(ng_clay, 100, dataset['P-INICIAL'], dataset['P-FINAL'])
      
      ng_p_rem = f.need_plaster_p_rem(dataset['P-REM'], dataset['T-Ca'])
      qg_p_rem = f.amount_plaster(ng_p_rem, 100, dataset['P-INICIAL'], dataset['P-FINAL'])

      saturation = f.search_saturation(dataset['CULTURA'])
      x = saturation['X']
      if ve <= 0:
         ve = saturation['V']
      nc_bs=0
      if (dataset['SB'] > 0) and (dataset['T'] > 0):
         nc_bs = f.base_saturation(dataset['SB'], dataset['T'], ve) 

      if (dataset['Al3+'] >= 0) and (dataset['m'] >= 0) and (dataset['t'] > 0) and (dataset['Ca2+'] > 0) and (dataset['Mg2+'] > 0):
         nc_clay, nc_p_rem = f.neutralization_Al_elevation_Ca_Mg(dataset['ARGILA'],
                                                                        dataset['P-REM'],
                                                                        dataset['Al3+'],
                                                                        dataset['m'],
                                                                        dataset['t'],
                                                                        x,
                                                                        dataset['Ca2+'],
                                                                        dataset['Mg2+'])
      else:
         nc_clay = 0
         nc_p_rem = 0

      ng_nc_clay = f.need_plaster_nc(nc_clay)
      qg_nc_clay = f.amount_plaster(ng_nc_clay, 100, dataset['P-INICIAL'], dataset['P-FINAL'])
      
      ng_nc_p_rem = f.need_plaster_nc(nc_p_rem)
      qg_nc_p_rem = f.amount_plaster(ng_nc_p_rem, 100, dataset['P-INICIAL'], dataset['P-FINAL'])

      ng_nc_bs = f.need_plaster_nc(nc_bs)
      qg_nc_bs = f.amount_plaster(ng_nc_bs, 100, dataset['P-INICIAL'], dataset['P-FINAL'])
      
      result_amount_plaster[c.CLAY] = qg_clay
      result_amount_plaster[c.P_REM] = qg_p_rem
      result_amount_plaster[c.NC_PLASTER_CLAY] = qg_nc_clay
      result_amount_plaster[c.NC_PLASTER_P_REM] = qg_nc_p_rem
      result_amount_plaster[c.NC_PLASTER_BS] = qg_nc_bs

      return result_amount_plaster

   def calculate_bases(self):
      ca = validates_float(self.register.edt_Ca_analysis.text())
      mg = validates_float(self.register.edt_Mg_analysis.text())
      k = validates_float(self.register.edt_K_cmolc_analysis.text())
      al = validates_float(self.register.edt_Al_analysis.text())
      ctc_ph7 = validates_float(self.register.edt_T_analysis.text())

      sb = ca + mg + k
      
      t = ca + mg + k + al
      
      if t > 0:
         m = ( al * 100 ) / t
      else:
         m = 0   
      
      if ctc_ph7 > 0:
         v = ( sb * 100 ) / ctc_ph7
      else:
         v = 0
      
      h_al = ctc_ph7 - sb
      
      self.register.edt_SB_analysis.setText(format_float(sb))
      self.register.edt_t_effective_CTC_analysis.setText(format_float(t))
      self.register.edt_m_analysis.setText(format_float(m))
      self.register.edt_V_analysis.setText(format_float(v))
      self.register.edt_H_Al_analysis.setText(format_float(h_al)) 

   def convert_K_cmolc_to_mg_dm3(self):
      k_cmolc = validates_float(self.register.edt_K_cmolc_analysis.text())
      k_mg_dm3 = 0
      if k_cmolc > 0:
         k_mg_dm3 = k_cmolc * 391
      return k_mg_dm3
   

   

