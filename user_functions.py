from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from tools import format_cpf_cnpj, message_confirmation


class User:

    def __init__(self, user_registration):
        self.register = user_registration

    def insert_new_user(self):
        self.button_enablements('insert')
        self.read_only_user_fields(False)
        self.clear_fields_user_register()
        self.register.edt_name_user.setFocus()

    def update_changes_user(self):
        code = self.register.lbl_code_user.text()
        if code != '':
            self.button_enablements('update')
            self.read_only_user_fields(False)
        self.register.edt_name_user.setFocus()

    def cancel_edit_user(self):
        if self.register.btn_save_user.isEnabled() == True:
            self.clear_fields_user_register()
        else:
            self.consult_user_code(self.register.lbl_code_user.text())

        self.register.table_grid_user.setFocus()
        self.register.edt_query_user.setFocus()

        self.button_enablements('save_or_cancel')
        self.read_only_user_fields(True)

    def save_new_user(self):
        dataset = (self.register.edt_name_user.text(),
                   self.register.edt_cpf_user.text(),
                   self.register.edt_address_user.text(),
                   self.register.edt_number_user.text(),
                   self.register.edt_complement_user.text(),
                   self.register.edt_neighborhood_user.text(),
                   self.register.edt_city_user.text(),
                   self.register.cbx_state_user.currentText(),
                   self.register.edt_cep_user.text(),
                   self.register.edt_phone_user.text(),
                   self.register.edt_email_user.text(),
                   self.register.edt_authentication_name_user.text(),
                   self.register.edt_password_user.text())              
        
        self.register.user_data.insert_user(dataset)
        self.button_enablements('save_or_cancel')
        self.read_only_user_fields(True)
        self.clear_fields_user_register()

    def save_changes_user(self):
        name_user = self.register.edt_name_user.text()

        dataset = (self.register.lbl_code_user.text(),
                   self.register.edt_name_user.text(),
                   self.register.edt_cpf_user.text(),
                   self.register.edt_address_user.text(),
                   self.register.edt_number_user.text(),
                   self.register.edt_complement_user.text(),
                   self.register.edt_neighborhood_user.text(),
                   self.register.edt_city_user.text(),
                   self.register.cbx_state_user.currentText(),
                   self.register.edt_cep_user.text(),
                   self.register.edt_phone_user.text(),
                   self.register.edt_email_user.text(),
                   self.register.edt_authentication_name_user.text(),
                   self.register.edt_password_user.text())              

        self.register.user_data.update_user(dataset)

        self.consult_user_code(self.register.lbl_code_user.text())

        self.register.table_grid_user.setFocus()
        self.register.edt_query_user.setFocus()

        self.button_enablements('save_or_cancel')

        self.read_only_user_fields(True)

    def delete_record_user(self):
        if self.register.table_grid_user.rowCount() >= 1:
            if message_confirmation('Excluir', 'Este registro será excluido.', 'Você tem certeza que deseja continuar?') == 'confirmado':
                code = self.register.lbl_code_user.text()
                self.register.user_data.delete_user(code)
                self.consult_user()
                if self.register.table_grid_user.rowCount() < 1:
                    self.clear_fields_user_register()

    def consult_user(self):
        result = self.register.user_data.query_user(self.generate_sql_query())
        self.table_assembly(result)
        self.register.table_grid_user.setFocus()
        self.register.edt_query_user.setFocus()

    def consult_user_code(self, code_user):
        result = self.register.user_data.query_user_code(code_user)
        self.table_assembly(result)

    def table_assembly(self, result):
        if result is not None:
            self.register.table_grid_user.setAlternatingRowColors(True)
            self.register.table_grid_user.clearContents()
            self.register.table_grid_user.setRowCount(len(result))
            self.register.table_grid_user.setColumnHidden(13, True)            
            for row_index, row_text in enumerate(result):
                for column_index, data in enumerate(row_text):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.register.table_grid_user.setItem(row_index, column_index, item)

        self.register.table_grid_user.setColumnWidth(0, 50)
        self.register.table_grid_user.setColumnWidth(1, 200)
        self.register.table_grid_user.setColumnWidth(2, 130)
        self.register.table_grid_user.setColumnWidth(3, 200)
        self.register.table_grid_user.setColumnWidth(4, 60)
        self.register.table_grid_user.setColumnWidth(5, 150)
        self.register.table_grid_user.setColumnWidth(6, 150)
        self.register.table_grid_user.setColumnWidth(7, 150)
        self.register.table_grid_user.setColumnWidth(8, 100)
        self.register.table_grid_user.setColumnWidth(9, 100)
        self.register.table_grid_user.setColumnWidth(10, 125)
        self.register.table_grid_user.setColumnWidth(11, 170)

    def export_excel_user(self):
        if self.register.table_grid_user.rowCount() >= 1:
            self.register.user_data.export_excel(self.generate_sql_query())

    def report_pdf_user(self):
        if self.register.table_grid_user.rowCount() >= 1:
            self.register.user_data.pdf_report(self.generate_sql_query())

    def dataset_user(self):

        current_row = self.register.table_grid_user.currentRow()

        if current_row == -1:
            current_row = 1

        item = self.register.table_grid_user.item(current_row, 0)

        if item is not None:
            self.register.lbl_code_user.setText(
                self.register.table_grid_user.item(current_row, 0).text())
            self.register.edt_name_user.setText(
                self.register.table_grid_user.item(current_row, 1).text())
            self.register.edt_cpf_user.setText(
                self.register.table_grid_user.item(current_row, 2).text())
            self.register.edt_address_user.setText(
                self.register.table_grid_user.item(current_row, 3).text())
            self.register.edt_number_user.setText(
                self.register.table_grid_user.item(current_row, 4).text())
            self.register.edt_complement_user.setText(
                self.register.table_grid_user.item(current_row, 5).text())
            self.register.edt_neighborhood_user.setText(
                self.register.table_grid_user.item(current_row, 6).text())
            self.register.edt_city_user.setText(
                self.register.table_grid_user.item(current_row, 7).text())
            self.register.cbx_state_user.setCurrentText(
                self.register.table_grid_user.item(current_row, 8).text())
            self.register.edt_cep_user.setText(
                self.register.table_grid_user.item(current_row, 9).text())
            self.register.edt_phone_user.setText(
                self.register.table_grid_user.item(current_row, 10).text())
            self.register.edt_email_user.setText(
                self.register.table_grid_user.item(current_row, 11).text())
            self.register.edt_authentication_name_user.setText(
                self.register.table_grid_user.item(current_row, 12).text())
            self.register.edt_password_user.setText(
                self.register.table_grid_user.item(current_row, 13).text())
          
    def button_enablements(self, status):
        if status == 'insert':
            self.register.btn_insert_user.setEnabled(False)
            self.register.btn_update_user.setEnabled(False)
            self.register.btn_cancelar_user.setEnabled(True)
            self.register.btn_save_change_user.setEnabled(False)
            self.register.btn_save_user.setEnabled(True)
        elif status == 'update':
            self.register.btn_insert_user.setEnabled(False)
            self.register.btn_update_user.setEnabled(False)
            self.register.btn_cancelar_user.setEnabled(True)
            self.register.btn_save_change_user.setEnabled(True)
            self.register.btn_save_user.setEnabled(False)
        elif status == 'save_or_cancel':
            self.register.btn_insert_user.setEnabled(True)
            self.register.btn_update_user.setEnabled(True)
            self.register.btn_cancelar_user.setEnabled(False)
            self.register.btn_save_change_user.setEnabled(False)
            self.register.btn_save_user.setEnabled(False)

    def read_only_user_fields(self, status):
        self.register.edt_name_user.setReadOnly(status)
        self.register.edt_cpf_user.setReadOnly(status)
        self.register.edt_address_user.setReadOnly(status)
        self.register.edt_number_user.setReadOnly(status)
        self.register.edt_complement_user.setReadOnly(status)
        self.register.edt_neighborhood_user.setReadOnly(status)
        self.register.edt_city_user.setReadOnly(status)
        self.register.edt_cep_user.setReadOnly(status)
        self.register.edt_phone_user.setReadOnly(status)
        self.register.edt_email_user.setReadOnly(status)
        self.register.edt_authentication_name_user.setReadOnly(status)
        self.register.edt_password_user.setReadOnly(status)
        if status == True:
            # read
            self.register.cbx_state_user.setEnabled(False)
            self.register.edt_name_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_cpf_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_address_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_number_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_complement_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_neighborhood_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_city_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_cep_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_phone_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_email_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_authentication_name_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_password_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.cbx_state_user.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
        else:
            # edition
            self.register.cbx_state_user.setEnabled(True)
            self.register.edt_name_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_cpf_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_address_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_number_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_complement_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_neighborhood_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_city_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_cep_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_phone_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_email_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_authentication_name_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_password_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.cbx_state_user.setStyleSheet(
                "background-color: rgb(255, 255, 127);")

    def clear_fields_user_register(self):
        self.register.lbl_code_user.setText('')
        self.register.edt_name_user.setText('')
        self.register.edt_cpf_user.setText('')
        self.register.edt_address_user.setText('')
        self.register.edt_number_user.setText('')
        self.register.edt_complement_user.setText('')
        self.register.edt_neighborhood_user.setText('')
        self.register.edt_city_user.setText('')
        self.register.cbx_state_user.setCurrentText('')
        self.register.edt_cep_user.setText('')
        self.register.edt_phone_user.setText('')
        self.register.edt_email_user.setText('')
        self.register.edt_authentication_name_user.setText('')
        self.register.edt_password_user.setText('')

    def cpf_cnpj(self):
        self.register.edt_cpf_user.setText(
            format_cpf_cnpj(self.register.edt_cpf_user.text()))

    def generate_sql_query(self):
        return """SELECT 
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
                     WHERE name_user LIKE '"""+ self.register.edt_query_user.text()+"%' ORDER BY name_user"""
                     
