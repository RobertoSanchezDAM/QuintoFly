# -- coding: utf-8 --

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Cliente(models.Model):
    _name = 'quintofly.cliente'
    _inherit = 'quintofly.persona'
    _description = 'Cliente'

    email = fields.Char("Email")
    
    #constraint que hace que email sea UNIQUE
    _sql_constraints=[
        ('email_uniq',
        'UNIQUE(email)',
        'El email tiene que ser único')
    ]

    

    #validacion de email
    @api.constrains('email')
    def _check_email(self):
        """
        Valida que el email tenga el formato direccionemail@dominio.xx
        """
        import re
        patron = re.compile(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$')
        
        for record in self:
            if record.email and not patron.match(record.email):
                raise ValidationError("El email debe tener el formato direccionemail@dominio.xx")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.dni} - {record.nombre}" if record.dni else record.nombre
            result.append((record.id, name))
        return result