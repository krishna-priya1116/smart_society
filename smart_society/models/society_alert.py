from odoo import fields,models,api
from odoo.exceptions import UserError


class ResidentAlerts(models.Model):
    _name = 'resident.alerts'
    _description='Resident Alert'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    alert_from=fields.Many2one('res.users',string='Alert From',default=lambda self:self.env.user)
    name=fields.Char(string='Alert Name')
    description=fields.Text(string='Alert Description')
    flat_id=fields.Many2many('society.flat',string='Flat',required=True)
    tower_id=fields.Many2many('society.tower',string='Tower')
    user_id=fields.Many2one('res.users',string='resident',default=lambda self: self.env.user)
    location=fields.Char(string='Location',required=True)
    alert_type=fields.Selection(selection=[('sos_alert','SOS Alert'),('fire_alert','Fire Alert'),
    ('panic_alert','Panic Alert'),('emergency_alert','Emergency Alert')])
    security_id=fields.Many2many('security.guard',string='Security')
    resident_id=fields.Many2many('resident.registrations',string='Resident')
    create_date=fields.Datetime(string='Date and Time',default=fields.Datetime.now)
    society_committee_id = fields.Many2one('society.committee')
    tower_committee_id = fields.Many2one('tower.committee')
    block_committee_id=fields.Many2one('block.committee')
    committee_emails = fields.Char(string='Committee Emails',compute='_compute_committee_emails')
    # committee_emails = fields.Char(string='Committee Emails')
    flat_id_save=fields.Char(compute='_compute_flat_id_save')


    @api.depends('user_id')
    def _compute_committee_emails(self):
        for record in self:
            emails=[]
            resident=self.env['resident.registrations'].search([
                ('user_id','=',record.user_id.id)
            ])
            print('resident.........',resident)
            print('resident flat_id.........',resident.flat_id)
            print('resident.........',resident.tower_id)
            print('resident.........',resident.tower_id.block)

            block_committee = self.env['block.committee'].search([
                ('tower_id', '=', record.tower_id.id),
                ('block', '=', resident.tower_id.block),
            ], limit=1)
            print('block,................',block_committee)
            if block_committee.block_member_id.email:
                print('block_committee.block_committee_id.email....................',block_committee.block_committee_id.email)
                emails.append(block_committee.block_member_id.email)

            tower_committee=self.env['tower.committee'].search([
                ('tower_id','=',resident.tower_id.id)
            ])
            print('tower committee..............',tower_committee)
            if tower_committee.tower_member_id.email:
                print('block_committee.block_committee_id.email....................',tower_committee.tower_member_id.email)
                emails.append(tower_committee.tower_member_id.email)

            society_committee=self.env['society.committee'].search([
                ('society_id','=',resident.tower_id.society_id.id)
            ])
            print('society_committee..................', society_committee)
            members = record.society_committee_id.society_committee_members
            emails.extend(members.mapped('partner_id.email'))
            print('society_id.....emails..............',emails)

            record.committee_emails = ",".join(emails)

    @api.onchange('alert_from')
    def assign_to_send(self):
        for record in self:

            search_user = self.env['resident.registrations'].search([
                ('user_id', '=', record.alert_from.id)
            ], limit=1)

            if not search_user:
                continue

            block_committee = self.env['block.committee'].search([
                ('tower_id', '=', search_user.tower_id.id),
                ('block', '=', search_user.tower_id.block),
            ], limit=1)
            record.block_committee_id = block_committee

            tower_committee = self.env['tower.committee'].search([
                ('tower_id', '=', search_user.tower_id.id)
            ], limit=1)
            record.tower_committee_id = tower_committee

            society_committee = self.env['society.committee'].search([
                ('society_id', '=', search_user.tower_id.society_id.id)
            ], limit=1)
            record.society_committee_id = society_committee

            select_security = self.env['security.guard'].search([
                ('tower_id', '=', search_user.tower_id.id)
            ])
            record.security_id = select_security

    # @api.onchange('resident_id', 'flat_id', 'tower_id')
    # def assign_to_send(self):
    #     for record in self:
    #         search_user = self.env['resident.registrations'].search([
    #             ('user_id', '=', record.alert_from.id)
    #         ])
    #         block_committee=self.env['block.committee'].search([
    #             ('tower_id', '=', record.tower_id.id),
    #             ('block', '=', search_user.tower_id.block),
    #         ], limit=1)
    #         record.block_committee_id=block_committee
    #         tower_committee=self.env['tower.committee'].search([
    #             ('tower_id', '=', search_user.tower_id.id)
    #         ])
    #         record.tower_committee_id=tower_committee
    #         print('\n\n\n.............search_user....', search_user)
    #         society_committee=self.env['society.committee'].search([
    #             ('society_id','=',search_user.tower_id.society_id.id)
    #         ])
    #         print('society_committee..................', society_committee)
    #         members = record.society_committee_id.society_committee_members
    #         record.society_committee_id=members
    #         select_security = self.env['security.guard'].search([
    #             ('tower_id', '=', search_user.tower_id.id)
    #         ])
    #         record.security_id = select_security


    @api.depends('flat_id')
    def _compute_flat_id_save(self):
        for record in self:
            for flat in record.flat_id:
                print('\n\n\n.......flat.name.................',flat.name)



    def action_send_email(self):

        template = self.env.ref(
            'smart_society.alerts_emails_template_smart_society'
        )
        if not template:
            raise UserError("Mail Template not found. Please check the template.")
        print('\n\n\n.......before....save_to_model.')
        # self.save_to_model()
        print('\n\n\n.......save_to_model..........')
        for record in self:
            print('\n\n\n.....action_send_email...record.....',record)
            record.message_post_with_source(
                template,
                email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
                subtype_xmlid='mail.mt_comment',
            )


class EmergencyBroadcasts(models.Model):
    _name='emergency.broadcasts'
    _description='Emergency Broadcast'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(string='Name')
    description=fields.Text(string='Description')
    tower_ids=fields.Many2many('society.tower',string='Tower')
    flat_ids=fields.Many2many('society.flat',string='Flat')
    create_date=fields.Datetime(string='Date and Time',default=fields.Datetime.now)
    resident_emails = fields.Char(compute='_compute_resident_email')

    @api.depends('tower_ids','flat_ids')
    def _compute_resident_email(self):
        for record in self:
            emails=[]
            tower_flat_ids=[]
            if record.tower_ids:
                tower_flats=self.env['society.flat'].search([
                    ('tower_id', 'in', record.tower_ids.ids)

                ])
                tower_flat_ids.extend(tower_flats.ids)
                tower_flat_ids=list(set(tower_flat_ids))
                residents = self.env['resident.registrations'].search([
                    ('flat_id', 'in', tower_flat_ids),
                ])
                for resident in residents:
                    if resident.email:
                        emails.append(resident.email)
            else:
                residents=self.env['resident.registrations'].search([
                    ('flat_id','in',record.flat_ids.ids)
                ])
                for resident in residents:
                    print('\n\n\n...........resident....',resident)
                    if resident.email:
                        emails.append(resident.email)
            record.resident_emails = ",".join(list(set(emails)))

    def action_send_broadcast(self):
        template = self.env.ref(
            'smart_society.emergency_broadcasts_email_template'
        )
        if not template:
            raise UserError("Mail Template not found. Please check the template.")
        for record in self:
            print('\n\n\n.....action_send_email...record.....', record)
            record.message_post_with_source(
                template,
                email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
                subtype_xmlid='mail.mt_comment',
            )
