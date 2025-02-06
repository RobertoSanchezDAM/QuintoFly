# -- coding: utf-8 --

from odoo import models, fields, api

class Vuelo(models.Model):
    _name = 'quintofly.vuelo'
    _description = 'Vuelo'
 
    piloto_ids = fields.Many2many('quintofly.piloto', string="Pilotos", required=True)
    origen = fields.Char("Origen", required=True)
    aeronave_id = fields.Many2one('quintofly.aeronave', string="Aeronave", required=True)
    destino = fields.Char("Destino", required=True)
    fecha_vuelo = fields.Datetime("Fecha del vuelo", required=True)


    def name_get(self):
        result = []
        for record in self:
            name = f"Vuelo {record.id} --- {record.origen} - {record.destino} --- {record.fecha_vuelo}"
            result.append((record.id, name))
        return result