from odoo import models, fields

class PartnerReferenceModel(models.Model):
    _name = 'reference.module'
    _description = 'refernce.module'
    partner_id = fields.Many2one('res.partner', string='Partner', default=lambda self: self.env.user.partner_id,required=True)
    company_name = fields.Char('Company')
    company_industry = fields.Char('Industry')
    project_name = fields.Char('Project Name')
    project_description = fields.Text('Project Description')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    email = fields.Char(string='Email', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    country = fields.Many2one('res.country',string='Country')
    job_level = fields.Char('Job Level')
    job_function = fields.Char("Job Function")
    product_cloud_interest = fields.Char('Product Cloud Interest')
    is_this_an_RFP = fields.Char('Is this an RFP?')
    budget_project = fields.Char('budget')
