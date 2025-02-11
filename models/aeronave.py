from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Aeronave(models.Model):
    _name = 'quintofly.aeronave'
    _description = 'Aeronave'
    
    # Relación One2many con Vuelo
    vuelo_ids = fields.One2many('quintofly.vuelo', 'aeronave_id', string="Vuelos")

    foto = fields.Binary('Foto')
    tipo = fields.Char("Tipo", required=True)
    matricula = fields.Char("Matrícula", required=True)
    modelo = fields.Char("Modelo", required=True)
    capacidad_peso = fields.Float("Capacidad de peso (Kg)", required=True)

    # Constraint que hace que matrícula sea única
    _sql_constraints = [
        ('matricula_uniq', 'UNIQUE(matricula)', 'La matrícula tiene que ser única')
    ]

    @api.constrains('matricula')
    def _check_matricula(self):
        """
        Valida que la matrícula tenga 2 letras seguidas de 3 números.
        """
        import re
        patron = re.compile(r'^[A-Z]{2}\d{3}$')
        
        for record in self:
            if not patron.match(record.matricula.upper()):
                raise ValidationError("La matrícula debe tener 2 letras seguidas de 3 números. Ejemplo: AB123")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.matricula} - {record.tipo} {record.modelo}"
            result.append((record.id, name))
        return result
