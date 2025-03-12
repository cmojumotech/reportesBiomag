import io
import base64
import xlsxwriter
from datetime import datetime
from odoo import models, fields

class StockReport(models.TransientModel):
    _name = 'stock.report'
    _description = 'Reporte de Stock'

    name = fields.Char(string='Nombre del Reporte', default='Reporte de Stock')

    def generate_excel_report(self):
        report_type = 'stock'
        current_time = fields.Datetime.now()

        export_log = self.env['report.export.log'].search([('report_type', '=', report_type)], limit=1)
        if not export_log:
            last_export = datetime(2000, 1, 1, 0, 0, 0)
            export_log = self.env['report.export.log'].create({
                'report_type': report_type,
                'last_export_time': current_time,
            })
        else:
            last_export = fields.Datetime.from_string(export_log.last_export_time)

        # Aquí filtrarías los productos actualizados entre last_export y current_time.
        data = [
            ['Producto A', 50, 'Almacén 1', 'Categoría 1'],
            ['Producto B', 30, 'Almacén 2', 'Categoría 2'],
        ]

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Stock')
        
        headers = ['Producto', 'Cantidad', 'Ubicación', 'Categoría']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        
        for row_num, row_data in enumerate(data, 1):
            for col_num, cell_data in enumerate(row_data):
                worksheet.write(row_num, col_num, cell_data)
        
        workbook.close()
        output.seek(0)
        file_data = output.read()

        export_log.last_export_time = current_time

        return base64.b64encode(file_data)