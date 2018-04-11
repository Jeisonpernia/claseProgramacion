# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _




class claseunefa(models.Model):
    _name = "clase.unefa"
    

    name = fields.Char(string='Estudiante', required=True, readonly=False,)
    categoria_id = fields.Many2one('clase.categoria', string='Categoria', required=True)

   


class claseCategoria(models.Model):
    _name = "clase.categoria"
    

    name = fields.Char(string='Categoría', required=True, readonly=False,)
    codigo = fields.Integer(string='Codigo', required=True, readonly=False,)
    active = fields.Boolean(string='Activo', required=True, readonly=False,)
   
