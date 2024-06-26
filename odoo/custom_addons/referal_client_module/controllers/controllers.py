# -*- coding: utf-8 -*-
# from odoo import http


# class ReferalClientModule(http.Controller):
#     @http.route('/referal_client_module/referal_client_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/referal_client_module/referal_client_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('referal_client_module.listing', {
#             'root': '/referal_client_module/referal_client_module',
#             'objects': http.request.env['referal_client_module.referal_client_module'].search([]),
#         })

#     @http.route('/referal_client_module/referal_client_module/objects/<model("referal_client_module.referal_client_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('referal_client_module.object', {
#             'object': obj
#         })

