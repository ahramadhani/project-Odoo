from odoo import models, fields

class TeacherLevel(models.Model):
    _name = 'ahramadhanimodul.teacher_level'
    
    name = fields.Char('Name')