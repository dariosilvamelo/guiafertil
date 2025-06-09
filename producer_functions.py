from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from tools import format_cpf_cnpj, message, message_confirmation


class Producer:

    def __init__(self, producer_registration):
        self.register = producer_registration

    def insert_new_producer(self):
        self.button_enablements('insert')
        self.read_only_producer_fields(False)
        self.clear_fields_producer_register()
        self.register.edt_name_producer.setFocus()

    def update_changes_producer(self):
        code = self.register.lbl_code_producer.text()
        if code != '':
            self.button_enablements('update')
            self.read_only_producer_fields(False)
        self.register.edt_name_producer.setFocus()

    def cancel_edit_producer(self):
        if self.register.btn_save_producer.isEnabled() == True:
            self.clear_fields_producer_register()
        else:
            self.consult_producer_code(self.register.lbl_code_producer.text())

        self.register.table_grid_producer.setFocus()
        self.register.edt_query_producer.setFocus()

        self.button_enablements('save_or_cancel')
        self.read_only_producer_fields(True)

    def save_new_producer(self, code_user):
        dataset = (self.register.edt_name_producer.text(),
                   self.register.edt_cpf_cnpj_producer.text(),
                   self.register.edt_address_producer.text(),
                   self.register.edt_number_producer.text(),
                   self.register.edt_complement_producer.text(),
                   self.register.edt_neighborhood_producer.text(),
                   self.register.edt_city_producer.text(),
                   self.register.cbx_state_producer.currentText(),
                   self.register.edt_cep_producer.text(),
                   self.register.edt_phone_producer.text(),
                   self.register.edt_email_producer.text(),
                   code_user)
        self.register.producer_data.insert_producer(dataset)
        self.button_enablements('save_or_cancel')
        self.read_only_producer_fields(True)
        self.clear_fields_producer_register()

    def save_changes_producer(self,code_user):
        name_producer = self.register.edt_name_producer.text()

        dataset = (self.register.lbl_code_producer.text(),
                   self.register.edt_name_producer.text(),
                   self.register.edt_cpf_cnpj_producer.text(),
                   self.register.edt_address_producer.text(),
                   self.register.edt_number_producer.text(),
                   self.register.edt_complement_producer.text(),
                   self.register.edt_neighborhood_producer.text(),
                   self.register.edt_city_producer.text(),
                   self.register.cbx_state_producer.currentText(),
                   self.register.edt_cep_producer.text(),
                   self.register.edt_phone_producer.text(),
                   self.register.edt_email_producer.text(),
                   str(code_user))
        self.register.producer_data.update_producer(dataset)

        self.consult_producer_code(self.register.lbl_code_producer.text())

        self.register.table_grid_producer.setFocus()
        self.register.edt_query_producer.setFocus()

        self.button_enablements('save_or_cancel')

        self.read_only_producer_fields(True)

    def delete_record_producer(self):
        if self.register.table_grid_producer.rowCount() >= 1:
            if message_confirmation('Excluir', 'Este registro será excluido.', 'Você tem certeza que deseja continuar?') == 'confirmado':
                code = self.register.lbl_code_producer.text()
                self.register.producer_data.delete_producers(code)
                self.consult_producer()
                if self.register.table_grid_producer.rowCount() < 1:
                    self.clear_fields_producer_register()

    def consult_producer(self):
        result = self.register.producer_data.query_producers(self.generate_sql_query())
        self.table_assembly(result)
        self.register.table_grid_producer.setFocus()
        self.register.edt_query_producer.setFocus()

    def consult_producer_code(self, code_producer):
        result = self.register.producer_data.query_producer_code(code_producer)
        self.table_assembly(result)

    def table_assembly(self, result):
        if result is not None:
            self.register.table_grid_producer.setAlternatingRowColors(True)
            self.register.table_grid_producer.clearContents()

            self.register.table_grid_producer.setRowCount(len(result))

            for row_index, row_text in enumerate(result):
                for column_index, data in enumerate(row_text):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.register.table_grid_producer.setItem(
                        row_index, column_index, item)

        self.register.table_grid_producer.setColumnWidth(0, 50)
        self.register.table_grid_producer.setColumnWidth(1, 200)
        self.register.table_grid_producer.setColumnWidth(2, 130)
        self.register.table_grid_producer.setColumnWidth(3, 200)
        self.register.table_grid_producer.setColumnWidth(4, 60)
        self.register.table_grid_producer.setColumnWidth(5, 150)
        self.register.table_grid_producer.setColumnWidth(6, 150)
        self.register.table_grid_producer.setColumnWidth(7, 150)
        self.register.table_grid_producer.setColumnWidth(8, 100)
        self.register.table_grid_producer.setColumnWidth(9, 100)
        self.register.table_grid_producer.setColumnWidth(10, 125)
        self.register.table_grid_producer.setColumnWidth(11, 170)
        self.register.table_grid_producer.setColumnWidth(12, 50)
        self.register.table_grid_producer.setColumnWidth(13, 200)

    def export_excel_producer(self):
        if self.register.table_grid_producer.rowCount() >= 1:
            self.register.producer_data.export_excel(self.generate_sql_query())

    def report_pdf_producer(self):
        if self.register.table_grid_producer.rowCount() >= 1:
            self.register.producer_data.pdf_report(self.generate_sql_query())

    def dataset_producer(self):
        current_row = self.register.table_grid_producer.currentRow()
        if current_row == -1:
           current_row = 1

        item = self.register.table_grid_producer.item(current_row, 0)

        if item is not None:
            self.register.lbl_code_producer.setText(self.register.table_grid_producer.item(current_row, 0).text())
            self.register.edt_name_producer.setText(self.register.table_grid_producer.item(current_row, 1).text())
            self.register.edt_cpf_cnpj_producer.setText(self.register.table_grid_producer.item(current_row, 2).text())
            self.register.edt_address_producer.setText(self.register.table_grid_producer.item(current_row, 3).text())
            self.register.edt_number_producer.setText(self.register.table_grid_producer.item(current_row, 4).text())
            self.register.edt_complement_producer.setText(self.register.table_grid_producer.item(current_row, 5).text())
            self.register.edt_neighborhood_producer.setText(self.register.table_grid_producer.item(current_row, 6).text())
            self.register.edt_city_producer.setText(self.register.table_grid_producer.item(current_row, 7).text())
            self.register.cbx_state_producer.setCurrentText(self.register.table_grid_producer.item(current_row, 8).text())
            self.register.edt_cep_producer.setText(self.register.table_grid_producer.item(current_row, 9).text())
            self.register.edt_phone_producer.setText(self.register.table_grid_producer.item(current_row, 10).text())
            self.register.edt_email_producer.setText(self.register.table_grid_producer.item(current_row, 11).text())
            if self.register.table_grid_producer.item(current_row, 13) is not None:
               self.register.lbl_name_user_producer.setText(self.register.table_grid_producer.item(current_row, 13).text())
            else:
               self.register.lbl_name_user_producer.setText('')

    def button_enablements(self, status):
        if status == 'insert':
            self.register.btn_insert_producer.setEnabled(False)
            self.register.btn_update_producer.setEnabled(False)
            self.register.btn_cancelar_producer.setEnabled(True)
            self.register.btn_save_change_producer.setEnabled(False)
            self.register.btn_save_producer.setEnabled(True)
        elif status == 'update':
            self.register.btn_insert_producer.setEnabled(False)
            self.register.btn_update_producer.setEnabled(False)
            self.register.btn_cancelar_producer.setEnabled(True)
            self.register.btn_save_change_producer.setEnabled(True)
            self.register.btn_save_producer.setEnabled(False)
        elif status == 'save_or_cancel':
            self.register.btn_insert_producer.setEnabled(True)
            self.register.btn_update_producer.setEnabled(True)
            self.register.btn_cancelar_producer.setEnabled(False)
            self.register.btn_save_change_producer.setEnabled(False)
            self.register.btn_save_producer.setEnabled(False)

    def read_only_producer_fields(self, status):
        self.register.edt_name_producer.setReadOnly(status)
        self.register.edt_cpf_cnpj_producer.setReadOnly(status)
        self.register.edt_address_producer.setReadOnly(status)
        self.register.edt_number_producer.setReadOnly(status)
        self.register.edt_complement_producer.setReadOnly(status)
        self.register.edt_neighborhood_producer.setReadOnly(status)
        self.register.edt_city_producer.setReadOnly(status)
        self.register.edt_cep_producer.setReadOnly(status)
        self.register.edt_phone_producer.setReadOnly(status)
        self.register.edt_email_producer.setReadOnly(status)
        if status == True:
            # read
            self.register.cbx_state_producer.setEnabled(False)
            self.register.edt_name_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_cpf_cnpj_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_address_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_number_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_complement_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_neighborhood_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_city_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_cep_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_phone_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.edt_email_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
            self.register.cbx_state_producer.setStyleSheet(
                "background-color: rgb(255, 255, 255);")
        else:
            # edition
            self.register.cbx_state_producer.setEnabled(True)
            self.register.edt_name_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_cpf_cnpj_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_address_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_number_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_complement_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_neighborhood_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_city_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_cep_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_phone_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.edt_email_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")
            self.register.cbx_state_producer.setStyleSheet(
                "background-color: rgb(255, 255, 127);")

    def clear_fields_producer_register(self):
        self.register.lbl_code_producer.setText('')
        self.register.edt_name_producer.setText('')
        self.register.edt_cpf_cnpj_producer.setText('')
        self.register.edt_address_producer.setText('')
        self.register.edt_number_producer.setText('')
        self.register.edt_complement_producer.setText('')
        self.register.edt_neighborhood_producer.setText('')
        self.register.edt_city_producer.setText('')
        self.register.cbx_state_producer.setCurrentText('')
        self.register.edt_cep_producer.setText('')
        self.register.edt_phone_producer.setText('')
        self.register.edt_email_producer.setText('')
        self.register.lbl_name_user_producer.setText('')

    def cpf_cnpj(self):
        self.register.edt_cpf_cnpj_producer.setText(
            format_cpf_cnpj(self.register.edt_cpf_cnpj_producer.text()))

    def generate_sql_query(self):
        return """  SELECT 
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
            WHERE P.name_producer LIKE '"""+ self.register.edt_query_producer.text()+"%' ORDER BY P.name_producer"
            
