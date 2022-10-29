# -*- coding: utf-8 -*-
# from odoo import http


# class CustomLogin(http.Controller):
#     @http.route('/custom_login/custom_login', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_login/custom_login/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_login.listing', {
#             'root': '/custom_login/custom_login',
#             'objects': http.request.env['custom_login.custom_login'].search([]),
#         })

#     @http.route('/custom_login/custom_login/objects/<model("custom_login.custom_login"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_login.object', {
#             'object': obj
#         })
