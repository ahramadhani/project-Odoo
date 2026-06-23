from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta

class Session(models.Model):
    _name = 'ahramadhanimodul.session'
    _inherit = ['mail.thread']
    
    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date', default=fields.Date.today())
    duration = fields.Integer('Duration')
    number_of_seats = fields.Integer('Number Of Seats')
    description = fields.Text('Description')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Progress'),
        ('done', 'Done'),
    ], string='State', default="draft", tracking=True)
    
    partner_id = fields.Many2one('res.partner', string='Instructor', domain="['|',('is_instructor','=',True),('teacher_level_id','!=',False)]")
    course_id = fields.Many2one('ahramadhanimodul.course', string='Course')
    
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')
    
    active = fields.Boolean('Active', default=True)
    
    session_code = fields.Char('Session Code', default='Unknown')
    
    @api.depends('partner_ids','number_of_seats')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.number_of_seats:
                rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
            else:
                rec.taken_seats = 0
    
    @api.model
    def create(self, vals):
        if vals[0].get('session_code', _('Unknown')) == _('Unknown'):
            # Checking
            # sequence = self.env['ir.sequence'].sudo().search([('code','=','khaikalacademy.session_code')])
            # today = fields.Date.context_today(self)
            # # Contoh anggap hari ini adalah besok
            # # today = today + timedelta(days=1)
            # if sequence.write_date:
            #     last_update = fields.Datetime.context_timestamp(self, sequence.write_date).date()
            #     # Rest if different date
            #     if last_update != today:
            #         sequence.sudo().write({
            #             'number_next_actual':1
            #         })
            vals[0]['session_code'] = self.env['ir.sequence'].next_by_code('khaikalacademy.session_code') or _('New')
        result = super(Session, self).create(vals)
        return result
    
    @api.onchange('number_of_seats','partner_ids')
    def _onchange_seats(self):
        if self.number_of_seats < 0 :
            return {
                'warning': {
                    'title': "Invalid Value",
                    'message': "Cannot input negatif number on seats",
                }
            }
        if len(self.partner_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': "Something Wrong",
                    'message': "Participants more then seats",
                }
            }
    
    @api.constrains('partner_id','partner_ids')
    def _constrains_instructor(self):
        for rec in self:
            if rec.partner_id in rec.partner_ids :
                raise ValidationError('Instructor cannot be attendees:{}'.format(rec.partner_id.name))
    
    def action_confirm(self):
        self.state = 'progress'
    
    def action_done(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'
        
    stop_date = fields.Date(compute='_compute_stop_date', string='stop_date', store=True)
    
    @api.depends('start_date','duration')
    def _compute_stop_date(self):
        for rec in self:
            if rec.start_date:
                rec.stop_date = rec.start_date + timedelta(days=rec.duration)
            else:
                rec.stop_date = False
    
    number_of_attendees = fields.Float(compute='_compute_number_of_attendees', string='Number Of Attendees', store=True)
    
    @api.depends('partner_ids')
    def _compute_number_of_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.partner_ids)
            
    def action_attendees_report_xlsx(self):
        # Memanggil action untuk mencetak laporan
        return {
            'type': 'ir.actions.act_url',
            'url': '/attendees/excel_report/%s' % (self.id),
            'target': 'new',
        }
        
    @api.model
    def _cron_notification_session_start(self):
        tomorrow = fields.Date.today() + timedelta(days=1)
        sessions = self.search([('start_date','=',tomorrow)])
        for rec in sessions:
            partners = rec.partner_id | rec.partner_ids
            partners = partners.filtered(lambda p: p.email)
            if not partners:
                    continue
            for p in partners:
                
                body_html = f"""
                    <p>Hallo {p.name}, </p>
                    <p>Session : {rec.name} pada course {rec.course_id.name} akan segera dimulai pada {rec.start_date}</p>
                    <p>Terimakasih</p>
                    
                """
                
                mail_values = {
                    'subject':"Reminder Session {}".format(rec.name),
                    'body_html':body_html,
                    'email_to':p.email,
                    'email_from': 'info@ahramadhani'
                }
                
                mail = self.env['mail.mail'].create(mail_values)
                mail.send()