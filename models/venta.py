# -- coding: utf-8 --

from odoo import models, fields, api

class Venta(models.Model):
    _name = 'quintofly.venta'
    _description = 'Venta'

    #relación de campos 
    cliente_id = fields.Many2one('quintofly.cliente', string="Cliente", required=True) 
    
    total = fields.Float("Total", required=True)
    fecha_venta = fields.Datetime("Fecha de venta", required=True)
    observaciones = fields.Text("Observaciones")
    
    def name_get(self):
        result = []
        for record in self:
            name = f"Venta - {record.id}"
            result.append((record.id, name))
        return result

