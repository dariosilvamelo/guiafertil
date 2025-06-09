import os
import sqlite3

import pandas as pd

from registration_report_pdf import RegistrationReportPdf
from tools import message, remention_excel_columns


class DataBaseProducer:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def insert_producer(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            fields = ('name_producer',
                      'cpf_cnpj_producer',
                      'address_producer',
                      'number_producer',
                      'complement_producer',
                      'neighborhood_producer',
                      'city_producer',
                      'state_producer',
                      'cep_producer',
                      'phone_producer',
                      'email_producer',
                      'code_user')
            markers = ','.join(['?'] * len(fields))
            sql = f"""INSERT INTO PRODUCER ({', '.join(fields)}) VALUES ({markers})"""
            cursor.execute(sql, dataset)
            self.connection_data_base.commit()
            message('ok', 'Registro inserido com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def update_producer(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = (f"""UPDATE PRODUCER SET
                   name_producer         = ?,
                   cpf_cnpj_producer     = ?,
                   address_producer      = ?,
                   number_producer       = ?,
                   complement_producer   = ?,
                   neighborhood_producer = ?,
                   city_producer         = ?,
                   state_producer        = ?,
                   cep_producer          = ?,
                   phone_producer        = ?,
                   email_producer        = ?,
                   code_user             = ?
                   where code_producer   = ?
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
                                 dataset[0]))
            self.connection_data_base.commit()
            message('ok', 'Registro atualizado com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def delete_producers(self, code):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = f"""DELETE FROM PRODUCER WHERE CODE_PRODUCER = ?"""
            cursor.execute(sql, (code,))
            self.connection_data_base.commit()
            message('ok', 'Registro apagado com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_producers(self, query):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            cursor.execute(query)
            producers = cursor.fetchall()
            return producers
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_producer_code(self, code_producer):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT 
                     P.code_producer,
                     P.name_producer, 
                     P.cpf_cnpj_producer, 
                     P.address_producer, 
                     P.number_producer, 
                     P.complement_producer, 
                     P.neighborhood_producer, 
                     P.city_producer, 
                     P.state_producer, 
                     P.cep_producer, 
                     P.phone_producer, 
                     P.email_producer,
                     U.code_user,
                     U.name_user
            FROM PRODUCER P left join USER U on P.code_user = U.code_user 
            WHERE P.code_producer = ?"""
            cursor.execute(sql, (code_producer,))
            producers = cursor.fetchall()
            return producers
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def export_excel(self, query):
        try:
            self.open_data_base()
            excel_file_path = "./excel/Produtores.xlsx"
            producer = pd.read_sql_query(query, con=self.connection_data_base)
            producer = producer.rename(columns={'code_producer': 'Código',
                                                'name_producer': 'Nome',
                                                'cpf_cnpj_producer': 'CPF/CNPJ',
                                                'address_producer': 'Endereço',
                                                'number_producer': 'Número',
                                                'complement_producer': 'Complemento',
                                                'neighborhood_producer': 'Bairro',
                                                'city_producer': 'Município',
                                                'state_producer': 'Estado',
                                                'cep_producer': 'CEP',
                                                'phone_producer': 'Telefone',
                                                'email_producer': 'e-mail',
                                                'code_user'    : 'Código do Usuário',
                                                'name_user'   : 'Nome do Usuário'
                                               })
            producer.to_excel(
                excel_file_path, sheet_name='Produtores', index=False)
            remention_excel_columns(excel_file_path)

            message('ok', 'Relatório gerado com sucesso!')
            os.system(f'start excel "{excel_file_path}"')
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def pdf_report(self, query):
        self.open_data_base()
        pdf_filename = './pdf/Produtores.pdf'

        producer = pd.read_sql_query(query, con=self.connection_data_base)
        
        producer = producer.rename(columns =   {'code_producer': 'Cód.',
                                                'name_producer': 'Nome',
                                                'cpf_cnpj_producer': 'CPF/CNPJ',
                                                'address_producer': 'Endereço',
                                                'number_producer': 'N°',
                                                'complement_producer': 'Complemento',
                                                'neighborhood_producer': 'Bairro',
                                                'city_producer': 'Município',
                                                'state_producer': 'UF',
                                                'cep_producer': 'CEP',
                                                'phone_producer': 'Telefone',
                                                'email_producer': 'e-mail',
                                                'code_user'    : 'Código do Usuário',
                                                'name_user'   : 'Nome do Usuário'
                                               })
        
        producer['Nome']      = producer['Nome'].str.slice(0, 17)
        producer['Endereço']  = producer['Endereço'].str.slice(0, 24)
        producer['N°']        = producer['N°'].str.slice(0, 4)
        producer['Bairro']    = producer['Bairro'].str.slice(0, 11)
        producer['Município'] = producer['Município'].str.slice(0, 19)
        producer['UF']        = producer['UF'].str.slice(0, 16)
        producer['e-mail']    = producer['e-mail'].str.slice(0, 30)

        producer.drop(columns=['Código do Usuário'], inplace=True)
        producer.drop(columns=['Nome do Usuário'], inplace=True)
        producer.drop(columns=['Complemento'], inplace=True)
        producer.drop(columns=['CEP'], inplace=True)
                        
        col_widths = [25, 100, 80, 130, 25, 65, 110, 20, 70, 130]

        report = RegistrationReportPdf(
            pdf_filename, producer, col_widths, 'Relatório de Produtores')
        report.initialize_table_style()
        report.generate_report()
        self.close_data_base()
