from odoo import models, fields, api


class SocietyDashboard(models.Model):
    _name = 'society.dashboard'
    _description = 'Smart Society Dashboard'

    name = fields.Char(default='Dashboard')

    society_id=fields.Many2one('society.setup',string='Society')
    tower_id=fields.Many2one('society.tower',string='Tower')
    total_notices = fields.Integer(string='Total Notices',compute='_compute_dashboard_data')
    total_events = fields.Integer(string='Total Events',compute='_compute_dashboard_data')
    total_complaints = fields.Integer(string='Total Complaints',compute='_compute_dashboard_data')
    # total_visitors = fields.Integer(string='Total Visitors',compute='_compute_dashboard_data')
    user_ids = fields.Many2one('res.users' ,default=lambda self:self.env.user.id)
    notice_ids = fields.Many2many('notice.board',compute='_compute_dashboard_data')
    event_ids = fields.Many2many('event.announcement',compute='_compute_dashboard_data')
    complaint_ids = fields.Many2many('complaint.desk',compute='_compute_dashboard_data')
    alert_type = fields.Selection(selection=[('sos_alert', 'SOS Alert'), ('fire_alert', 'Fire Alert'),
            ('panic_alert', 'Panic Alert'),('emergency_alert', 'Emergency Alert'),
            ('emergency_broadcast','Emergency Broadcast')])


    def sos_alerts(self):
        print('\n\n\n............sos_alert.........')
        return {
            'name': 'SOS Alert',
            'type': 'ir.actions.act_window',
            'res_model': 'resident.alerts',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_alert_type': 'sos_alert',
                'default_name': 'SOS Alert',
            },
            'groups': [(4,self.env.ref('smart_society.group_registration_administration').id),
                        (4, self.env.ref('smart_society.group_registration_user').id),
                       (4, self.env.ref('smart_society.group_registration_committee').id),
                       (4, self.env.ref('smart_society.group_registration_security').id)],
        }

    def fire_alerts(self):
        # self.ensure_one()
        # for record in self:
        #     record.alert_type='fire_alert'
        return {
            'name': "Fire Alert",
            'type': 'ir.actions.act_window',
            'res_model': 'resident.alerts',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_alert_type': 'fire_alert',
                'default_name': 'Fire Alert',
            },
            'groups': [(4, self.env.ref('smart_society.group_registration_administration').id),
                       (4, self.env.ref('smart_society.group_registration_user').id),
                       (4, self.env.ref('smart_society.group_registration_committee').id),
                       (4, self.env.ref('smart_society.group_registration_security').id)],
        }
    def medical_panic_buttons(self):
        # self.ensure_one()
        # for record in self:
        #     record.alert_type='panic_alert'
        return {
            'name': "Panic Alert",
            'type': 'ir.actions.act_window',
            'res_model': 'resident.alerts',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_alert_type': 'panic_alert',
                'default_name': 'Panic Alert',
            },
            'groups': [(4, self.env.ref('smart_society.group_registration_administration').id),
                       (4, self.env.ref('smart_society.group_registration_user').id),
                       (4, self.env.ref('smart_society.group_registration_committee').id),
                       (4, self.env.ref('smart_society.group_registration_security').id)],
        }

    def emergency_broadcast(self):
        # self.ensure_one()
        # for record in self:
        #     record.alert_type='emergency_alert'
        return {
            'name': "Emergency Alert",
            'type': 'ir.actions.act_window',
            'res_model': 'emergency.broadcasts',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                # 'default_alert_type': 'emergency_alert',
                'default_name': 'Emergency Alert',
            },
            'groups': [(4, self.env.ref('smart_society.group_registration_administration').id),
                       (4, self.env.ref('smart_society.group_registration_user').id),
                       (4, self.env.ref('smart_society.group_registration_committee').id),
                       (4, self.env.ref('smart_society.group_registration_security').id)],
        }

    # (4, self.env.ref('smart_society.group_registration_user').id),
    # def _compute_counts(self):
    #     for rec in self:
    #         group_users=self.env.ref('smart_society.group_registration_user')
    #         print('\n\ngroup_users.............................',group_users)
    #         group_users1=self.env.ref('smart_society.group_registration_user').id
    #         print('\n\ngroup_users....................1.........',group_users1)
    #         group_users2=self.env.ref('smart_society.group_registration_committee').id
    #         print('\n\ngroup_users....................2.........',group_users2)
    #         group_users3=self.env.ref('smart_society.group_registration_security').id
    #         print('\n\ngroup_users....................3.........',group_users3)
    #
    #         get_group=self.env['res.users'].search([
    #             ('group_ids','in',[group_users.id])
    #         ])
    #         print('\n\n\n....get_group.....',get_group)
    #
    #         rec.total_notices = self.env['notice.board'].search_count([])
    #         rec.total_events = self.env['event.announcement'].search_count([])
    #         rec.total_complaints = self.env['complaint.desk'].search_count([])
    #         rec.total_visitors = self.env['visitor.registrations'].search_count([])
    #
    #         print('........rec.total_notices.............',rec.total_notices)
    #         print('.......rec.total_events............',rec.total_events)
    #         print('........rec.total_complaints.............',rec.total_complaints)
    #         print('........rec.total_visitors .............',rec.total_visitors )

    def _compute_dashboard_data(self):
        for record in self:
            record.total_notices = self.env['notice.board'].search_count([])
            record.total_events = self.env['event.announcement'].search_count([])
            # record.total_visitors = self.env['visitor.registrations'].search_count([])
            record.notice_ids = self.env['notice.board'].search([],order='create_date desc')
            record.event_ids = self.env['event.announcement'].search([],order='event_time_start asc')
            # Complaints
            if self.env.user.has_group('base.group_portal'):
                resident = self.env['resident.registrations'].search([
                    ('partner_id', '=', self.env.user.partner_id.id)
                ], limit=1)
                record.total_complaints = self.env['complaint.desk'].search_count([
                    ('resident_id', '=', resident.id)
                ])
                record.complaint_ids = self.env['complaint.desk'].search([
                    ('resident_id', '=', resident.id)
                ])
            else:
                record.complaint_ids = self.env['complaint.desk'].search([])
                record.total_complaints = self.env['complaint.desk'].search_count([])

            if self.env.user.has_group('smart_society.group_registration_committee') or self.env.user.has_group('smart_society.group_registration_security'):
                user=self.env.user
                print('\n\n\n..........user.tower_id',user.tower_id.id)
                # print('\n\n\n..........user.society_id')
                # print('\n\n\n..........user.tower_id')
                record.total_notices = self.env['notice.board'].search_count([('tower_id','=',user.tower_id.id)])
                record.total_events = self.env['event.announcement'].search_count([('tower_id','=',user.tower_id.id)])
                # record.total_visitors = self.env['visitor.registrations'].search_count([('tower_id','=',record.tower_id)])
                record.notice_ids = self.env['notice.board'].search([('tower_id','=',user.tower_id.id)], order='create_date desc')
                record.event_ids = self.env['event.announcement'].search([('tower_id','=',user.tower_id.id)], order='event_time_start asc')

            if self.env.user.has_group('smart_society.group_registration_administration'):
                record.total_notices = self.env['notice.board'].search_count([])
                record.total_events = self.env['event.announcement'].search_count([])
                # record.total_visitors = self.env['visitor.registrations'].search_count([('tower_id','=',record.tower_id)])
                record.notice_ids = self.env['notice.board'].search([],
                                                                    order='create_date desc')
                record.event_ids = self.env['event.announcement'].search([],
                                                                         order='event_time_start asc')

    def action_open_notice(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Notices',
            'res_model': 'notice.board',
            'view_mode': 'list,form',
        }

    def action_open_events(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Events',
            'res_model': 'event.announcement',
            'view_mode': 'list,form',
        }

    def action_open_complaints(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Complaints',
            'res_model': 'complaint.desk',
            'view_mode': 'list,form',
        }

    def action_open_visitors(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Visitors',
            'res_model': 'visitor.registrations',
            'view_mode': 'list,form',
    }


