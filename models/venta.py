# -- coding: utf-8 --

from odoo import models, fields, api

class Venta(models.Model):
    _name = 'quintofly.venta'
    _description = 'Venta'

    cliente_id = fields.Many2one('quintofly.cliente', string="Cliente") 
    
    total = fields.Float("Total")
    observaciones = fields.Text("Observaciones")
    fecha_venta = fields.Datetime("Fecha de venta")