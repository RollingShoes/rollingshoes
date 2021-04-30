# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasInvoiceReport/(http.Controller):
#     @http.route('/mx_integritas_invoice_report//mx_integritas_invoice_report//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_invoice_report//mx_integritas_invoice_report//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_invoice_report/.listing', {
#             'root': '/mx_integritas_invoice_report//mx_integritas_invoice_report/',
#             'objects': http.request.env['mx_integritas_invoice_report/.mx_integritas_invoice_report/'].search([]),
#         })

#     @http.route('/mx_integritas_invoice_report//mx_integritas_invoice_report//objects/<model("mx_integritas_invoice_report/.mx_integritas_invoice_report/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_invoice_report/.object', {
#             'object': obj
#         })
