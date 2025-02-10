from odoo import models, fields, api

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

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.matricula} - {record.tipo} {record.modelo}"
            result.append((record.id, name))
        return result
