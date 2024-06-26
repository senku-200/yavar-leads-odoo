from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home as HomeOriginal

class Home(HomeOriginal):

    def _login_redirect(self, uid, redirect=None):
        """ Redirect after login. """
        if not redirect:
            redirect = '/'

        return super(Home, self)._login_redirect(uid, redirect)
