from odoo import models, fields, api

class Buku(models.Model):
    _name = 'ramadhaniperpuslib.buku'

    name = fields.Char('Name', required=True)
    total = fields.Float('Total')
    description = fields.Text('Description')

    transaksi_ids = fields.One2many('ramadhaniperpuslib.transaksi', 'buku_id', string='Transaksi')

    available_book = fields.Float(compute='_compute_available_book', string='Available Book', store=True)

    @api.depends('total', 'transaksi_ids.state')
    def _compute_available_book(self):
        for rec in self:
            transaksi_progress = rec.transaksi_ids.filtered(lambda t: t.state == 'progress')
            rec.available_book = rec.total - len(transaksi_progress)
