# -*- coding: utf-8 -*-

from odoo import models, fields, api


class referal_client_module(models.Model):
    _name = 'referal_client_module.referal_client_module'
    _description = 'referal_client_module.referal_client_module'


    name = fields.Char(string='User Name', required=True)
    email = fields.Char(string='Email', required=True)
    # company_name = fields.Char('Company')
    # company_industy = fields.Char('Industry')
    # project_name = fields.Char('Project Name')
    # project_description = fields.Text('Project Description')
    # first_name = fields.Char('First Name')
    # last_name = fields.Char('Last Nmae')
    # email = fields.models.EmailField(max_length=254)
    # phone_number = fields.models.PhoneNumberField()
    # country = fields.Char('Country')
    # job_level = fields.Char('Job Level')
    # job_function = fields.Char("Job Function")
    # product_cloud_intrest = fields.Char()
    # is_this_an_RFP = fields.Boolean()
    # CHOICES = (
    #     (1,'YES'),
    #     (2,'NO'),
    #     (3,'Just Exploring')
    # )
    # budget_project = fields.Selection()



