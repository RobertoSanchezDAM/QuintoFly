# -- coding: utf-8 --

from odoo import models, fields, api

class Piloto(models.Model):
    _name = 'quintofly.piloto'
    _inherit = 'quintofly.persona'
    _description = 'Piloto'

    num_licencia = fields.Integer("Número de licencia", required=True)
    anyos_experiencia = fields.Integer("Años de experiencia", required=True)

    #constraist para que el numero de licencia sea UNIQUE
    _sql_constraints=[
        ('num_licencia_uniq',
        'UNIQUE(num_licencia)',
        'El numero de licencia tiene que ser único')
    ]

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.num_licencia} - {record.nombre}"
            result.append((record.id, name))
        return result