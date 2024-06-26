{
    'name': 'Partners Module',
    'version': '1.0',
    'depends': ['base','web'],
    'data': [
        'views/template.xml',
        'views/partners_display.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
