from odoo import models, fields, api

class Vuelo(models.Model):
    _name = 'quintofly.vuelo'
    _description = 'Vuelo'
    
    # Relación Many2many con Pilotos
    piloto_ids = fields.Many2many('quintofly.piloto', string="Pilotos", required=True)
    
    origen = fields.Char("Origen", required=True)
    aeronave_id = fields.Many2one('quintofly.aeronave', string="Aeronave", required=True)
    destino = fields.Char("Destino", required=True)
    fecha_salida = fields.Datetime("Fecha y hora de salida", required=True)
    fecha_llegada = fields.Datetime("Fecha y hora de llegada", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"Vuelo {record.id} - {record.origen} -> {record.destino} / {record.fecha_salida}"
            result.append((record.id, name))
        return result
    
    @api.constrains('piloto_ids', 'fecha_salida', 'fecha_llegada')
    def _check_piloto_schedule(self):
        for vuelo in self:
            # Convertir las fechas de salida y llegada solo a fecha (sin horas)
            fecha_salida = vuelo.fecha_salida.date()
            fecha_llegada = vuelo.fecha_llegada.date()

            # Verificar cada piloto en este vuelo
            for piloto in vuelo.piloto_ids:
                # Buscar vuelos del piloto que se solapen con el vuelo actual (solo la fecha)
                vuelos_conflictivos = self.search([
                    ('piloto_ids', '=', piloto.id),
                    ('id', '!=', vuelo.id),
                    ('fecha_salida', '>=', str(fecha_salida)),
                    ('fecha_llegada', '<=', str(fecha_llegada))
                ])
                
                # Si encontramos vuelos conflictivos, mostramos un mensaje
                if vuelos_conflictivos:
                    raise models.ValidationError(f"El piloto {piloto.nombre} ya tiene un vuelo programado el día {fecha_salida}.")