# -- coding: utf-8 --

from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'quintofly.servicio'
    _description = 'Servicio'

    nombre = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
    precio_hora = fields.Float("Precio por hora")
    precio_base = fields.Float("Precio base")