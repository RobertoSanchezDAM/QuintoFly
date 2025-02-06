# -- coding: utf-8 --

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'quintofly.cliente'
    _inherit = 'quintofly.persona'
    _description = 'Cliente'

    email = fields.Char("Email")

    # ESTOY CALVO DE COJONES
