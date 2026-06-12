from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError


class MaintenanceBill(models.Model):
    _name = 'maintenance.bill'
    _description = 'Maintenance Bill Template'

    name = fields.Char(required=True)
    tower_id = fields.Many2one('society.tower',string='Tower',required=True)
    maintenance_amount = fields.Float(string='Maintenance Amount',required=True)
    penalty_per_day = fields.Float(string='Penalty Per Day',required=True)
    due_day = fields.Integer(string='Due Day',default=10,required=True)
    maintenance_ids = fields.One2many('society.maintenance','maintenance_bill_id')
    invoice_id = fields.Many2one('account.move')

    def generate_monthly_bills(self):
        print('\n\n\n generate.........................................')
        today = fields.Date.today()
        print('today................',today)
        for bill in self:
            print("bill...............", bill)
            print("tower..............", bill.tower_id)
            print("tower_id...........", bill.tower_id.id)
            flats = self.env['society.flat'].search([
                ('tower_id', '=', bill.tower_id.id),
                ('flat_status','=','occupied')
            ])
            print('flats..........',flats)
            due_date = today.replace(day=bill.due_day)
            for flat  in flats:
                print('\n\n................flats........', flat )
                existing = self.env['society.maintenance'].search([
                    ('flat_id', '=', flat.id),
                    ('month', '=', today.month),
                    ('year', '=', today.year)
                ], limit=1)
                print('\n\n\n........existing...........',existing)
                resident = self.env['resident.registrations'].search([
                    ('flat_id', '=', flat.id)
                ])
                print('\n\n\n............resident.......',resident)
                # user = False
                # if resident and resident.email:
                #     user = self.env['res.users'].search([
                #         ('login', '=', resident.email)
                #     ], limit=1)
                if not existing:
                    print('\n\n.......if not exist.......')
                    self.env['society.maintenance'].create({
                        'flat_id': flat.id,
                        'maintenance_bill_id': bill.id,
                        'due_date': due_date,
                        'month': today.month,
                        'year': today.year,
                        # 'user_id':user.id,
                        'resident_id':resident.ids,
                        # 'invoice_id':invoice.id,
                    })








class SocietyMaintenance(models.Model):
    _name = 'society.maintenance'
    _description = 'Society Maintenance'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    maintenance_bill_id = fields.Many2one('maintenance.bill',required=True)
    flat_id = fields.Many2one('society.flat',string='Flat',required=True)
    resident_id = fields.Many2many('resident.registrations',string='Residents',compute='_compute_resident_id',store=True)
    tower_id = fields.Many2one(related='flat_id.tower_id',store=True)
    due_date = fields.Date(string='Due Date')
    month = fields.Integer(string='Month')
    year = fields.Integer(string='Year')
    maintenance_amount = fields.Float(related='maintenance_bill_id.maintenance_amount',store=True)
    penalty_per_day = fields.Float(related='maintenance_bill_id.penalty_per_day',store=True)
    penalty_amount = fields.Float(compute='_compute_penalty',store=True)
    total_amount = fields.Float(compute='_compute_total',store=True)
    is_paid = fields.Boolean(default=False)
    state = fields.Selection([('unpaid', 'Unpaid'),('paid', 'Paid')], default='unpaid')
    payment_date = fields.Date(string='Payment Date')
    user_id = fields.Many2one('res.users',string='Resident User',store=True)
    resident_emails = fields.Char(compute='_compute_resident_email')
    invoice_id = fields.Many2one('account.move')


    @api.depends('flat_id')
    def _compute_resident_email(self):
        for record in self:
            emails=[]
            residents = self.env['resident.registrations'].search([
                ('flat_id', 'in', record.flat_id.id),
            ])
            for resident in residents:
                if resident.email:
                    emails.append(resident.email)
            record.resident_emails = ",".join(list(set(emails)))
            print('\n\n\n........record.resident_emails ...........',record.resident_emails )

    @api.depends('flat_id')
    def _compute_resident_id(self):
        for record in self:
            residents = self.env['resident.registrations'].search([
                ('flat_id', '=', record.flat_id.id)
            ])
            record.resident_id = residents

    @api.depends('due_date', 'penalty_per_day', 'is_paid')
    def _compute_penalty(self):
        today = fields.Date.today()

        for record in self:

            if record.is_paid:
                record.penalty_amount = 0
                continue

            if record.due_date and today > record.due_date:
                late_days = (today - record.due_date).days
                record.penalty_amount = (
                    late_days * record.penalty_per_day
                )
            else:
                record.penalty_amount = 0

    @api.depends('maintenance_amount', 'penalty_amount')
    def _compute_total(self):
        for record in self:
            record.total_amount = (
                record.maintenance_amount +
                record.penalty_amount
            )

    def action_mark_paid(self):
        self.write({
            'is_paid': True,
            'payment_date': fields.Date.today(),
            'state': 'paid'
        })

    def maintenance_email(self):
        print('\n\n\n..........maintenance_email.....')
        template=self.env.ref(
            'smart_society.maintenance_email_template_smart_society',
            raise_if_not_found=False
        )
        if not template:
            raise UserError("Mail Template not found. Please check the template.")
        for record in self:
            print('\n\n\n..........send_maintenance...record.....',record)
            record.message_post_with_source(
                template,
                email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
                subtype_xmlid='mail.mt_comment',
            )










        # else:
        #     residents=self.env['resident.registrations'].search([
        #         ('flat_id','in',record.flat_ids.ids)
        #     ])
        #     for resident in residents:
        #         print('\n\n\n...........resident....',resident)
        #         if resident.email:
        #             emails.append(resident.email)


