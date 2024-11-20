import os
import sqlite3

import pandas as pd

from registration_report_pdf import RegistrationReportPdf
from tools import message, remention_excel_columns


class DataBaseUser:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def insert_user(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            fields = ('name_user',
                      'cpf_user',
                      'address_user',
                      'number_user',
                      'complement_user',
                      'neighborhood_user',
                      'city_user',
                      'state_user',
                      'cep_user',
                      'phone_user',
                      'email_user',
	                  'authentication_name_user',
	                  'password_user')                
            markers = ','.join(['?'] * len(fields))
            sql = f"""INSERT INTO USER ({', '.join(fields)}) VALUES ({markers})"""
            cursor.execute(sql, dataset)
            self.connection_data_base.commit()
            message('ok', 'Registro inserido com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def update_user(self, dataset):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = (f"""UPDATE USER SET
                   name_user                = ?,
                   cpf_user                 = ?,
                   address_user             = ?,
                   number_user              = ?,
                   complement_user          = ?,
                   neighborhood_user        = ?,
                   city_user                = ?,
                   state_user               = ?,
                   cep_user                 = ?,
                   phone_user               = ?,
                   email_user               = ?,
	               authentication_name_user = ?,
	               password_user            = ?                
                   where code_user   = ?""")
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
                                 dataset[0]))
            self.connection_data_base.commit()
            message('ok', 'Registro atualizado com sucesso!')
        except Exception as e:
            self.connection_data_base.rollback()
            message('erro', str(e))
        finally:
            self.close_data_base()

    def delete_user(self, code):
        if int(code) != 1: # The user with code "1" is the system administrator and cannot be deleted.
            if self.user_linked_records(code)==0:                
                try:
                    self.open_data_base()
                    cursor = self.connection_data_base.cursor()
                    sql = f"""DELETE FROM USER WHERE CODE_USER = ?"""
                    cursor.execute(sql, (code,))
                    self.connection_data_base.commit()
                    message('ok', 'Registro apagado com sucesso!')
                except Exception as e:
                    self.connection_data_base.rollback()
                    message('erro', str(e))
                finally:
                    self.close_data_base()
            else:
                message('erro','O usuário é referenciado em outros registros no sistema e não pode ser apagado.')        
        else:
            message('erro', 'O usuário do código 1 é o "Adminstrador do Sistema" e não pode ser apagado.')    

    def user_linked_records(self,code_user):
        self.open_data_base()
        try:
            number_references=0

            cursor = self.connection_data_base.cursor()
            sql = """SELECT count(*) FROM producer WHERE code_user = ? """
            cursor.execute(sql, (code_user,))
            user = cursor.fetchall()
            number_references= int(user[0][0])

            cursor = self.connection_data_base.cursor()
            sql = """SELECT count(*) FROM analysis WHERE code_user = ? """
            cursor.execute(sql, (code_user,))
            user = cursor.fetchall()
            number_references= number_references + int(user[0][0])

            return number_references
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_user(self, query):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            cursor.execute(query)
            user = cursor.fetchall()
            return user
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_user_code(self, code_user):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT 
                     code_user,
                     name_user, 
                     cpf_user, 
                     address_user, 
                     number_user, 
                     complement_user, 
                     neighborhood_user, 
                     city_user, 
                     state_user, 
                     cep_user, 
                     phone_user, 
                     email_user,
  	                 authentication_name_user,
	                 password_user                
                     FROM user 
                     WHERE code_user = ?"""
            cursor.execute(sql, (code_user,))
            user = cursor.fetchall()
            return user
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def export_excel(self, query):
        try:
            self.open_data_base()
            excel_file_path = "./excel/Usuarios.xlsx"

            user = pd.read_sql_query(query, con=self.connection_data_base)

            user = user.rename(columns={'code_user'                : 'Código',
                                        'name_user'                : 'Nome',
                                        'cpf_user'                 : 'CPF',
                                        'address_user'             : 'Endereço',
                                        'number_user'              : 'Número',
                                        'complement_user'          : 'Complemento',
                                        'neighborhood_user'        : 'Bairro',
                                        'city_user'                : 'Município',
                                        'state_user'               : 'Estado',
                                        'cep_user'                 : 'CEP',
                                        'phone_user'               : 'Telefone',
                                        'email_user'               : 'e-mail',
  	                                    'authentication_name_user' : 'Nome do Usuário',
  	                                    'password_user'            : 'Senha'})

            user.to_excel(
                excel_file_path, sheet_name='Usuarios', index=False)
            remention_excel_columns(excel_file_path)
            message('ok', 'Relatório gerado com sucesso!')
            os.system(f'start excel "{excel_file_path}"')
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def pdf_report(self, query):
        self.open_data_base()
        pdf_filename = './pdf/Usuario.pdf'
        cursor = self.connection_data_base.cursor()
        user = pd.read_sql_query(query, con=self.connection_data_base)
        user = user.rename(columns={    'code_user'                : 'Cód.',
                                        'name_user'                : 'Nome',
                                        'cpf_user'                 : 'CPF',
                                        'address_user'             : 'Endereço',
                                        'number_user'              : 'N°',
                                        'complement_user'          : 'Complemento',
                                        'neighborhood_user'        : 'Bairro',
                                        'city_user'                : 'Município',
                                        'state_user'               : 'UF',
                                        'cep_user'                 : 'CEP',
                                        'phone_user'               : 'Telefone',
                                        'email_user'               : 'e-mail',
  	                                    'authentication_name_user' : 'Nome do Usuário',
  	                                    'password_user'            : 'Senha'})

        user['Nome']      = user['Nome'].str.slice(0, 24)
        user['Endereço']  = user['Endereço'].str.slice(0, 30)
        user['N°']        = user['N°'].str.slice(0, 4)
        user['Bairro']    = user['Bairro'].str.slice(0, 13)
        user['Município'] = user['Município'].str.slice(0, 19)
        user['UF']        = user['UF'].str.slice(0, 16)
        user['e-mail']    = user['e-mail'].str.slice(0, 30)

        user.drop(columns=['Complemento'], inplace=True)
        user.drop(columns=['CEP'], inplace=True)
        user.drop(columns=['Nome do Usuário'], inplace=True)
        user.drop(columns=['Senha'], inplace=True)
                        
        col_widths = [25, 100, 80, 130, 25, 65, 110, 20, 70, 130]

        report = RegistrationReportPdf(
            pdf_filename, user, col_widths, 'Relatório de Usuário')
        report.initialize_table_style()
        report.generate_report()
        self.close_data_base()

