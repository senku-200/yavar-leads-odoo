# -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request

# class ReferalClientModule(http.Controller):
    # @http.route('/referal_client_module/referal_client_module', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    # @http.route('/referal_client_module/referal_client_module/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('referal_client_module.listing', {
    #         'root': '/referal_client_module/referal_client_module',
    #         'objects': http.request.env['referal_client_module.referal_client_module'].search([]),
    #     })

    # @http.route('/referal_client_module/referal_client_module/objects/<model("referal_client_module.referal_client_module"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('referal_client_module.object', {
    #         'object': obj
    #     })
    # @http.route('/referal_form',type='http',auth='user',website=True)
    # def referal_form_view(self,**post):
    #     company_name = post.get('company_name')

    #     if company_name:
    #         request.env['referal_client_module.referal_client_module'].sudo().create(
    #             {
    #                 'company_name':company_name
    #             }
    #         )
    #         return request.redirect('/referal_form?submitted=1')
    #     return request.render('referal_view_template')



from odoo import http
from odoo.http import request

class UserController(http.Controller):

    @http.route('/users', type='http', auth='public', website=True)
    def list_users(self, **kwargs):
        users = request.env['referal_client_module.referal_client_module'].sudo().search([])
        return request.render('refer_client_module.partners_list_template', {'users': users})

    @http.route('/partners/create', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def create_user(self, **post):
        if 'name' in post and 'email' in post:
            request.env['referal_client_module.referal_client_module'].sudo().create({
                'name': post['name'],
                'email': post['email'],
            })
        return request.redirect('/users')
