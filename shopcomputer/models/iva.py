from odoo import models, fields, api

class Iva(models.Model):
    _name = 'shopcomputer.iva'
    nombre = fields.Char('Tipo de IVA')
    cantidad= fields.Integer()

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
