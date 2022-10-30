# -*- coding: utf-8 -*-
{
    'name': "free_odoo_debranding",
    'description': """Remove branding everywhere in odoo for free""",
    'author': "DERICK TEMFACK",
    'website': "https://github.com/tderick/free_odoo_deranding",
    'category': 'Uncategorized',
    'version': '14.0.0.1',
    'application': True,
    'installable': True,
    'auto_install': True,
    'licence': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/views.xml',
    ],
    "qweb": ["static/src/xml/base.xml"]

}
