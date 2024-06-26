from odoo import http
from odoo.http import request
class YavarProductsController(http.Controller):
    @http.route('/',type='http',auth='user')
    def display_website(self,**kw):
        return request.render('product_yavar.index_template')