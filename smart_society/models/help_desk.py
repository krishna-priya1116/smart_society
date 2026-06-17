from odoo import api,fields,models
from odoo.exceptions import UserError, ValidationError


class Helpdesk(models.Model):
    _name = 'help.desk'
    _description = 'Help desk'

    name=fields.Char(string='Name',required=True)
    tower_id=fields.Many2one('society.tower',string='Tower',required=True)
    complaint_ids=fields.One2many('complaint.desk','help_desk_id',string='Complaints')
    notice_ids=fields.Many2many('notice.board',string='Notices')


from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Complaint(models.Model):
    _name = 'complaint.desk'
    _description = 'Complaint desk'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Complaint', required=True)
    tower_id = fields.Many2one(related='flat_id.tower_id', string='Tower', required=True)
    flat_id = fields.Many2one(related='resident_id.flat_id', string='Flat', required=True)
    resident_id = fields.Many2one('resident.registrations', string='Resident')
    description = fields.Char(string='Description', required=True)
    create_date = fields.Datetime(string='Create Date', default=fields.Date.today())
    to_committee = fields.Many2one('society.committee')
    help_desk_id = fields.Many2one('help.desk', string='Helpdesk')
    user_id = fields.Many2one('res.users', string='Resident', default=lambda self: self.env.user)
    # committee_emails = fields.Char(string='Committee Emails', compute='_compute_committee_emails')
    committee_emails = fields.Char(string='Committee Emails')
    proof = fields.Binary(string='Proof Photo/video')

    stage = fields.Selection([
        ('draft',      'Draft'),
        ('send',       'Sent'),
        ('on_process', 'On Process'),
        ('hold',       'Hold'),
        ('resolve',    'Resolved'),
        ('reject',     'Rejected'),
    ], string='Stage', default='draft', tracking=True)


    def action_send(self):
        for record in self:
            # if record.stage in ('draft',):
            #     raise ValidationError("Only a Draft complaint can be sent.")
            record.stage = 'send'
            record._send_complaint_email()

    def action_process(self):
        for record in self:
            if record.stage not in ('send', 'hold'):
                raise ValidationError("Complaint must be Sent or On Hold to move to On Process.")
            record.stage = 'on_process'

    def action_hold(self):
        for record in self:
            if record.stage not in ('send', 'on_process'):
                raise ValidationError("Complaint must be Sent or On Process to put on Hold.")
            record.stage = 'hold'

    def action_resolve(self):
        for record in self:
            if record.stage not in ('on_process', 'hold'):
                raise ValidationError("Complaint must be On Process or Hold to mark as Resolved.")
            record.stage = 'resolve'

    def action_reject(self):
        for record in self:
            if record.stage in ('resolve', 'reject'):
                raise ValidationError("Cannot reject an already Resolved or Rejected complaint.")
            record.stage = 'reject'

    def action_reset_draft(self):
        for record in self:
            if record.stage not in ('reject', 'hold'):
                raise ValidationError("Only Rejected or Hold complaints can be reset to Draft.")
            record.stage = 'draft'


    def _send_complaint_email(self):
        template = self.env.ref(
            'smart_society.complaint_email_template_smart_society',
            raise_if_not_found=False
        )
        if not template:
            raise UserError("Mail template not found. Please check the template.")
        self.message_post_with_source(
            template,
            email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
            subtype_xmlid='mail.mt_comment',
        )


    @api.onchange('resident_id')
    def help_desk_id_check(self):
        for record in self:
            help_desk = self.env['help.desk'].search([
                ('tower_id', '=', record.tower_id.id),
            ], limit=1)
            if not record.help_desk_id:
                record.help_desk_id = help_desk

    @api.depends('to_committee')
    def _compute_committee_emails(self):
        for record in self:
            emails = []
            for partner in record.to_committee.committee_name_id:
                if partner.email:
                    emails.append(partner.email)
            if record.to_committee.chairman_id.email:
                emails.append(record.to_committee.chairman_id.email)
            if record.to_committee.secretary_id.email:
                emails.append(record.to_committee.secretary_id.email)
            record.committee_emails = ",".join(set(emails))