# class SocietyAlerts(models.Model):
#     _name = 'society.alert.save'
#     _description='Society Alert Save'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name=fields.Char(string='Alert Name',required=True)
#     description=fields.Text(string='Alert Description')
#     flat_id=fields.Many2one('society.flat',string='Flat',required=True)
#     tower_id=fields.Many2one(related='flat_id.tower_id',string='Tower')
#     user_id=fields.Many2one('res.users',string='resident',default=lambda self: self.env.user)
#     location=fields.Char(string='Location',required=True)
#     alert_type=fields.Selection(required=True,selection=[('sos_alert','SOS Alert'),('fire_alert','Fire Alert'),
#     ('panic_alert','Panic Alert'),('emergency_alert','Emergency Alert')])
#     datetime=fields.Datetime(string='Date and Time',default=fields.Datetime.now)
#     to_committee = fields.Many2one('society.committee', required=True)
#     committee_emails=fields.Char(string='Committee Emails')

# class EmergencyBroadcast(models.TransientModel):
#     _name='emergency.broadcast.save'
#     _description='Emergency Broadcast Save'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name=fields.Char(string='Emergency Broadcast')
#     description=fields.Text(string='Emergency Broadcast')
#     tower_ids=fields.Many2many('society.tower',string='Tower')
#     flat_ids=fields.Many2many('society.flat',string='Flat')
#     datetime=fields.Datetime(string='Date and Time',default=fields.Datetime.now)
#     resident_emails = fields.Char(compute='_compute_resident_email')
#
#
#
#
#     # def sos_alert(self):
#     #     self.ensure_one()
#     #     for record in self:
#     #         record.alert_type='sos_alert'
#     #         # record.alert_id.alert_type='sos_alert'
#     #     return {
#     #         'name': "SOS Alert",
#     #         'type': 'ir.actions.act_window',
#     #         'res_model': 'society.alert',
#     #         'view_mode': 'form',
#     #         'target': 'new',
#     #         'alert_type':'sos_alert',
#     #
#     #     }
#
#     # alert_id=fields.Many2one('society.alert')
#
#     # tower_id=fields.Many2one(related='flat_id.tower_id')
#     # tower_ids=fields.Many2many('society.tower')
#     # flat_id=fields.Many2one('society.flat')