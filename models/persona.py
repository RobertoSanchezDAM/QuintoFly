# -- coding: utf-8 --

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    #validacion de dni
    @api.constrains('dni')
    def _check_dni(self):
        """
        Valida que el DNI tenga 8 dígitos seguidos de una letra correcta.
        """
        import re
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        patron = re.compile(r'^(\d{8})([A-Z])$')

        for record in self:
            dni = record.dni.upper()
            match = patron.match(dni)
            if not match:
                raise ValidationError("El DNI debe tener 8 dígitos seguidos de una letra. Ejemplo: 12345678Z")
            numero = int(match.group(1))
            letra_correcta = letras[numero % 23]
            if letra_correcta != match.group(2):
                raise ValidationError(f"La letra del DNI no es correcta. Debe ser {letra_correcta}.")