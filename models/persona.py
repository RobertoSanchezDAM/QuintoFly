# -- coding: utf-8 --

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'quintofly.persona'
    _description = 'Persona'

    dni = fields.Char("DNI", size = 9)
    nombre = fields.Char("Nombre completo", size = 50)
    fecha= fields.Datetime('Fecha de nacimiento')
    sexo = fields.Selection([
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),],
    "Sexo", default = "masculino")
    direccion = fields.Char("Dirección", size = 60)
    telefono = fields.Char("Telefono", size = 9)