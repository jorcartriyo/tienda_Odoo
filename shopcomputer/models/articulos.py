from odoo import models, fields, api

class Articulos(models.Model):
    _name = 'shopcomputer.articulos'
    codigo = fields.Integer('Codigo')
    nombre = fields.Char('Nombre')
    descripcion = fields.Text('Descripción')
    precio = fields.Float('Precio')
    stock = fields.Char('Stock')
    rebajado = fields.Boolean('Rebajado')

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

