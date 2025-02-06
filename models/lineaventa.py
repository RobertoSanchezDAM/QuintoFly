# -- coding: utf-8 --

from odoo import models, fields, api

class LineaVenta(models.Model):
    _name = 'quintofly.lineaventa'
    _description = 'Línea de Venta'

    venta_id = fields.Many2one('quintofly.venta', string="Venta")
    vuelo_id = fields.Many2one('quintofly.vuelo', string="Vuelo asociado")
     
    subtotal = fields.Float("Subtotal")
    num_horas = fields.Integer("Número de horas")
