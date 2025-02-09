# -- coding: utf-8 --

from odoo import models, fields, api

class LineaVenta(models.Model):
    _name = 'quintofly.lineaventa'
    _description = 'Línea de Venta'

    #relación de campos
    venta_id = fields.Many2one('quintofly.venta', string="Venta", required=True)
    subtotal = fields.Float("Subtotal", required=True)
    vuelo_id = fields.Many2one('quintofly.vuelo', string="Vuelo asociado", required=True)
    num_horas = fields.Integer("Número de horas", required=True)
    
    #cosnstraint para que venta_id sea UNIQUE
    _sql_constraints=[
        ('venta_id_uniq',
        'UNIQUE(venta_id)',
        'El id de la Venta tiene que ser único')
        ]

