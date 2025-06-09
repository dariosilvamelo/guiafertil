import os
import sqlite3

import pandas as pd

from analysis_report_pdf import AnalysisReportPdf
from registration_report_pdf import RegistrationReportPdf
from tools import message, remention_excel_columns


class DataBaseAnalysis:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def insert_analysis(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            fields = ('code_producer',
                      'code_user',
                      'agricultural_period_analysis',
                      'culture_analysis',
                      'area_analysis',
                      'altitude_analysis',
                      'latitude_analysis',
                      'longitude_analysis',
                      'planting_system_analysis',
                      'average_productivity_analysis',
                      'minimum_temperature_analysis',
                      'maximum_temperature_analysis',
                      'rain_vegetative_analysis',
                      'rain_reproductive_analysis',
                      'initial_depth_analysis',
                      'final_depth_analysis',
                      'ph_H2O_analysis',
                      'ph_CaCl2_analysis',
                      'clay_analysis',
                      'MO_analysis',
                      'CO_analysis',
                      'K_cmolc_analysis',
                      'Ca_analysis',
                      'Mg_analysis',
                      'Al_analysis',
                      'H_Al_analysis',
                      'SB_analysis',
                      't_effective_CTC_analysis',
                      'T_analysis',
                      'V_analysis',
                      'm_analysis',
                      'P_meh_analysis',
                      'P_rem_analysis',
                      'Na_analysis',
                      'K_mg_analysis',
                      'S_SO4_analysis',
                      'B_analysis',
                      'Cu_analysis',
                      'Fe_analysis',
                      'Mn_analysis',
                      'Zn_analysis',
                      'limestone_analysis',               
  	                  'plaster_analysis',
                      'pre_sowing_fertilizer_analysis',
                      'pre_sowing_N_analysis',
                      'pre_sowing_P2O5_analysis',
                      'pre_sowing_K2O_analysis',
                      'seeding_fertilizer_analysis',
                      'seeding_N_analysis',
                      'seeding_P2O5_analysis',
                      'seeding_K2O_analysis',
                      'top_dressing_fertilizer_analysis',
                      'top_dressing_N_analysis',
                      'top_dressing_P2O5_analysis',
                      'top_dressing_K2O_analysis',
                      'sector_analysis',
                      'micro_analysis',
                      'micro_zn_analysis',
                      'micro_b_analysis',
                      'micro_cu_analysis',
                      'micro_mn_analysis',
                      'micro_mo_analysis',
                      'micro_co_analysis',
                      'micro_ca_analysis',
                      'micro_s_analysis',
                      'prnt_analysis',
                      'tca_analysis'
                      )                 
            markers = ','.join(['?'] * len(fields))
            sql = f"""INSERT INTO ANALYSIS ({', '.join(fields)}) VALUES ({markers})"""
            cursor.execute(sql, dataset)
            self.connection_data_base.commit()
            message('ok', 'Registro inserido com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def update_analysis(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = (f"""UPDATE ANALYSIS SET
                       code_producer                    = ?,
                       code_user                        = ?,
                       agricultural_period_analysis     = ?,
                       culture_analysis                 = ?,
                       area_analysis                    = ?,
                       altitude_analysis                = ?,
                       latitude_analysis                = ?,
                       longitude_analysis               = ?,
                       planting_system_analysis         = ?,
                       average_productivity_analysis    = ?,
                       minimum_temperature_analysis     = ?,
                       maximum_temperature_analysis     = ?,
                       rain_vegetative_analysis         = ?,
                       rain_reproductive_analysis       = ?,
                       initial_depth_analysis           = ?,
                       final_depth_analysis             = ?,
                       ph_H2O_analysis                  = ?,
                       ph_CaCl2_analysis                = ?,
                       clay_analysis                    = ?,
                       MO_analysis                      = ?,
                       CO_analysis                      = ?,
                       K_cmolc_analysis                 = ?,
                       Ca_analysis                      = ?,
                       Mg_analysis                      = ?,
                       Al_analysis                      = ?,
                       H_Al_analysis                    = ?,
                       SB_analysis                      = ?,
                       t_effective_CTC_analysis         = ?,
                       T_analysis                       = ?,
                       V_analysis                       = ?,
                       m_analysis                       = ?,
                       P_meh_analysis                   = ?,
                       P_rem_analysis                   = ?,
                       Na_analysis                      = ?,
                       K_mg_analysis                    = ?,
                       S_SO4_analysis                   = ?,
                       B_analysis                       = ?,
                       Cu_analysis                      = ?,
                       Fe_analysis                      = ?,
                       Mn_analysis                      = ?,
                       Zn_analysis                      = ?,
                       limestone_analysis               = ?,
                       plaster_analysis                 = ?,
                       pre_sowing_fertilizer_analysis   = ?,
                       pre_sowing_N_analysis            = ?,
                       pre_sowing_P2O5_analysis         = ?,
                       pre_sowing_K2O_analysis          = ?,
                       seeding_fertilizer_analysis      = ?,
                       seeding_N_analysis               = ?,
                       seeding_P2O5_analysis            = ?,
                       seeding_K2O_analysis             = ?,
                       top_dressing_fertilizer_analysis = ?,
                       top_dressing_N_analysis          = ?,
                       top_dressing_P2O5_analysis       = ?,
                       top_dressing_K2O_analysis        = ?,
                       sector_analysis                  = ?,
                       micro_analysis                   = ?,
                       micro_zn_analysis                = ?,
                       micro_b_analysis                 = ?,
                       micro_cu_analysis                = ?,
                       micro_mn_analysis                = ?,
                       micro_mo_analysis                = ?,
                       micro_co_analysis                = ?,
                       micro_ca_analysis                = ?,
                       micro_s_analysis                 = ?,
                       prnt_analysis                    = ?,
                       tca_analysis                     = ?
                       where code_analysis              = ?
               """)
            cursor.execute(sql, (dataset[1],
                                 dataset[2],
                                 dataset[3],
                                 dataset[4],
                                 dataset[5],
                                 dataset[6],
                                 dataset[7],
                                 dataset[8],
                                 dataset[9],
                                 dataset[10],
                                 dataset[11],
                                 dataset[12],
                                 dataset[13],
                                 dataset[14],
                                 dataset[15],
                                 dataset[16],
                                 dataset[17],
                                 dataset[18],
                                 dataset[19],
                                 dataset[20],
                                 dataset[21],
                                 dataset[22],
                                 dataset[23],
                                 dataset[24],
                                 dataset[25],
                                 dataset[26],
                                 dataset[27],
                                 dataset[28],
                                 dataset[29],
                                 dataset[30],
                                 dataset[31],
                                 dataset[32],
                                 dataset[33],
                                 dataset[34],
                                 dataset[35],
                                 dataset[36],
                                 dataset[37],
                                 dataset[38],
                                 dataset[39],
                                 dataset[40],
                                 dataset[41],
                                 dataset[42],
                                 dataset[43],
                                 dataset[44],
                                 dataset[45],
                                 dataset[46],
                                 dataset[47],
                                 dataset[48],
                                 dataset[49],
                                 dataset[50],
                                 dataset[51],
                                 dataset[52],
                                 dataset[53],
                                 dataset[54],
                                 dataset[55],
                                 dataset[56],
                                 dataset[57],
                                 dataset[58],
                                 dataset[59],
                                 dataset[60],
                                 dataset[61],
                                 dataset[62],
                                 dataset[63],
                                 dataset[64],
                                 dataset[65],
                                 dataset[66],
                                 dataset[67],
                                 dataset[0]))
            self.connection_data_base.commit()
            message('ok', 'Registro atualizado com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def delete_analysis(self, code):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()

            sql = f"""DELETE FROM ANALYSIS WHERE CODE_ANALYSIS = ?"""
            cursor.execute(sql, (code,))
            self.connection_data_base.commit()
            message('ok', 'Registro apagado com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_analysis(self, sql):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            cursor.execute(sql)
            analysis = cursor.fetchall()
            return analysis
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_analysis_code(self, code_analysis):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """Select
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
                       Where a.code_analysis = ?"""
            cursor.execute(sql, (code_analysis,))
            analysis = cursor.fetchall()
            return analysis
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def export_excel(self, query):
        try:
            self.open_data_base()
            excel_file_path = "./excel/analysis.xlsx"
            analysis = pd.read_sql_query(query, con=self.connection_data_base)
            analysis = analysis.rename(columns={'code_analysis' : 'Código da Análise',
                                                'code_producer' : 'Código do Produtor',
                                                'name_producer' : 'Nome',
                                                'agricultural_period_analysis' : 'Safra Agrícola',
                                                'culture_analysis' : 'Cultura',
                                                'area_analysis' : 'Área (ha)',
                                                'altitude_analysis' : 'Altitude',
                                                'latitude_analysis' : 'Latitude',
                                                'longitude_analysis' : 'Longitude',
                                                'planting_system_analysis' : 'Sistema de Plantio',
                                                'average_productivity_analysis' : 'Produção Média (60kg)',
                                                'minimum_temperature_analysis' : 'Temp. Mínima (C°)',
                                                'maximum_temperature_analysis' : 'Temp. Máxima (C°)',
                                                'rain_vegetative_analysis' : 'Chuva no Veg. (mm)',
                                                'rain_reproductive_analysis' : 'Chuva no Rep. (mm)',
                                                'initial_depth_analysis' : 'Profundidade Inicial',
                                                'final_depth_analysis' : 'Profundidade Final',
                                                'ph_H2O_analysis' : 'pH H2O (1 : 2,5)',
                                                'ph_CaCl2_analysis' : 'pH CaCl2 (1 : 2,5)',
                                                'clay_analysis' : 'Argila (g/kg)',
                                                'MO_analysis' : 'MO (dag/kg)',
                                                'CO_analysis' : 'CO (dag/kg)',
                                                'K_cmolc_analysis' : 'K (cmolc/dm3)',
                                                'Ca_analysis' : 'Ca (cmolc/dm3)',
                                                'Mg_analysis' : 'Mg (cmolc/dm3)',
                                                'Al_analysis' : 'Al (cmolc/dm3)',
                                                'H_Al_analysis' : 'H + Al (cmolc/dm3)',
                                                'SB_analysis' : 'SB (cmolc/dm3)',
                                                't_effective_CTC_analysis' : 't (cmolc/dm3)',
                                                'T_analysis' : 'T (cmolc/dm3)',
                                                'V_analysis' : 'V (%)',
                                                'm_analysis' : 'm (%)',
                                                'P_meh_analysis' : 'P (mg/dm3)',
                                                'P_rem_analysis' : 'P rem (mg/dm3)',
                                                'Na_analysis' : 'Na (mg/dm3)',
                                                'K_mg_analysis' : 'K (mg/dm3)',
                                                'S_SO4_analysis' : 'S-SO4 (mg/dm3)',
                                                'B_analysis' : 'B (mg/dm3)',
                                                'Cu_analysis' : 'Cu (mg/dm3)',
                                                'Fe_analysis' : 'Fe (mg/dm3)',
                                                'Mn_analysis' : 'Mn (mg/dm3)',
                                                'Zn_analysis' : 'Zn (mg/dm3)',
                                                'limestone_analysis' : 'Calcário (kg/ha)',
                                                'plaster_analysis' : 'Gesso (kg/ha)',
                                                'pre_sowing_fertilizer_analysis' : 'Adubação no Pré Plantio (kg/ha)',
                                                'pre_sowing_N_analysis' : 'N (%)',
                                                'pre_sowing_P2O5_analysis' : 'P2O5 (%)',
                                                'pre_sowing_K2O_analysis' : 'K2O (%)',
                                                'pre_sowing_N_analysis_kg' : 'N (KG)',
                                                'pre_sowing_P2O5_analysis_kg' : 'P2O5 (KG)',
                                                'pre_sowing_K2O_analysis_kg' : 'K2O (KG)',
                                                'seeding_fertilizer_analysis' : 'Adubação na Semeadura (kg/ha)',
                                                'seeding_N_analysis' : 'N (%)',
                                                'seeding_P2O5_analysis' : 'P2O5 (%)',
                                                'seeding_K2O_analysis' : 'K2O (%)',
                                                'seeding_N_analysis_kg' : 'N (KG)',
                                                'seeding_P2O5_analysis_kg' : 'P2O5 (KG)',
                                                'seeding_K2O_analysis_kg' : 'K2O (KG)',
                                                'top_dressing_fertilizer_analysis' : 'Adubação no Pós Plantio (kg/ha)',
                                                'top_dressing_N_analysis' : 'N (%)',
                                                'top_dressing_P2O5_analysis' : 'P2O5 (%)',
                                                'top_dressing_K2O_analysis' : 'K2O (%)',
                                                'top_dressing_N_analysis_kg' : 'N (KG)',
                                                'top_dressing_P2O5_analysis_kg' : 'P2O5 (KG)',
                                                'top_dressing_K2O_analysis_kg' : 'K2O (KG)',
                                                'top_dressing_K2O_analysis_kg' : 'K2O (KG)',
                                                'sector_analysis' : 'Talhão',
                                                'micro_analysis'  : 'Micros-kg/ha',
                                                'micro_zn_analysis'    : 'Zn-%',
                                                'micro_b_analysis'     : 'B-%',
                                                'micro_cu_analysis'    : 'Cu-%',
                                                'micro_mn_analysis'    : 'Mn-%',
                                                'micro_mo_analysis'    : 'Mo-%',
                                                'micro_co_analysis'    : 'Co-%',
                                                'micro_ca_analysis'    : 'Ca-%',
                                                'micro_s_analysis'     : 'S-%',
                                                'micro_zn_analysis_kg' : 'Zn-kg/ha',
                                                'micro_b_analysis_kg'  : 'B-kg/ha',
                                                'micro_cu_analysis_kg' : 'Cu-kg/ha',
                                                'micro_mn_analysis_kg' : 'Mn-kg/ha',
                                                'micro_mo_analysis_kg' : 'Mo-kg/ha',
                                                'micro_co_analysis_kg' : 'Co-kg/ha',
                                                'micro_ca_analysis_kg' : 'Ca-kg/ha',
                                                'micro_s_analysis_kg'  : 'S-kg/ha',
                                                'prnt_analysis'        : 'PRNT-%',
                                                'tca_analysis'         : 'TCA-%',
                                                'name_user'            : 'Usuário'})
            analysis.to_excel(
                excel_file_path, sheet_name='Análises', index=False)
            remention_excel_columns(excel_file_path)

            message('ok', 'Relatório gerado com sucesso!')
            os.system(f'start excel "{excel_file_path}"')
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def pdf_report(self, query):
        self.open_data_base()
        pdf_filename = '.\\pdf\\Análises.pdf'
        analysis = pd.read_sql_query(query, con=self.connection_data_base)
        analysis['name_producer']   = analysis['name_producer'].str.slice(0, 29)
        analysis['sector_analysis'] = analysis['sector_analysis'].str.slice(0, 14)

        report = AnalysisReportPdf (pdf_filename, analysis, 'Relatório de Análises')
        report.generate_report()
        self.close_data_base()

    def export_data_csv(self):
        try:
            self.open_data_base()
            csv_file_path = "./csv/data.csv"
            sql = """Select
                       a.altitude_analysis,
                       a.planting_system_analysis,
                       a.average_productivity_analysis,
                       a.minimum_temperature_analysis,
                       a.maximum_temperature_analysis,
                       a.rain_vegetative_analysis,
                       a.rain_reproductive_analysis,
                       a.ph_H2O_analysis,
                       a.ph_CaCl2_analysis,
                       a.clay_analysis,
                       a.MO_analysis,
                       a.CO_analysis,
                       a.K_cmolc_analysis,
                       a.Ca_analysis,
                       a.Mg_analysis,
                       a.Al_analysis,
                       a.H_Al_analysis,
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
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_N_analysis/100.00)) as pre_sowing_N_analysis_kg,
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_P2O5_analysis/100.00)) as pre_sowing_P2O5_analysis_kg,
                       (a.pre_sowing_fertilizer_analysis * (a.pre_sowing_K2O_analysis/100.00)) as pre_sowing_K2O_analysis_kg,
                       (a.seeding_fertilizer_analysis * (a.seeding_N_analysis/100.00)) as seeding_N_analysis_kg,
                       (a.seeding_fertilizer_analysis * (a.seeding_P2O5_analysis/100.00)) as seeding_P2O5_analysis_kg,
                       (a.seeding_fertilizer_analysis * (a.seeding_K2O_analysis/100.00)) as seeding_K2O_analysis_kg,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_N_analysis/100.00)) as top_dressing_N_analysis_kg,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_P2O5_analysis/100.00)) as top_dressing_P2O5_analysis_kg,
                       (a.top_dressing_fertilizer_analysis * (a.top_dressing_K2O_analysis/100.00)) as top_dressing_K2O_analysis_kg
                       From analysis a
                       where 
                       a.average_productivity_analysis > 0"""
            analysis = pd.read_sql_query(sql, con=self.connection_data_base)
            analysis.to_csv(csv_file_path, index=False)
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()
