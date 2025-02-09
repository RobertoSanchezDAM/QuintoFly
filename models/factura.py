# -- coding: utf-8 --

from odoo import models, fields, api

class Factura(models.Model):
    _name = 'quintofly.factura'
    _description = 'Factura'

    venta_id = fields.Many2one('quintofly.venta', string="Venta relacionada", required=True)
    cliente_id = fields.Many2one('quintofly.cliente', string="Cliente", required=True) 
    
    identificador = fields.Integer("Identificador", required=True)
    iva = fields.Float("IVA", required=True)
    subtotal = fields.Float("Subtotal")
    importe_total = fields.Float("Importe Total", compute="_compute_importe_total", store=True)
    concepto = fields.Char("Concepto", required=True)
    descripcion = fields.Text("Descripción")
    fecha_factura = fields.Datetime("Fecha de Factura", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada')
    ], "Estado", default='pendiente', required=True)
    
    _sql_constraints=[
        ('identificador_uniq',
        'UNIQUE(identificador)',
        'El identificador tiene que ser único')
        ]

    @api.onchange('venta_id')
    def _onchange_venta_id(self):
        if self.venta_id:
            self.subtotal = self.venta_id.total
        
    @api.depends('subtotal', 'iva')
    def _compute_importe_total(self):
        for record in self:
            record.importe_total = record.subtotal + (record.subtotal * (record.iva / 100))

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.identificador} --- {record.concepto}"
            result.append((record.id, name))
        return result
