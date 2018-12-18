# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Pelanggan(models.Model):
    _name = 'nursery.customer'

    name = fields.Char("Nama Pelanggan", required=True)
    email = fields.Char(help="To receive the newsletter")
