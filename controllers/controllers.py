# -*- coding: utf-8 -*-
# from odoo import http


# class Quintofly(http.Controller):
#     @http.route('/quintofly/quintofly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quintofly/quintofly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quintofly.listing', {
#             'root': '/quintofly/quintofly',
#             'objects': http.request.env['quintofly.quintofly'].search([]),
#         })

#     @http.route('/quintofly/quintofly/objects/<model("quintofly.quintofly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quintofly.object', {
#             'object': obj
#         })
