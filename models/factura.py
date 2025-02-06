# -- coding: utf-8 --

from odoo import models, fields, api

class Factura(models.Model):
    _name = 'quintofly.factura'
    _description = 'Factura'

    venta_id = fields.Many2one('quintofly.venta', string="Venta relacionada", required=True)
    cliente_id = fields.Many2one('quintofly.cliente', string="Cliente", required=True) 
    
    identificador = fields.Integer("Identificador", required=True)
    iva = fields.Float("IVA", required=True)
    subtotal = fields.Float("Subtotal", required=True)
    importe_total = fields.Float("Importe Total", required=True)
    concepto = fields.Char("Concepto", required=True)
    descripcion = fields.Text("Descripción")
    fecha_factura = fields.Datetime("Fecha de Factura", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada')
    ], "Estado", default='pendiente', required=True)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.identificador} --- {record.concepto}"
            result.append((record.id, name))
        return result
