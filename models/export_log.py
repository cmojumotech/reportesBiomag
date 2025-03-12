from odoo import models, fields

class ReportExportLog(models.Model):
    _name = 'report.export.log'
    _description = 'Registro de Exportación de Reportes'

    report_type = fields.Char(string='Tipo de Reporte', required=True)
    last_export_time = fields.Datetime(string='Última Exportación')