class NoticeBoard(models.Model):
    _name = 'notice.board'
    _description = 'Notice Board'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(string='Notice topic',required=True)
    # tower_id=fields.Many2many('society.tower', 'tower_desk_id','tower_id','help_desk_id',string='Tower', required=True)
    tower_id=fields.Many2many('society.tower',string='Tower', required=True)
    create_date = fields.Datetime(string='Create Date', default=fields.Datetime.now)
    description = fields.Char(string='Description',required=True)
    help_desk_id = fields.Many2many('help.desk', string='Helpdesk')
    notice_emails = fields.Char(
        string='Notice Emails',
        compute='_compute_notice_emails')
    stage = fields.Selection([
        ('send', 'Send'),('cancel','Cancel'),('draft','Draft')
    ])


    def send_notice(self):
        print('\n\n\n..........send_notice.....')
        template=self.env.ref(
            'smart_society.notice_email_template_smart_society',
             raise_if_not_found=False
        )
        if not template:
            raise UserError("Mail Template not found. Please check the template.")
        for record in self:
            print('\n\n\n.....send_notice...record.....',record)
            record.stage = 'send'
            record.message_post_with_source(
                template,
                email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
                subtype_xmlid='mail.mt_comment',
            )

    def draft_notice(self):
        for record in self:
            if record.stage == 'send' and record.stage=='draft':
                record.stage='draft'

    def cancel_notice(self):
        for record in self:
            if record.stage == 'send':
                raise ValidationError("The complaint is already send, can't cancel")
            record.stage = 'draft'

    @api.onchange('tower_id')
    def check_tower_id(self):
        for record in self:
            helpdesk=self.env['help.desk'].search([
                ('tower_id','in',record.tower_id.ids)
            ])
            print('\n\n\n.......check_tower_id....help.......',helpdesk)
            record.help_desk_id=helpdesk.ids

            print('\n\n\n.......record.help_desk_id......',record.help_desk_id)

    @api.depends('tower_id')
    def _compute_notice_emails(self):
        # notices = super().create(val_list),val_list
        print('......................._compute_notice_emails...................')
        for record in self:
            emails=[]
            if record.tower_id:
                residents=self.env['resident.registrations'].search([
                    # ('tower_id','=',record.tower_id.id),
                    ('tower_id', 'in', record.tower_id.ids),
                ])
                print('\n\n\n\n.......residents.....',residents)
                for res in residents:
                    print('\n\n\n.........res.......',res)
                    if res.email:
                        print('.............res.email......',res.email)
                        emails.append(res.email)
                    # print('\n\n\n..........residents.email.....',residents.email)


                # print('\n\n\n.........residents........',residents)
                # print('.........residents........',residents.partner_id.name)
                emails = list(set(emails))
                record.notice_emails = ",".join(emails)

class SocietyEvent(models.Model):
    _name='event.announcement'
    _description='Event Announcement'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char(string='Event Name',required=True)
    description=fields.Char(string='Description',required=True)
    # event_date=fields.Datetime(string='Event Date',required=True)
    event_time_start=fields.Datetime(string='Event Start Date Time',required=True)
    event_time_end=fields.Datetime(string='Event End Date Time',required=True)
    event_place=fields.Char(string='Event Place',required=True)
    tower_id=fields.Many2many('society.tower', 'tower_event_rel','event_id','tower_id',string='Tower',required=True)
    society_id=fields.Many2one(related='tower_id.society_id', string='Society')
    stage = fields.Selection([
        ('send', 'Send'),('cancel','Cancel'),('draft','Draft')
    ])
    event_emails = fields.Char(
        string='Event Emails',
        compute='_compute_event_emails'
    )

    @api.depends('tower_id')
    def _compute_event_emails(self,val_list):
        events=super().create(val_list)
        for record in events:
            emails = []
            resident=self.env['resident.registrations'].search([
                # ('tower_id','=',record.tower_id.id),
                ('tower_id', 'in', record.tower_id.ids),
            ])
            for res in resident:
                if res.email:
                    emails.append(res.email)
                    print('\n\n\n............resident.email.......',res.email)
            print('\n\n\n.........residents........',resident)
            emails = list(set(emails))
            record.event_emails = ",".join(emails)

    def send_event(self):
        template=self.env.ref(
            'smart_society.event_email_template_smart_society',
            raise_if_not_found=False
        )
        if not template:
            raise UserError("Mail Template not found. Please check the template.")
        for record in self:
            record.stage='send'
            record.message_post_with_source(
                template,
                email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
                subtype_xmlid='mail.mt_comment',
            )

    def draft_event(self):
        for record in self:
            if record.stage == 'send' and record.stage=='draft':
                record.stage='draft'

    def cancel_event(self):
        for record in self:
            if record.stage == 'send':
                raise ValidationError("The complaint is already send, can't cancel")
            record.stage = 'draft'



    # @api.onchange('tower_id')
    # def _check_tower_id(self):
    #     for record in self:
    #
    #         list_tower=[]
    #         if record.tower_id:
    #             print('\n\n\n......record.tower_id.....',record.tower_id)
    #             if len(record.tower_id)>1:
    #                 list_tower.append(record.tower_id)
    #         print('\n\n\n......record.tower_id.....',list_tower)
    # #




    # @api.constrains('tower_id')
    # def _check_tower_id(self):
    #     for record in self:
    #         list1=[]
    #         if record.tower_id:
    #             print('\n\n\nrecord.tower_id.....................',record.tower_id)
    #         help_desk_id=self.env['help.desk'].search([
    #             ('tower_id','=',record.tower_id.id),
    #         ])
    #         print('.........help_desk_id.....................',help_desk_id)
    #
    #         list1.append(help_desk_id)
    #         print('\n\n\n.........list1............',list1)
    #         for i in list1:
    #             record.write({
    #                 'help_desk_id':i,
    #             })
    #         print('\n\n\n.......record.help_desk_id.....',record.help_desk_id)




            # , limit = 1
            # record.help_desk_id=record.help_desk_id.mapped(list1)
            # if not help_desk_id:
            #     print('')
            # record.help_desk_id.mapped('help_desk_id')




