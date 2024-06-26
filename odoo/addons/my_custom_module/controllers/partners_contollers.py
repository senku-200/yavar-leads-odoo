from odoo import http
from odoo.http import request
import logging
class UserRegistrationController(http.Controller):

    @http.route('/partners/register', auth='public', website=True)
    def user_registration_form(self, **kw):
        countries = request.env['res.country'].sudo().search([])
        return http.request.render('my_custom_module.partners_list_template', {'countries':countries})

_logger = logging.getLogger(__name__)

class PartnerController(http.Controller):
    @http.route('/partners/create', type='http', auth="public", website=True, csrf=False)
    def create_partner(self, **kwargs):
        try:
            if request.httprequest.method == 'POST':
                _logger.info("Received data: %s", kwargs)
                partner_data = {
                    'company_name': kwargs.get('company_name'),
                    'company_industry': kwargs.get('company_industry'),
                    'project_name': kwargs.get('project_name'),
                    'project_description': kwargs.get('project_description'),
                    'first_name': kwargs.get('first_name'),
                    'last_name': kwargs.get('last_name'),
                    'email': kwargs.get('email'),
                    'phone_number': kwargs.get('phone_number'),
                    'country': kwargs.get('country'),
                    'job_level': kwargs.get('job_level'),
                    'job_function': kwargs.get('job_function'),
                    'product_cloud_interest': kwargs.get('product_cloud_interest'),
                    'is_this_an_RFP': kwargs.get('is_this_an_RFP'),
                    'budget_project': kwargs.get('budget_project'),
                }
                _logger.info("Processed partner data: %s", partner_data)
                new_partner = request.env['reference.module'].sudo().create(partner_data)
                _logger.info("New partner created with ID: %s", new_partner.id)
                return request.redirect('/partners/list')
        except Exception as e:
            _logger.error("Error creating partner: %s", e, exc_info=True)
            return request.render('my_custom_module.partners_list_template', {'error': str(e)})
        
        return request.render('my_custom_module.partners_list_template')


from odoo import http
from odoo.http import request

class UserTableController(http.Controller):

    @http.route('/partners/list', auth='public', website=True)
    def partners_list(self, **kw):
        user = request.env.user
        is_admin = request.env.user.has_group('base.group_erp_manager')
        if not is_admin:
            partner_id = request.env.user.partner_id.id
            docs = request.env['reference.module'].sudo().search([('partner_id', '=', partner_id)])
        else:
            docs = request.env['reference.module'].sudo().search([])
        isTrue = bool(docs)
        if isTrue:
            for record in docs:
                _logger.info('partner_company:%s',record.partner_id.company_name)
        return http.request.render('my_custom_module.partners_list_display', {'docs': docs,'isTrue':isTrue,'is_admin':is_admin})
    
    @http.route('/partners/unlink', auth='public', website=True)
    def unlink(self, **kw):
        is_admin = request.env.user.has_group('base.group_erp_manager')
        if not is_admin:
            partner_id = request.env.user.partner_id.id
            docs = request.env['reference.module'].sudo().search([('partner_id', '=', partner_id)])
        else:
            docs = request.env['reference.module'].sudo().search([])
        try:
            docs.unlink()
            return request.redirect('/partners/list')
        except Exception as e:
            return request.redirect('/partners/list')
         

