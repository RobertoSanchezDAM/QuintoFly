# -- coding: utf-8 --

from odoo import models, fields, api

class Vuelo(models.Model):
    _name = 'quintofly.vuelo'
    _description = 'Vuelo'

    fecha_vuelo = fields.Datetime("Fecha del vuelo")
    piloto_ids = fields.Many2many('quintofly.piloto', string="Pilotos")
    aeronave_id = fields.Many2one('quintofly.aeronave', string="Aeronave")
