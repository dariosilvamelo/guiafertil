
import os

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

import constants
from tools import format_float


class AnalysisReportPdf:
    def __init__(self, filename, dataset, title):
        self.filename = filename
        self.data = dataset
        self.logo_filename = constants.LOGO_REPORT
        self.titleReport = title
        self.page_width, self.page_height = landscape(A4)
        self.c = canvas.Canvas(filename, pagesize=(self.page_width, self.page_height))
        self.c.setFillColor("black")
        self.label_font_type = "Courier-Bold"
        self.value_font_type = "Courier"
        self.font_size = 9
        self.line_spacing = 3.5
        self.line_position = self.point_to_mm(self.page_height) - self.line_spacing
        self.page = 1
        self.end_page = 7
        self.columns = [5,34,63,93,120,149,178,207,236,265]
        self.label = {
                      "code_analysis"                : "Cód. Análise",
                      "code_producer"                : "Código",
                      "name_producer"                : "Produtor",
                      "agricultural_period_analysis" : "Safra agríc.",
                      "culture_analysis"             : "Cultura",
                      "area_analysis"                : "Área-ha",
                      "altitude_analysis"            : "Altitude",
                      "latitude_analysis"            : "Latitude",
                      "longitude_analysis"           : "Londitude",
                      "planting_system_analysis"     : "S. Plantio",
                      "average_productivity_analysis": "Média-60kg",
                      "minimum_temperature_analysis" : "Temp. Mín C°",
                      "maximum_temperature_analysis" : "Temp. Máx C°",
                      "rain_vegetative_analysis"     : "Chuva V.-mm",
                      "rain_reproductive_analysis"   : "Chuva R.-mm",
                      "initial_depth_analysis"       : "P. Inic.-cm",
                      "final_depth_analysis"         : "P. Final-cm",
                      "ph_H2O_analysis"              : "pH:H2O-1:2,5:",
                      "ph_CaCl2_analysis"            : "pH:CaCl2-1:2,5:",
                      "clay_analysis"                : "Argila-g/kg.:",
                      "MO_analysis"                  : "MO-g/dm3....:",
                      "CO_analysis"                  : "CO-g/dm3....:",
                      "K_cmolc_analysis"             : "K-cmolc/dm3",
                      "Ca_analysis"                  : "Ca-cmolc/dm3",
                      "Mg_analysis"                  : "Mg-cmolc/dm3",
                      "Al_analysis"                  : "Al-cmolc/dm3",
                      "H_Al_analysis"                : "H+Al-cmolc/dm3",
                      "SB_analysis"                  : "SB-cmolc/dm3",
                      "t_effective_CTC_analysis"     : "t-cmolc/dm3",
                      "T_analysis"                   : "T-cmolc/dm3",
                      "V_analysis"                   : "V-%",
                      "m_analysis"                   : "m-%",
                      "P_meh_analysis"               : "P-mg/dm3",
                      "P_rem_analysis"               : "P rem-mg/dm3",
                      "Na_analysis"                  : "Na-mg/dm3",
                      "K_mg_analysis"                : "K-mg/dm3",
                      "S_SO4_analysis"               : "S-SO4-mg/dm3",
                      "B_analysis"                   : "B-mg/dm3",
                      "Cu_analysis"                  : "Cu-mg/dm3",
                      "Fe_analysis"                  : "Fe-mg/dm3",
                      "Mn_analysis"                  : "Mn-mg/dm3",
                      "Zn_analysis"                  : "Zn-mg/dm3",
                      "limestone_analysis"           : "Calc.-kg/ha",
                      "plaster_analysis"             : "Gesso-kg-ha",
                      "pre_sowing"                   : "Pré-Sem....:",
                      "seeding_fertilizer"           : "Plantio....:",
                      "top_dressing"                 : "Cobertura..:",
                      "NPK_analysis"                 : "NPK(kg/ha)",
                      "N_analysis"                   : "N(%)",
                      "P2O5_analysis"                : "P2O5(%)",
                      "K2O_analysis"                 : "K2O(%)",
                      "N_analysis_kg"                : "N(kg/ha)",
                      "P2O5_analysis_kg"             : "P2O5(kg/ha)",
                      "K2O_analysis_kg"              : "K2O(kg/ha)",
                      "sector_analysis"              : "Talhão",
                      "micro_nutrients_analysis"     : "Micros kg/ha:",
                      "micro_zn_analysis"            : "Zn",
                      "micro_b_analysis"             : "B",
                      "micro_cu_analysis"            : "Cu",
                      "micro_mn_analysis"            : "Mn",
                      "micro_mo_analysis"            : "Mo",
                      "micro_co_analysis"            : "Co",
                      "micro_ca_analysis"            : "Ca",
                      "micro_s_analysis"             : "S",
                      "prnt_analysis"                : "PRNT-%",
                      "tca_analysis"                 : "TCA-%",
                      "name_user"                    : "Usuário.....:"
                     }

    def point_to_mm(self, point):
        return point * 25.4 / 72

    def mm_to_point(self, mm):
        return mm * 72 / 25

    def report_header(self):
        self.c.setFont(self.label_font_type, self.font_size)
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawImage(self.logo_filename, self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), width=125, height=50)
        self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position + self.line_spacing), self.titleReport)
        self.line_position = self.line_position - self.line_spacing

    def generate_report(self):
        self.report_header()
        total_lines = self.data.shape[0]
        total_items = len(self.data)
        for index, field in self.data.iterrows():
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['code_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['code_producer'])
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['name_producer'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['agricultural_period_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['culture_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['area_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['altitude_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['latitude_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['longitude_analysis'])
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['code_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['code_producer']))
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), field['name_producer'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), field['agricultural_period_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), field['culture_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['area_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['altitude_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), field['latitude_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), field['longitude_analysis'])

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['sector_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['average_productivity_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['planting_system_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['minimum_temperature_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['maximum_temperature_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['rain_vegetative_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['rain_reproductive_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['initial_depth_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['final_depth_analysis'])
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['sector_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['average_productivity_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), field['planting_system_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['minimum_temperature_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['maximum_temperature_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['rain_vegetative_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['rain_reproductive_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), str(field['initial_depth_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), str(field['final_depth_analysis']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing

            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['ph_H2O_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['ph_H2O_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['ph_CaCl2_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['ph_CaCl2_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['MO_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['MO_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['CO_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['CO_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['clay_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), str(field['clay_analysis']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['K_cmolc_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Ca_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Mg_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Al_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['H_Al_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['SB_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['t_effective_CTC_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['T_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['V_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['m_analysis'])
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['K_cmolc_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Ca_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Mg_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Al_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['H_Al_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['SB_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['t_effective_CTC_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['T_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), str(field['V_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), str(field['m_analysis']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['P_meh_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['P_rem_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Na_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), self.label['K_mg_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['S_SO4_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['B_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Cu_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Fe_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Mn_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['Zn_analysis'])
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['P_meh_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['P_rem_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Na_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['K_mg_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['S_SO4_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['B_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Cu_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Fe_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Mn_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), str(field['Zn_analysis']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['limestone_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['plaster_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), self.label['NPK_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['N_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['P2O5_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['K2O_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['N_analysis_kg'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['P2O5_analysis_kg'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['K2O_analysis_kg'])

            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['limestone_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['plaster_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['pre_sowing'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['pre_sowing_fertilizer_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['pre_sowing_N_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['pre_sowing_P2O5_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['pre_sowing_K2O_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['pre_sowing_N_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['pre_sowing_P2O5_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['pre_sowing_K2O_analysis_kg']))
            
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['prnt_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), self.label['tca_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['seeding_fertilizer'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['seeding_fertilizer_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['seeding_N_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['seeding_P2O5_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['seeding_K2O_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['seeding_N_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['seeding_P2O5_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['seeding_K2O_analysis_kg']))
            
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), str(field['prnt_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['tca_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['top_dressing'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['top_dressing_fertilizer_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['top_dressing_N_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['top_dressing_P2O5_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['top_dressing_K2O_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['top_dressing_N_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['top_dressing_P2O5_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['top_dressing_K2O_analysis_kg']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_nutrients_analysis'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_analysis']))
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_zn_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_b_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_cu_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_mn_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_mo_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_co_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_ca_analysis'])
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), self.label['micro_s_analysis'])

            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), '( % )........:')
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_zn_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_b_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_cu_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_mn_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_mo_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_co_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_ca_analysis']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), str(field['micro_s_analysis']))

            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), '( kg/ha )....:')
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_zn_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_b_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_cu_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_mn_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_mo_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[7]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_co_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[8]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_ca_analysis_kg']))
            self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field['micro_s_analysis_kg']))

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.label_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), self.label['name_user'])
            self.c.setFont(self.value_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[1]), self.mm_to_point(self.line_position-self.line_spacing), str(field['name_user']))

            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '----------------------------------------------------------------------------------------------------------------------------------------------------')

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            
            if self.line_position == self.end_page:
               self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), 'Página: '+str(self.page))
               self.page=self.page+1
               self.line_position = self.point_to_mm(self.page_height) - self.line_spacing
               if index != total_items-1:
                   self.c.showPage()
                   self.report_header()

            elif (index == (total_lines-1)):
                self.line_position = self.end_page   
                self.c.drawString(self.mm_to_point(self.columns[9]), self.mm_to_point(self.line_position-self.line_spacing), 'Página: '+str(self.page))

        self.c.save()
        try:
            os.startfile(self.filename)
        except AttributeError:
            os.system('xdg-open ' + self.filename)




