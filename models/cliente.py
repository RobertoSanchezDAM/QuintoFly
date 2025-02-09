# -- coding: utf-8 --

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'quintofly.cliente'
    _inherit = 'quintofly.persona'
    _description = 'Cliente'

    email = fields.Char("Email")
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.dni} --- {record.nombre}" if record.dni else record.nombre
            result.append((record.id, name))
        return result

    #constraint que hace que email sea UNIQUE
    _sql_constraints=[
        ('email_uniq',
        'UNIQUE(email)',
        'El email tiene que ser único')
        ]