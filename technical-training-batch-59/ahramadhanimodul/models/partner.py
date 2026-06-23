from odoo import models, fields

class InheritParter(models.Model):
    _inherit = 'res.partner'
    
    is_instructor = fields.Boolean('Instructor ?')
    session_ids = fields.Many2many('ahramadhanimodul.session', string='Sessions')
    teacher_level_id = fields.Many2one('ahramadhanimodul.teacher_level', string='Teacher Level')