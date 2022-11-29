# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class Pollita(models.Model):
    _name = 'mipollita.pollita'
    _description = 'Tipos de pollas'
    _inherit = 'mipollita.base'
    
    name = fields.Char(string="Nombre", required=True)
    raza = fields.Char(string="Raza")
    description = fields.Text(string="Descripción")
    sexo = fields.Selection([('Hembra', 'Hemvra')], string="Sexo")
    
    # huevos_ids = fields.One2many('mipollita.huevos', 'pollita_id', string='huevos de la polla')