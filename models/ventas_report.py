import io
import base64
import xlsxwriter
from datetime import datetime
from odoo import models, fields

class VentasReport(models.TransientModel):
    _name = 'ventas.report'
    _description = 'Reporte de Ventas'

    name = fields.Char(string='Nombre del Reporte', default='Reporte de Ventas')

    def generate_excel_report(self):
        # Determinar el tipo de reporte para el log
        report_type = 'ventas'
        current_time = fields.Datetime.now()

        # Buscar el registro de log para este reporte
        export_log = self.env['report.export.log'].search([('report_type', '=', report_type)], limit=1)
        if not export_log:
            # Si no existe, asignamos una fecha de inicio lejana
            last_export = datetime(2000, 1, 1, 0, 0, 0)
            export_log = self.env['report.export.log'].create({
                'report_type': report_type,
                'last_export_time': current_time,
            })
        else:
            last_export = fields.Datetime.from_string(export_log.last_export_time)

        # Aquí filtrarías los registros de ventas creados entre last_export y current_time.
        # Por ejemplo, en producción:
        # orders = self.env['sale.order'].search([('create_date', '>=', last_export), ('create_date', '<', current_time)])
        # Y luego extraerías los campos necesarios de cada orden.
        #
        # Para el ejemplo, usaremos datos de muestra:
        data = [
            ['Cliente A', 'PV001', 1000, 1, 1, 1000],
            ['Cliente B', 'PV002', 2000, 1, 0, 0],
        ]

        # Crear el Excel
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Ventas')
        
        headers = ['Cliente', 'Pedido de venta', 'Monto total', 'Facturas emitidas', 'Facturas pagadas', 'Total de pagos']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        
        # Escribir los datos (los nuevos registros)
        for row_num, row_data in enumerate(data, 1):
            for col_num, cell_data in enumerate(row_data):
                worksheet.write(row_num, col_num, cell_data)
        
        workbook.close()
        output.seek(0)
        file_data = output.read()

        # Actualizamos la marca de tiempo de la última exportación
        export_log.last_export_time = current_time

        return base64.b64encode(file_data)