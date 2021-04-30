# -*- coding: utf-8 -*-
{
    'name': "mx_integritas_invoice_report/",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modifica el reporte de facturas a una estructura parecida al SAT.
    """,

    'author': "Integritas",
    'website': "https://integritas.mx",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
