# -- coding: utf-8 --

from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'quintofly.servicio'
    _description = 'Servicio'

    tiposerv = fields.Selection([
    ('turismo', 'Turismo por Andalucía'),
    ('transporte', 'Transporte'),
    ('fumigacion', 'Fumigación'),
    ('clases', 'Clases de pilotaje'),],
    "Tipo de Servicio", default = "turismo", required=True)
    descripcion = fields.Text("Descripción")
    precio_hora = fields.Float("Precio por hora", required=True)
    precio_base = fields.Float("Precio base", required=True)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"Servicio {record.id} - {record.tiposerv}"
            result.append((record.id, name))
        return result