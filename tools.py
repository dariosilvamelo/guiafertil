import openpyxl
from PySide6.QtWidgets import QLineEdit, QMessageBox


def message_confirmation(title, text, question):
    m = QMessageBox()
    m.setWindowTitle(title)
    m.setText(text)
    m.setInformativeText(question)
    m.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    m.button(QMessageBox.Yes).setText("Sim")
    m.button(QMessageBox.No).setText("Não")
    response = m.exec()
    if response == QMessageBox.Yes:
        return 'confirmado'
    else:
        return 'cancelar'


def message(type_message, text):
    m = QMessageBox()
    m.setWindowTitle('GUIAFERTIL')
    if type_message == 'ok':
        m.setIcon(QMessageBox.Information)
    elif type_message == 'erro':
        m.setIcon(QMessageBox.Critical)
    elif type_message == 'aviso':
        m.setIcon(QMessageBox.Warning)
    m.setText(text)
    m.exec()


def format_cpf_cnpj(numero):

    numero = ''.join(filter(str.isdigit, numero))
    if len(numero) == 11:
        return f'{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}'
    elif len(numero) == 14:
        return f'{numero[:2]}.{numero[2:5]}.{numero[5:8]}/{numero[8:12]}-{numero[12:]}'
    else:
        return numero


def numeric_field(lineedit):
    for char in lineedit.text():
        if not char.isdigit():
           if char!=',':
              lineedit.backspace()
              return
           else:
              if lineedit.text().count(',')>1:
                 lineedit.backspace()
                 return 


def validates_float(number):
    if isinstance(number, str):
        number = number.replace(',', '.')
    try:
        return float(number)
    except (ValueError, TypeError):
        return 0


def format_value(lineedit):
    try:
        if lineedit.text() != '':
            text = lineedit.text().replace(',', '.')
            current_value = float(text)
            formatted_value = "{:.2f}".format(current_value)
            lineedit.setText(formatted_value.replace('.', ','))
        else:
            lineedit.setText('0,00')    
    except ValueError:
        pass


def format_float(n):
    result = 0.00
    if n is None:
        return '0,00'
    else:
        if isinstance(n, str):
            result = float(n)
        else:
            result = n
        return f"{result:.2f}".replace('.', ',')



def remention_excel_columns(excel_file_path):
    wb = openpyxl.load_workbook(excel_file_path)
    ws = wb.active
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column]
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[openpyxl.utils.get_column_letter(
            column[0].column)].width = adjusted_width
    wb.save(excel_file_path)
