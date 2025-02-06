# -- coding: utf-8 --

from odoo import models, fields, api

class Piloto(models.Model):
    _name = 'quintofly.piloto'
    _inherit = 'quintofly.persona'
    _description = 'Piloto'

    num_licencia = fields.Integer("Número de licencia")
    anyos_experiencia = fields.Integer("Años de experiencia")
