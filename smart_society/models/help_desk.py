from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Helpdesk(models.Model):
    _name = 'help.desk'
    _description = 'Help desk'

    name=fields.Char(string='Name',required=True)
    tower_id=fields.Many2one('society.tower',string='Tower',required=True)
    complaint_ids=fields.One2many('complaint.desk','help_desk_id',string='Complaints')
    notice_ids=fields.Many2many('notice.board',string='Notices')


class Complaint(models.Model):
    _name = 'complaint.desk'
    _description = 'Complaint desk'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Complaint', required=True)
    resident_id = fields.Many2one('resident.registrations', string='Resident')
    flat_id = fields.Many2one(related='resident_id.flat_id', string='Flat', required=True)
    tower_id = fields.Many2one(related='flat_id.tower_id', string='Tower', required=True)
    description = fields.Char(string='Description', required=True)
    create_date = fields.Datetime(string='Create Date', default=fields.Date.today())
    block_committee_id = fields.Many2one('block.committee')
    tower_committee_id=fields.Many2one('tower.committee')
    society_committee_id=fields.Many2one('society.committee')
    help_desk_id = fields.Many2one('help.desk', string='Helpdesk')
    user_id = fields.Many2one('res.users', string='Resident', default=lambda self: self.env.user)
    # committee_emails = fields.Char(string='Committee Emails', compute='_compute_committee_emails')
    committee_emails = fields.Char(string='Committee Emails',compute='_compute_committee_emails')
    proof = fields.Binary(string='Proof Photo/video')
    stage = fields.Selection([
        ('draft',      'Draft'),
        ('send',       'Sent'),
        ('on_process', 'On Process'),
        ('hold',       'Hold'),
        ('resolve',    'Resolved'),
        ('reject',     'Rejected'),
        ('not_resolved_block','Move to Tower'),
        ('not_resolved_tower', 'Move to Committee'),
    ], string='Stage', default='draft', tracking=True)

    @api.constrains('stage')
    def action_committee_complaints(self):
        if self.env.user.has_group('smart_society.group_registration_tower_committee'):
            tower_committee = self.env['tower.committee'].search([
                ('tower_member_id', '=', self.env.user.id)
            ], limit=1)
            return {
                'type': 'ir.actions.act_window',
                'name': 'Tower Complaints',
                'res_model': 'complaint.desk',
                'view_mode': 'list,form',
                'domain': [
                    ('stage', '=', 'not_resolved_block'),
                    ('tower_id', '=', tower_committee.tower_id.id),
                ],
            }

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

    def action_not_resolved_block(self):
        for record in self:
            if record.stage in ('resolve','reject','on_process'):
                raise ValidationError('Cant Move the resolve or rejected Complaint.')
            record.stage='not_resolved_block'
            print('record.stage..........',record.stage)

            if record.stage=='not_resolved_block':
                tower_committee = self.env['tower.committee'].search([
                    ('tower_id', '=', record.tower_id.id),
                ], limit=1)
                if not record.tower_committee_id:
                    record.tower_committee_id = tower_committee

    def action_not_resolved_tower(self):
        for record in self:
            if record.stage in ('resolve','reject','on_process'):
                raise ValidationError('Cant Move the resolve or rejected Complaint.')
            record.stage='not_resolved_tower'
            print('record.stage..........',record.stage)

            if record.stage=='not_resolved_tower':
                society_committee=self.env['society.committee'].search([
                    ('society_id','=',record.tower_id.society_id.id)
                ])
                if not record.society_committee_id:
                    record.society_committee_id=society_committee

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

    @api.onchange('stage','resident_id','flat_id','tower_id')
    def help_desk_id_check(self):
        for record in self:
            help_desk = self.env['help.desk'].search([
                ('tower_id', '=', record.tower_id.id),
            ], limit=1)
            if not record.help_desk_id:
                record.help_desk_id = help_desk

            block_committee=self.env['block.committee'].search([
                ('tower_id','=',record.tower_id.id),
                ('block','=',record.tower_id.block),
            ],limit=1)
            print('\n\n\n............block_committee............')
            if not record.block_committee_id:
                print('\n\n.....before record.block_committee_id......',record.block_committee_id)
                record.block_committee_id=block_committee
                print('\n\n\n...after...record.block_committee_id...',record.block_committee_id)

            if record.stage=='not_resolved_block':
                tower_committee = self.env['tower.committee'].search([
                    ('tower_id', '=', record.tower_id.id),
                ], limit=1)
                if not record.tower_committee_id:
                    record.tower_committee_id = tower_committee

            if record.stage=='not_resolved_tower':
                society_committee=self.env['society.committee'].search([
                    ('society_id','=',record.tower_id.society_id.id)
                ])
                if not record.society_committee_id:
                    record.society_committee_id=society_committee

    @api.depends('stage','block_committee_id','tower_committee_id','society_committee_id')
    def _compute_committee_emails(self):
        for record in self:
            emails=[]
            if record.stage=='send':
                print('\n\n......it should go to block committee.........')
                if record.block_committee_id.block_member_id.email:
                    print('record.block_committee_id.block_member_id....................',record.block_committee_id.block_member_id)
                    emails.append(record.block_committee_id.block_member_id.email)

            elif record.stage=='not_resolved_block':
                print('\n\n........it should go to tower committee.....')
                if record.tower_committee_id.tower_member_id.email:
                    print('record.tower_committee_id.tower_member_id.email....................',record.tower_committee_id.tower_member_id.emaild)
                    emails.append(record.tower_committee_id.tower_member_id.email)

            # elif record.stage=='not_resolved_tower':

            elif record.stage == 'not_resolved_tower':
                print('\n\n\n.......it should go to society committee.......')
                members = record.society_committee_id.society_committee_members
                emails.extend(members.mapped('partner_id.email'))

            record.committee_emails = ",".join(
                filter(None, set(emails))
            )
            print('\n\n\n.......record.committee_emails...........',record.committee_emails)



    # def committee_wise_complaints(self):
    #     if self.env.user.has_group('smart_society.group_registration_tower_committee'):
    #         tower_committee = self.env['tower.committee'].search([
    #             ('tower_member_id', '=', self.env.user.id)
    #         ], limit=1)
    #
    #         complaints = self.env['complaint.desk'].search([
    #             ('stage', '=', 'not_resolved_block'),
    #             ('tower_id', '=', tower_committee.tower_id.id),
    #         ])
    #
    #         return complaints


    # def committee_wise_complaints(self):
    #     for record in self:
    #         if self.env.user.has_group('smart_society.group_registration_tower_committee'):
    #             complaints=self.env['complaint.desk'].search([
    #                 ('stage','=','not_resolved_block')
    #             ])
    #             return complaints



    # @api.depends('to_committee')
    # def _compute_committee_emails(self):
    #     for record in self:
    #         emails = []
    #         for partner in record.to_committee.committee_name_id:
    #             if partner.email:
    #                 emails.append(partner.email)
    #         if record.to_committee.chairman_id.email:
    #             emails.append(record.to_committee.chairman_id.email)
    #         if record.to_committee.secretary_id.email:
    #             emails.append(record.to_committee.secretary_id.email)
    #         record.committee_emails = ",".join(set(emails))

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








