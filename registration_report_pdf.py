import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, Frame, Image, PageBreak,
                                PageTemplate, Table, TableStyle)
from reportlab.platypus.flowables import Spacer


class RegistrationReportPdf:
    def __init__(self, filename, dataset, col_widths, title):
        self.filename = filename
        self.elements = []
        self.data = [list(dataset.columns)] + dataset.values.tolist()
        self.table = Table(self.data, colWidths=col_widths)
        self.logo_filename = './images/soon/guiafertil-02.png'
        self.titleReport = title

    def initialize_table_style(self):
        self.table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), (1, 1, 1)),
                                        ('TEXTCOLOR', (0, 0), (-1, -1), (0, 0, 0)), 
                                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
                                        ('FONTSIZE', (0, 0), (-1, 0), 8),
                                        ('FONTSIZE', (0, 1), (-1, -1), 8),  
                                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])) 
 
    def generate_header(self, canvas):
        logo = Image(self.logo_filename, width=100, height=50)
        logo.drawOn(canvas, 15, 550)
        canvas.drawString(125, 570, self.titleReport)

    def generate_footer(self, canvas):
        page_num = canvas.getPageNumber()
        text = f"Página {page_num}"
        canvas.drawString(700, 20, text)

    def generate_report(self):
        doc = BaseDocTemplate(self.filename, pagesize=landscape(letter), rightMargin=72, leftMargin=72, topMargin=0, bottomMargin=30)
        
        table_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 1*inch, id='normal')

        page_template = PageTemplate(id='main_template', frames=[table_frame], onPage=self.generate_header_footer)

        doc.addPageTemplates(page_template)

        self.elements.append(self.table)
        self.elements.append(PageBreak())

        doc.build(self.elements)
        os.system(f'start acrobat "{self.filename}"')

    def generate_header_footer(self, canvas, doc):
        self.generate_header(canvas)
        self.generate_footer(canvas)
