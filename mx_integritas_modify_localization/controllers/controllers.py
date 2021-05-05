# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasModifyLocalization/(http.Controller):
#     @http.route('/mx_integritas_modify_localization//mx_integritas_modify_localization//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_modify_localization//mx_integritas_modify_localization//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_modify_localization/.listing', {
#             'root': '/mx_integritas_modify_localization//mx_integritas_modify_localization/',
#             'objects': http.request.env['mx_integritas_modify_localization/.mx_integritas_modify_localization/'].search([]),
#         })

#     @http.route('/mx_integritas_modify_localization//mx_integritas_modify_localization//objects/<model("mx_integritas_modify_localization/.mx_integritas_modify_localization/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_modify_localization/.object', {
#             'object': obj
#         })
