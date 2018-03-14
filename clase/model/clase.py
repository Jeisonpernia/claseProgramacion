# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _




class claseunefa(models.Model):
    _name = "clase.unefa"
    

    name = fields.Char(string='Estudiante', required=True, readonly=False,)
   
