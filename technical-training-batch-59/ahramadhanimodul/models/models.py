# from odoo import models, fields, api


# class ahramadhanimodul(models.Model):
#     _name = 'ahramadhanimodul.ahramadhanimodul'
#     _description = 'ahramadhanimodul.ahramadhanimodul'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

