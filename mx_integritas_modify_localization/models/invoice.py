# -*- coding: utf-8 -*-

from odoo import models, fields, api
class AccountMove(models.Model):
    _inherit = ['account.move']

    l10n_mx_edi_cfdi_uuid = fields.Char(string='Fiscal Folio', copy=False, readonly=False,
        help='Folio in electronic invoice, is returned by SAT when send to stamp.',
        compute='_compute_cfdi_values')