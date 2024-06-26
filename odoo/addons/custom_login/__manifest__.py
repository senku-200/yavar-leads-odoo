{
    'name': 'Custom Login',
    'description': 'Custom login page for Odoo',
    'category': 'Customization',
    'author':'yavar',
    'version': '1.0',
    'depends': ['web'],
    'data': [
        'views/login_template.xml',
        'views/assests.xml', 
    ],
    'assets': {
        'web.assets_backend': [
            'custom_login/static/src/scss/login.scss',
        ],
        'web.assets_frontend': [
            'custom_login/static/src/scss/login.scss',
        ],
    },
}   
