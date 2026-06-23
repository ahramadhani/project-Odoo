from odoo import models, fields, api, _

class Transaksi(models.Model):
    _name = 'ramadhaniperpuslib.transaksi'

    name = fields.Char('Name', default='New', readonly=True)

    tanggal_pinjam = fields.Date('Tanggal Pinjam')
    tanggal_kembali = fields.Date('Tanggal Kembali')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Progress'),
        ('done', 'Done'),
    ], string='State', default='draft')

    buku_id = fields.Many2one('ramadhaniperpuslib.buku', string='Buku', domain="[('available_book', '>', 0)]")
    description = fields.Text('Description')
    partner_id = fields.Many2one('res.partner', string='Peminjam')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('ramadhaniperpuslib.transaksi') or _('New')
        result = super(Transaksi, self).create(vals_list)
        return result

    def action_progress(self):
        self.write({
            'state': 'progress',
            'tanggal_pinjam': fields.Date.today(),
        })

    def action_done(self):
        self.write({
            'state': 'done',
            'tanggal_kembali': fields.Date.today(),
        })

    def action_draft(self):
        self.state = 'draft'