# class SocietyMaintenance(models.Model):
#     _name = 'society.maintenance'
#     _description = 'Society Maintenance'
#
#     maintenance_bill_id = fields.Many2one('maintenance.bill',required=True)
#     flat_id = fields.Many2one('society.flat',string='Flat',required=True)
#     resident_id = fields.Many2many(related='flat_id.resident_id',string='Resident')
#     tower_id = fields.Many2one(related='flat_id.tower_id',store=True)
#     # user_id = fields.Many2one('res.users',string='Resident',default=lambda self: self.env.user)
#     due_date = fields.Date(string='Due Date')
#     month = fields.Integer(string='month')
#     year = fields.Integer(string='year')
#     maintenance_amount = fields.Float(related='maintenance_bill_id.maintenance_amount',store=True)
#     penalty_per_day = fields.Float(related='maintenance_bill_id.penalty_per_day',store=True)
#     penalty_amount = fields.Float(compute='_compute_penalty',store=True)
#     total_amount = fields.Float(compute='_compute_total',store=True)
#     is_paid = fields.Boolean(default=False)
#     state = fields.Selection([('unpaid', 'Unpaid'),('paid', 'Paid')], default='unpaid', string='Status')
#     payment_date = fields.Date(string='Payment Date')
#     user_id=fields.Many2one('res.users',string='Resident')
#
#     # , compute = "_compute_user_id"
#     @api.depends('resident_id')
#     def _compute_user_id(self):
#         for record in self:
#             search_resident=self.env['resident.registrations'].search([
#                 ('flat_id', '=', record.flat_id.id),
#                 ('email','=',)
#             ])
#             # for resident in search_resident:
#             #     self.env['res.users'].search([
#             #         ('partner_id', '=', record.partner_id.id),
#             #     ])
#
#             print('\n\n\nsearch_resident...................',search_resident)
#
#     @api.constrains('due_date','penalty_per_day','is_paid')
#     def compute_penalty(self):
#         today = fields.Date.today()
#         for record in self:
#             if record.is_paid:
#                 record.penalty_amount = 0
#                 continue
#             if record.due_date and today > record.due_date:
#                 late_days = (today - record.due_date).days
#                 record.penalty_amount = (late_days *record.penalty_per_day)
#             else:
#                 record.penalty_amount = 0
#
#     @api.depends('maintenance_amount','penalty_amount')
#     def _compute_total(self):
#         for record in self:
#             record.total_amount = (record.maintenance_amount +record.penalty_amount
#             )
#
#     def action_mark_paid(self):
#         self.write({
#             'is_paid': True,
#             'payment_date': fields.Date.today(),
#             'state':'paid'
#         })
#
#     @api.depends('flat_id')
#     def _compute_resident_id(self):
#         for record in self:
#             residents=self.env['resident.registrations'].search([
#                 ('flat_id', '=', record.flat_id.id),
#             ])
#             print('residents..........',residents)
#             print('residents.id........',residents.id)
#             record.resident_id = residents
#             print('\n\n\n......record.resident_id',record.resident_id)






