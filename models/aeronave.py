# -- coding: utf-8 --

from odoo import models, fields, api

class Aeronave(models.Model):
    _name = 'quintofly.aeronave'
    _description = 'Aeronave'

    matricula = fields.Char("Matrícula", required=True)
    tipo = fields.Char("Tipo")
    modelo = fields.Char("Modelo")
    capacidad_peso = fields.Float("Capacidad de peso")
