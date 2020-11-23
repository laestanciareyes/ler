# -*- coding: utf-8 -*-
{
    'name': "Soluciones Estrategicas",

    'summary': """
        Modulo de personalización para el cliente La Estancia Reyes S.A. de C.V. en San Ana, El Salvador""",

    'description': """
        Se incluye la personalización de Vistas, desarrollos personalizados y exclusivos para el cliente.
    """,

    'author': "Soluciones Estrategicas AC",
    'website': "http://www.solucionesestrategicas-ac.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/custom_views.xml',
        'reports/reportes.xml',
        'reports/solicitud_cliente.xml',
        #'reports/reporte_corrida_financiera.xml',
        'reports/corrida_financiera.xml',
        
        #'views/templates.xml',
        
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
