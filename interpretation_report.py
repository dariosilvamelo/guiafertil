import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import constants
from tools import format_float


class InterpretationReport():
    def __init__(self, initial_depth, final_depth, prnt, tca, saturation, expected_saturation, soil_attributes, filename, micros, npk_clay, npk_p_rem, limestone, plaster, report_header):
        self.filename = filename
        self.initial_depth = initial_depth
        self.final_depth = final_depth
        self.prnt = prnt
        self.tca = tca
        self.saturation = saturation
        self.expected_saturation = expected_saturation
        self.soil_attributes = soil_attributes
        self.micros = micros
        self.npk_clay = npk_clay
        self.npk_p_rem = npk_p_rem
        self.limestone = limestone
        self.plaster = plaster
        self.header = report_header
        self.logo_filename = constants.LOGO_REPORT

        self.page_width, self.page_height = A4

        self.c = canvas.Canvas(filename, pagesize=(self.page_width, self.page_height))
        self.c.setFillColor("black")

        self.font_type = "Courier-Bold"
        self.reference_font_type = "Courier"

        self.title_font_size = 10
        self.font_size = 10
        self.reference_font_size = 7

        self.line_spacing = 3.5

        self.line_position = self.point_to_mm(self.page_height) - self.line_spacing

        self.page = 1
        self.end_page = 13.500000000000057

        self.columns = [5, 30, 40, 67, 105, 143, 180]

    def point_to_mm(self, point):
        return point * 25.4 / 72

    def mm_to_point(self, mm):
        return mm * 72 / 25

    def report_header(self):
        self.c.setFont(self.font_type, self.font_size)
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawImage(self.logo_filename, self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), width=125, height=50)
        self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position + self.line_spacing), self.header['title'] + ' Cultura(' + self.npk_clay['culture'] + ')')

        self.c.setFont(self.font_type, self.reference_font_size)
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position + self.line_spacing), 'Produtor.........: '+self.header['producer'])
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position + self.line_spacing), 'Talhão...........: '+self.header['plots'])
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position + self.line_spacing), 'Sist. de Plantio.: '+self.header['planting_system'])
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position + self.line_spacing), 'Área.............: '+self.header['area'])
        self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position + self.line_spacing), 'Altitude : '+self.header['altitude'])
        self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position + self.line_spacing), 'Safra : '+self.header['period'])

    def generate_report(self):
        self.report_header()
        culture = self.npk_clay['culture']
        total_items = len(self.soil_attributes)
        sulfur_S = False
        for index, field in enumerate(self.soil_attributes):

            if field[0][0] == 'S':
                sulfur_S = True

            if (field[2] > 0) or (field[0][0] in ('Al3+', 'm')):

                self.line_position = self.line_position - self.line_spacing
                self.c.setFont(self.font_type, self.font_size)
                self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

                self.line_position = self.line_position - self.line_spacing
                self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), field[0][1]+'('+field[0][0]+')')
                self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), format_float(field[2]))
                self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), field[0][2])
                self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), '(' + field[1] + ')')

                self.line_position = self.line_position - self.line_spacing
                if field[0][0] == 'P' or field[0][0] == 'S':
                    self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '(Pelo teor de ' + field[3]+')')

                self.line_position = self.line_position - self.line_spacing
                self.c.setFont(self.font_type, self.reference_font_size)
                if field[0][0] == constants.M:
                    self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), 'Valor máximo tolerado:')

                self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), 'Valores de referência '+field[0][2]+' :')

                self.line_position = self.line_position - self.line_spacing
                self.c.setFont(self.reference_font_type, self.reference_font_size)

                if field[0][0] in (constants.PH_H2O, constants.PH_CACL2):
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), constants.LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), constants.GOOD)
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), constants.HIGH_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_HIGH_AVAILABILITY)

                elif field[0][0] in (constants.AL, constants.SB, constants.H_AL, constants.CTC_EFFECTIVE, constants.CTC_PH7, constants.M, constants.V):
                    if field[0][0] == constants.M:
                        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), 'cultura : '+culture)
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), constants.LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), constants.AVERAGE_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), constants.HIGH_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_HIGH_AVAILABILITY)

                elif field[0][0] == 'P' and culture == constants.WHEAT:
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), constants.LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), constants.AVERAGE_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), constants.GOOD)

                else:
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), constants.LOW_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), constants.AVERAGE_AVAILABILITY)
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), constants.GOOD)
                    self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), constants.VERY_GOOD)

                self.line_position = self.line_position - self.line_spacing
                self.c.setFont(self.reference_font_type, self.reference_font_size)

                if field[0][0] == constants.M:
                    self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), format_float(self.saturation[constants.M]) + field[0][2])

                if field[0][0] == 'P' and culture == 'Trigo':
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), field[0][0]+' <  '+ field[0][3])
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), field[0][3]+' <= '+ field[0][0] +' < '+ field[0][4])
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), field[0][4]+' <= '+ field[0][0] +' < '+ field[0][5])
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), field[0][5]+' <= '+ field[0][0])
                else:
                    self.c.drawString(self.mm_to_point(self.columns[2]), self.mm_to_point(self.line_position-self.line_spacing), field[0][0]+' <  '+ field[0][3])
                    self.c.drawString(self.mm_to_point(self.columns[3]), self.mm_to_point(self.line_position-self.line_spacing), field[0][3]+' <= '+ field[0][0] +' < '+ field[0][4])
                    self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing), field[0][4]+' <= '+ field[0][0] +' < '+ field[0][5])
                    self.c.drawString(self.mm_to_point(self.columns[5]), self.mm_to_point(self.line_position-self.line_spacing), field[0][5]+' <= '+ field[0][0] +' < '+ field[0][6])
                    self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), field[0][6]+' <= '+ field[0][0])

            if self.line_position == self.end_page:
               self.line_position = self.line_position - self.line_spacing
               self.line_position = self.line_position - self.line_spacing
               self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), 'Página: '+str(self.page))
               self.page=self.page+1
               self.line_position = self.point_to_mm(self.page_height) - self.line_spacing

               if index != ( total_items - 1 ):
                   self.c.showPage()
                   self.report_header()

            elif index == ( total_items - 1):
                self.line_position = self.end_page
                self.line_position = self.line_position - self.line_spacing
                self.line_position = self.line_position - self.line_spacing
                self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), 'Página: '+str(self.page))


        self.page=self.page+1
        self.line_position = self.point_to_mm(self.page_height) - self.line_spacing
        self.c.showPage()
        self.report_header()
        self.line_position = self.line_position - self.line_spacing
        self.c.setFont(self.font_type, self.font_size)

        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Recomendação de fertilizantes e corretivos.')
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Adubação mineral de N-P-K (kg/ha):')

        self.c.setFont(self.reference_font_type, self.font_size)
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Pelo teor de Argila:')

        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'N.....: '+format_float(self.npk_clay['N'][0])+' (plantio)')
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'P2O5..: '+format_float(self.npk_clay['P'])+' (plantio)')
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'N.....: '+format_float(self.npk_clay['N'][1])+' (cobertura)')
        self.line_position = self.line_position - self.line_spacing
        if self.npk_clay['culture'] == constants.WHEAT:
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'K2O...: '+format_float(self.npk_clay['k'])+' (cobertura)')
        else:
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'K2O...: '+format_float(self.npk_clay['k'])+' (plantio e ou cobertura)')

        if (self.npk_clay['culture'] != constants.WHEAT) and (self.npk_p_rem != {}):
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Pelo teor de P-REM:')

            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'N.....: '+format_float(self.npk_p_rem['N'][0])+' (plantio)')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'P2O5..: '+format_float(self.npk_p_rem['P'])+' (plantio)')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'N.....: '+format_float(self.npk_p_rem['N'][1])+' (cobertura)')
            self.line_position = self.line_position - self.line_spacing
            if self.npk_p_rem['culture'] == constants.WHEAT:
                self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'K2O...: '+format_float(self.npk_p_rem['k'])+' (cobertura)')
            else:
                self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'K2O...: '+format_float(self.npk_p_rem['k'])+' (plantio e ou cobertura)')


        self.c.setFont(self.font_type, self.font_size)
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Adubação mineral de micronutrientes (kg/ha):')
        
        self.line_position = self.line_position - self.line_spacing
        self.c.setFont(self.reference_font_type, self.font_size)
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Dose para aplicações a lanço, para aplicação no sulco de plantio, é recomendado 1/4 da dose.')

        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Zn....: '+format_float(self.micros['Zn']))
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'B.....: '+format_float(self.micros['B']))
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Cu....: '+format_float(self.micros['Cu']))
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Mn....: '+format_float(self.micros['Mn']))
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Mo....: '+format_float(self.micros['Mo']))
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Co....: '+format_float(self.micros['Co']))

        self.c.setFont(self.font_type, self.font_size)
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        if (sulfur_S == True) and (self.micros['S'] > 0):
            
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Adubação mineral de Enxofre S (kg/ha):')

            self.line_position = self.line_position - self.line_spacing
            self.c.setFont(self.reference_font_type, self.font_size)
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Dose para aplicação em plantio ou em cobertura.')

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'S.....: '+format_float(self.micros['S']))

            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        if (self.micros['Mg2+'] > 0):
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Adubação mineral de Magnésio Mg (kg/ha):')

            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Dose para aplicação em plantio ou em cobertura.')

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Mg....: '+format_float(self.micros['Mg2+']))

            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        if self.limestone != {}:
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Calcário:')
            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Fazer aplicação 3 a 6 meses antes do plantio.')

            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Profundidade de aplicação (cm) ..: '+format_float(self.final_depth)+' - ( '+format_float(self.initial_depth)+' a '+format_float(self.final_depth)+' )')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'PRNT do calcário (%).............: '+format_float(self.prnt))
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Superficie de aplicação (%)......: 100,00')
        
            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Método da neutralização de Al3+ e elevação dos teores de Ca2+ e Mg2+.')
        
            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de calcário (TON/ha)..: '+format_float(self.limestone['ARGILA'])+' (pelo teor de argila)')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de calcário (TON/ha)..: '+format_float(self.limestone['P-REM'])+' (pelo teor de P-REM)')

            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Método de saturação por bases.')

            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de calcário (TON/ha)..: '+format_float(self.limestone['SATURAÇÃO POR BASES']))
            self.c.drawString(self.mm_to_point(self.columns[4]), self.mm_to_point(self.line_position-self.line_spacing),'(para uma saturação esperada (Ve) = '+format_float(self.expected_saturation)+'%)')

            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing), '------------------------------------------------------------------------------------------------')

        if self.plaster != {}:
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Gesso:')

            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Espessura da camada (cm) ........: '+format_float(self.final_depth-self.initial_depth)+' - ( '+format_float(self.initial_depth)+' a '+format_float(self.final_depth)+' )')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Teor de Ca (TCa) (%).............: '+format_float(self.tca))

            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de gesso (TON/ha).....: '+format_float(self.plaster['ARGILA'])+' (pelo teor de argila)')

            if self.tca > 0:
                self.line_position = self.line_position - self.line_spacing
                self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de gesso (TON/ha).....: '+format_float(self.plaster['P-REM'])+' (pelo teor de P-REM)')

            self.c.setFont(self.font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Recomendação com base na determinação da necessidade de calcário (NC).')

            self.c.setFont(self.reference_font_type, self.font_size)
            self.line_position = self.line_position - self.line_spacing
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de gesso (TON/ha).....: '+format_float(self.plaster['NC - ARGILA'])+' (NC pelo teor de argila)')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de gesso (TON/ha).....: '+format_float(self.plaster['NC - P-REM'])+' (NC pelo teor de P-REM)')
            self.line_position = self.line_position - self.line_spacing
            self.c.drawString(self.mm_to_point(self.columns[0]), self.mm_to_point(self.line_position-self.line_spacing),'Quantidade de gesso (TON/ha).....: '+format_float(self.plaster['NC - SATURAÇÃO POR BASES'])+' (NC pela saturação por bases)')
        
        
        self.line_position = self.end_page
        self.line_position = self.line_position - self.line_spacing
        self.line_position = self.line_position - self.line_spacing
        self.c.drawString(self.mm_to_point(self.columns[6]), self.mm_to_point(self.line_position-self.line_spacing), 'Página: '+str(self.page))

        self.c.save()
        try:
            os.startfile(self.filename)
        except AttributeError:
            os.system('xdg-open ' + self.filename)