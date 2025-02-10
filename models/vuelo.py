from odoo import models, fields, api

class Vuelo(models.Model):
    _name = 'quintofly.vuelo'
    _description = 'Vuelo'
    
    # Relación Many2many con Pilotos
    piloto_ids = fields.Many2many('quintofly.piloto', string="Pilotos", required=True)
    aeronave_id = fields.Many2one('quintofly.aeronave', string="Aeronave", required=True)
    
    origen = fields.Char("Origen", required=True)
    destino = fields.Char("Destino", required=True)
    fecha_salida = fields.Datetime("Fecha y hora de salida", required=True)
    fecha_llegada = fields.Datetime("Fecha y hora de llegada", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"Vuelo {record.id} - {record.origen} -> {record.destino} / {record.fecha_salida}"
            result.append((record.id, name))
        return result