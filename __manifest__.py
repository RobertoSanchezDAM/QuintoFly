# -*- coding: utf-8 -*-
{
    'name': "QuintoFly",

    'summary': """
        Agencia de viajes - QuintoFly""",

    'description': """
        ¡¡Vuela a buen precio con nuestra Agencia de Viajes!!
    """,

    'author': "Pablo Suero, Roberto Sánchez, Adrián Serrano",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # installable application
    'installable': True,
    'application': True,

    # always loaded
    'data': [

        #views de las clases
        'security/ir.model.access.csv',
        'views/piloto_view.xml',
        'views/cliente_view.xml',
        'views/vuelo_view.xml',
        'views/venta_view.xml',
        'views/factura_view.xml',
        'views/servicio_view.xml',
        'views/aeronave_view.xml',
        'views/lineaventa_view.xml',
        'views/menu_view.xml',
        'views/views.xml',
        'views/templates.xml',

        #generacion de pdf 
        'views/report_factura.xml',  
        'views/factura_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