# class SocietyMaintenance(models.Model):
#     _name='society.maintenance'
#     _description='Society Maintenance'
#
#     # user_id=fields.Many2one('resident.registrations',string='Resident')
#     # user_id = fields.Many2one('res.users', string='Resident', default=lambda self: self.env.user),default=lambda self: self.env.partner_id
#     # , default = lambda self: self.env.user
#     resident_id=fields.Many2one('resident.registrations',string='Resident',default=lambda self:self.env.user)
#     user_id=fields.Many2one('res.users',string='User',compute='_compute_user_id')
#     # user_id=fields.Many2one('res.users',domain=['user_id','=',resident_id.user_id.id],string='User')
#     bill_amount=fields.Float(compute='_compute_amount',string='Bill Amount')
#     maintenance_bill_id=fields.Many2one('maintenance.bill')
#     maintenance_bill=fields.Float(related='maintenance_bill_id.maintenance_bill')
#     tower_id=fields.Many2one(related='resident_id.tower_id',string='Tower')
#     penalty=fields.Float(related='maintenance_bill_id.penalty',string='Penalty/per day')
#     select_date_to_pay=fields.Datetime(related='maintenance_bill_id.select_date_to_pay',string='Due Date to pay')
#     due_date=fields.Datetime(string='Due Date')
#     today=fields.Datetime(string='Today',default=fields.Date.today())
#     is_paid=fields.Boolean(string='Is Paid',default=False)
#
#     @api.depends('today','select_date_to_pay')
#     def _compute_amount(self):
#         for record in self:
#             if record.select_date_to_pay<=record.due_date:
#                 record.bill_amount=record.maintenance_bill
#
#             if record.select_date_to_pay > record.due_date:
#                 record.bill_amount+=record.penalty
#
#     @api.depends('resident_id')
#     def compute_user_id(self):
#         for record in self:
#             if record.resident_id:
#                 record.user_id=self.env['res.users'].search([
#                     ('user_id','=',record.resident_id.id),
#                 ],limit=1)


# class MaintenanceBill(models.Model):
#     _name='maintenance.bill'
#     _description='Maintenance Bill'
#
#     maintenance_bill=fields.Float(string='Maintenance Bill',require=True)
#     penalty=fields.Float(string='Penalty/per day',require=True)
#     select_date_to_pay=fields.Datetime(string='Select Date',required=True)
#     tower_id=fields.Many2one('society.tower')
#     society_maintenance_ids=fields.One2many('society.maintenance','maintenance_bill_id')
#
#
#     def generate_maintenance_bill(self):
#         for record in self:
#             list_users=[]
#             bill_exist=self.env['society.maintenance'].search([
#                 ('tower_id','=',record.tower_id),
#                 ('maintenance_bill_id','=',record.id),
#             ],limit=1)
#             print('\n\n\n................bill_exist',bill_exist)
#             if not bill_exist:
#                 users=self.env['resident.registrations'].search([
#                     ('tower_id','=',record.tower_id)
#                 ])
#                 for user in users:
#                     res_users=self.env['res.users'].search([
#                         'user_id','=',user.partner_id
#                     ])
#                     list_users.append(res_users)
#
#                 for user in list_users:
#                     print('\n\n\n..............',user)
#                     self.env['society.maintenance'].create({
#                         'user_id':user.id,
#                         'maintenance_bill':record.maintenance_bill,
#                         'penalty':record.penalty,
#                         'select_date_to_pay':record.select_date_to_pay,
#                     })
#             print('\n\n\n.......list_users.',list_users)





