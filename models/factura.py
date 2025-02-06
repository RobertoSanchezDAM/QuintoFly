# -- coding: utf-8 --

from odoo import models, fields, api

class Factura(models.Model):
    _name = 'quintofly.factura'
    _description = 'Factura'

    venta_id = fields.Many2one('quintofly.venta', string="Venta relacionada")
    cliente_id = fields.Many2one('quintofly.cliente', string="Cliente") 
    
    identificador = fields.Integer("Identificador", required=True)
    iva = fields.Float("IVA")
    subtotal = fields.Float("Subtotal")
    importe_total = fields.Float("Importe Total")
    concepto = fields.Char("Concepto")
    descripcion = fields.Text("Descripción")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada')
    ], "Estado", default='pendiente')
    fecha_factura = fields.Datetime("Fecha de Factura")
