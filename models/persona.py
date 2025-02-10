# -- coding: utf-8 --

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'quintofly.persona'
    _description = 'Persona'

    dni = fields.Char("DNI", size = 9, required=True)
    nombre = fields.Char("Nombre", size = 20, required=True)
    apellido = fields.Char("Apellido", size = 20, required=True)
    sexo = fields.Selection([
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),],
    "Sexo", default = "masculino", required=True)
    fecha= fields.Datetime('Fecha de nacimiento', required=True)
    telefono = fields.Char("Telefono", size = 9, required=True)
    direccion = fields.Char("Dirección", size = 60)
    
    #constraint que el dni sea UNIQUE
    _sql_constraints=[
        ('dni_uniq',
        'UNIQUE(dni)',
        'El DNI tiene que ser único')
    ]
