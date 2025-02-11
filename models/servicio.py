# -- coding: utf-8 --

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Servicio(models.Model):
    _name = 'quintofly.servicio'
    _description = 'Servicio'

    tiposerv = fields.Selection([
        ('turismo', 'Turismo por Andalucía'),
        ('transporte', 'Transporte'),
        ('fumigacion', 'Fumigación'),
        ('clases', 'Clases de pilotaje'),
    ], "Tipo de Servicio", default="turismo", required=True)
    descripcion = fields.Text("Descripción")
    precio_hora = fields.Float("Precio por hora", required=True)
    precio_base = fields.Float("Precio base", required=True)

    @api.constrains('precio_hora', 'precio_base')
    def _check_precios(self):
        """
        Valida que los precios no sean negativos.
        """
        for record in self:
            if record.precio_hora < 0:
                raise ValidationError("El precio por hora no puede ser negativo.")
            if record.precio_base < 0:
                raise ValidationError("El precio base no puede ser negativo.")

    def name_get(self):
        result = []
        for record in self:
            name = f"Servicio {record.id} - {record.tiposerv}"
            result.append((record.id, name))
        return result