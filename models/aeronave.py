# -- coding: utf-8 --

from odoo import models, fields, api

class Aeronave(models.Model):
    _name = 'quintofly.aeronave'
    _description = 'Aeronave'

    tipo = fields.Char("Tipo", required=True)
    matricula = fields.Char("Matrícula", required=True)
    modelo = fields.Char("Modelo", required=True)
    capacidad_peso = fields.Float("Capacidad de peso (Kg)", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.matricula} --- {record.tipo} {record.modelo}"
            result.append((record.id, name))
        return result