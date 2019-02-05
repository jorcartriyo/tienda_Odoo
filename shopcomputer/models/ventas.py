from odoo import models, fields, api

class Ventas(models.Model):
    _name = 'shopcomputer.ventas'
    cliente = fields.Many2one('shopcomputer.clientes','Cliente')
    fecha = fields.Date('Fecha de venta')
    articulo = fields.Many2one('shopcomputer.articulos','Articulo')
    cantidad = fields.Integer('Cantidad',required=True)
    precio = fields.Float('Precio',compute='_precio')
    subtotal = fields.Float(string='Subtotal', compute='_subtotal')
    iva = fields.Many2one('shopcomputer.iva','IVA')
    total = fields.Float(string='Total', compute='_total')


    @api.one
    def _precio(self):
        cursor = self.env.cr
        cursor.execute('select precio from shopcomputer_articulos where codigo=%s',(self.articulo.codigo,))
        for partner in cursor.fetchall():
            if (self.articulo.rebajado):
                self.precio= (partner[0]*0.95)
            else:
                self.precio = partner[0]
    @api.one
    @api.depends('precio','cantidad')
    def _subtotal(self):
        self.subtotal = self.precio * self.cantidad

    @api.one
    @api.depends('subtotal', 'iva')
    def _total(self):
        self.total = ((self.subtotal * (self.iva.cantidad / 100)) + self.subtotal)

