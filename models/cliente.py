# -- coding: utf-8 --

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'quintofly.cliente'
    _inherit = 'quintofly.persona'
    _description = 'Cliente'

    email = fields.Char("Email")

    # me pesa el huevo izquierdo
    # y el derecho tambien
    
