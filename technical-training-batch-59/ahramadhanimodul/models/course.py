from odoo import models, fields

class Course(models.Model):
    _name = 'ahramadhanimodul.course'
    
    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    
    user_id = fields.Many2one('res.users', string='Responsible User')
    
    session_ids = fields.One2many('ahramadhanimodul.session', 'course_id', string='Sessions')
    
    _name_uniq = models.Constraint(
        "unique(name)",
        "Name must be unique",
    )
    
    _check_name_and_description = models.Constraint(
        "check(name != description)",
        "Name And Description must be different"
    )
    
    def copy(self, default=None):
        results = self.browse()  # untuk menyimpan hasil copy

        for rec in self:
            default_copy = dict(default or {})
            
            copied_count = self.search_count([
                ('name', '=like', "Copy of {}%".format(rec.name))
            ])

            if not copied_count:
                new_name = "Copy of {}".format(rec.name)
            else:
                new_name = "Copy of {} ({})".format(rec.name, copied_count)

            default_copy['name'] = new_name

            new_rec = super(Course, rec).copy(default_copy)
            results += new_rec

        return results