# -- coding: utf-8 --

from odoo import models, fields, api

class LineaVentaServicio(models.Model):
    _name = 'quintofly.lineaventaservicio'
    _description = 'Relación entre Línea de Venta y Servicio'

    lineaventa_id = fields.Many2one('quintofly.lineaventa', string="Línea de Venta", required=True)
    servicio_id = fields.Many2one('quintofly.servicio', string="Servicio", required=True)
    venta_id = fields.Many2one('quintofly.venta', string="Venta asociada", required=True) 