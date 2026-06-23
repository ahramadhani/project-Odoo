from odoo import models, fields, api


class AddAttendees(models.TransientModel):
    _name = 'ahramadhanimodul.add_attendees'
    
    session_ids = fields.Many2many('ahramadhanimodul.session', string='Sessions')
    partner_ids = fields.Many2many('res.partner', string='partner')
    
    def confirm(self):
        self.session_ids.partner_ids |= self.partner_ids