# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class Huevos(models.Model):
    _name = 'mipollita.huevos'
    _description = 'Tipos de huevos'
    _inherit = 'mipollita.base'
    
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    
    # pollita_ids = fields.Many2one('mipollita.pollita', string='polla')
    