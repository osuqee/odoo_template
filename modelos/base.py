from odoo import models, fields, api

class base(models.Model):
    _name = 'mipollita.base'
    _description = 'Clase base para heredar'
    
    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')