# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Pabrik Pesawat',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manajemen Pesawat dan Pelanggan',
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'depends': ['web'],
    'data': [
        'data/actions.xml',
        'data/plant_views.xml',
        'data/order_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
