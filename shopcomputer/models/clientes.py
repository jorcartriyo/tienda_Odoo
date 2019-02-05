from odoo import models, fields, api

class Clientes(models.Model):
    _name = 'shopcomputer.clientes'
    codigo = fields.Integer('Codigo')
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')
    direccion = fields.Char('Direccion')
    provincia = fields.Char('Provincia')
    cif = fields.Char('CIF')

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