# class Complaint(models.Model):
#     _name = 'complaint.desk'
#     _description = 'Complaint desk'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name = fields.Char(string='Complaint', required=True)
#     tower_id = fields.Many2one(related='flat_id.tower_id', string='Tower', required=True)
#     # tower_id = fields.Many2one('society.tower', string='Tower', required=True)
#     # flat_id = fields.Many2one('society.flat', string='Flat', required=True)
#     flat_id = fields.Many2one(related='resident_id.flat_id', string='Flat', required=True)
#     resident_id = fields.Many2one('resident.registrations', string='Resident')
#     description = fields.Char(string='Description', required=True)
#     create_date=fields.Datetime(string='Create Date',default=fields.Date.today())
#     to_committee = fields.Many2one('society.committee')
#     help_desk_id = fields.Many2one('help.desk', string='Helpdesk')
#     user_id = fields.Many2one('res.users',string='Resident',default=lambda self: self.env.user)
#     committee_emails = fields.Char( string='Committee Emails',compute='_compute_committee_emails')
#     stage = fields.Selection([
#         ('draft', 'Draft'),
#         ('send', 'Sent'),
#         ('on_process', 'On Process'),
#         ('hold', 'Hold'),
#         ('resolve', 'Resolved'),
#         ('reject', 'Rejected'),
#     ], string='Stage', default='draft', tracking=True)
#     proof = fields.Binary(string='Proof Photo/video')
#
#     def draft_complaint(self):
#         for record in self:
#             if record.stage=='send' or record.stage=='cancel':
#                 record.stage = 'draft'
#
#     def cancel_complaint(self):
#         for record in self:
#             if record.stage == 'send':
#                 raise ValidationError("The complaint is already send, can't cancel")
#             record.stage = 'cancel'
#
#     @api.onchange('resident_id')
#     def help_desk_id_check(self):
#         for record in self:
#             help_desk_id=self.env['help.desk'].search([
#                 ('tower_id','=',record.tower_id.id),
#             ],limit=1)
#             print('\n\n\n\n.............................help_desk_id.......',help_desk_id)
#             if not record.help_desk_id:
#                 record.help_desk_id = help_desk_id
#
#     @api.depends('to_committee')
#     def _compute_committee_emails(self):
#         for record in self:
#             emails = []
#             for partner in record.to_committee.committee_name_id:
#                 if partner.email:
#                     emails.append(partner.email)
#
#             if record.to_committee.chairman_id.email:
#                 emails.append(record.to_committee.chairman_id.email)
#
#             if record.to_committee.secretary_id.email:
#                 emails.append(record.to_committee.secretary_id.email)
#
#             emails = list(set(emails))
#             record.committee_emails = ",".join(emails)
#
#     def send_complaint(self):
#         template = self.env.ref(
#             'smart_society.complaint_email_template_smart_society',
#             raise_if_not_found=False
#         )
#         if not template:
#             raise UserError("Mail Template not found. Please check the template.")
#         for record in self:
#             record.stage = 'send'
#             # This sends the email AND logs it in the chatter
#             record.message_post_with_source(
#                 template,
#                 email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
#                 subtype_xmlid='mail.mt_comment',
#             )





