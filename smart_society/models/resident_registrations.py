from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, time
import re


class ResidentRegistrations(models.Model):
    _name='resident.registrations'
    _description='Resident Registrations'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # partner_id=fields.Many2one('res.users',required=True)
    partner_id=fields.Many2one('res.partner',required=True,string='Resident Name')
    name=fields.Char(related='partner_id.name',string='Resident Name')
    age=fields.Integer(string='Age')
    mobile_number=fields.Char(string='Mobile Number',related='partner_id.phone',readonly=False)
    email=fields.Char(string='Email',related='partner_id.email',readonly=False)
    flat_id=fields.Many2one('society.flat',string='Flat Number')
    tower_id=fields.Many2one(related="flat_id.tower_id",string='Tower')
    id_proof = fields.Binary(string="ID Proof Copy")
    emergency_contacts=fields.Char(string='Emergency Contacts',required=True)
    resident_type=fields.Selection(string='Resident Type',required=True,
                                   selection=[('owner','Owner'),('tenant','Tenant'),
                                   ('family_member','Family Member'),('temporary_resident','Temporary Resident'),
                                              ])
    has_vehicle=fields.Boolean(string='Has Vehicle',default=False)
    vehicle_count=fields.Integer(string='Vehicle Count')
    vehicle_ids=fields.One2many('vehicle.registrations','resident_id',string='Vehicle ID')
    real_owner=fields.Char(string='Real Owner')
    tenant_certificate=fields.Binary(string='Tenant Certificate')
    user_id = fields.Many2one( 'res.users',string='User',readonly=False)
    join_date=fields.Date(string='Join Date')
    leave_date=fields.Date(string='Leave Date')
    attendance_status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
    ], compute='_compute_attendance_status')

    worked_hours = fields.Float(compute='_compute_attendance_status')    # today = fields.Date.today()




    @api.constrains('resident_type')
    def have_real_owner(self):
        for record in self:
            if record.resident_type=='tenant' or record.resident_type=='temporary_resident':
                if not record.real_owner:
                    raise ValidationError('Need real owner')
            if record.resident_type=='tenant':
                if not record.tenant_certificate:
                    ValidationError('Tenant Certificate needed')
                # self.env['resident.documents.storage'].create({
                #     'resident_id':record.partner_id.id,
                #     'id_proof':record.id_proof,
                #     'tenant_certificate':record.tenant_certificate,
                # })

    # @api.model_create_multi
    # def create(self, vals_list):
    #     records = super().create(vals_list)
    #
    #     for record in records:
    #         if record.id_proof or record.tenant_certificate:
    #             self.env['resident.proof'].create({
    #                 'resident_id': record.id,
    #                 'id_proof': record.id_proof,
    #                 'tenant_certificate': record.tenant_certificate,
    #             })
    #
    #     return records

    @api.model_create_multi
    def create(self, vals_list):
        resident=super().create(vals_list)

        for record in resident:
            print('\n\n\n...........record..........',record)
            check_partner=self.env['res.users'].search([
                ('partner_id','=',record.partner_id.id),
                ('email','=',record.email),
            ],limit=1)
            print('\n\n\n............check_partner..........',check_partner)
            if not check_partner and (record.email or record.mobile_number):
                user=self.env['res.users'].create({
                    'name':record.name,
                    # .partner_id
                    'phone':record.mobile_number,
                    'login':record.email,
                    'email':record.email,
                    'password':f'{record.name}1234',
                    'tower_id': record.tower_id.id if record.tower_id else False,
                    # 'block':record.tower_id.block,
                    # 'implied_ids':[(4, self.env.ref('smart_society.group_registration_user'))],
                    # "group_ids": [Command.set([self.ref("base.group_portal")])]
                    'group_ids': [(4,self.env.ref('smart_society.group_registration_user').id),
                                  (4,self.env.ref("base.group_portal").id)],
                    # 'group_ids': self.env.ref('base.group_user').ids,
                })

                # (4, self.env.ref('base.group_user').id),
                print('\n\n\n............check_partner..........',check_partner)
                if user:
                    record.user_id=user.id

        for record in resident:
            if record.id_proof or record.tenant_certificate:
                self.env['resident.proof'].create({
                    'resident_id': record.id,
                    'id_proof': record.id_proof,
                    'tenant_certificate': record.tenant_certificate,
                })
        return resident

    @api.onchange('flat_id')
    def change_flat_status(self):
        for record in self:
            self.env['resident.registrations'].search([
                ('flat_id','=',record.flat_id.id),
            ])
            # flat=record.flat_id.id
            print('\n\n\n............record.flat_id.......',record.flat_id)
            print('\n\n\n.............record.flat_id.id...',record.flat_id.id)
            search_flat=self.env['society.flat'].search([
                ('id','=',record.flat_id.id),
            ])
            print('\n\n.........out...search_flat............',search_flat)
            if search_flat:
                print('\n\n\n.....if.......search_flat...........',search_flat)
                search_flat.write({
                    'flat_status':'occupied'
                })

                # print('\n\n\n....fs.......',fs)


         # 'name': 'Marc Demo',
         #    'email': 'mark.brown23@example.com',
         #    'image_1920': False,
         #    'create_date': '2015-11-12 00:00:00',
         #    'login': 'demo_1',
         #    'password': 'demo_1',
         #    'partner_id': partner_without_image.id,

    @api.constrains('vehicle_count','vehicle_ids')
    def check_vehicle(self):
        for registration in self:
            if registration.has_vehicle:
                count=len(registration.vehicle_ids)
                if registration.vehicle_count<count or registration.vehicle_count>count:
                    print('.........if...registration.has_vehicle..............', count)
                    raise ValidationError('the vehicle count and vehicle added is different ')
                print('............registration.has_vehicle..............',count)

    @api.constrains('mobile_number')
    def check_mobile_number(self):
        for registration in self:
            if registration.resident_type=='owner' and not registration.mobile_number:
                registration.real_owner=registration.name
                print('.................................',registration.mobile_number)
                raise ValidationError('enter mobile number')
            if registration.mobile_number:
                regex=r'^\d{10}$'
                if not re.match(regex,registration.mobile_number):
                    raise ValidationError('enter 10 digit mobile number')

    @api.constrains('email')
    def check_email(self):
        for registration in self:
            if registration.email:
                regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}$'
                if not re.match(regex, registration.email):
                    raise ValidationError('enter valid email address')

    @api.constrains('emergency_contacts')
    def check_emergency_contacts(self):
        for registration in self:
            if registration.emergency_contacts:
                regex=r'^\d{10}$'
                if not re.match(regex,registration.emergency_contacts):
                    raise ValidationError('enter 10 digit mobile number')

    @api.constrains('age')
    def check_age(self):
        for registration in self:
            if registration.age<0:
                raise ValidationError('enter valid age')



class ResidentProof(models.Model):
    _name='resident.proof'

    resident_id=fields.Many2one('resident.registrations')
    id_proof = fields.Binary(string="ID Proof Copy")
    tenant_certificate=fields.Binary(string='Tenant Certificate')




class SecurityHistory(models.Model):
    _name='security.history'

    security_guard_id=fields.Many2one('security.guard',string='Security Guard')
    security_id = fields.Many2one('hr.employee',related='security_guard_id.security_id',
        store=True,readonly=True,string='Employee')
    tower_id=fields.Many2one('society.tower',string='Tower')
    mobile_number=fields.Char(string="Mobile Number")
    email=fields.Char(string='Email')
    age = fields.Integer(string='Age', required=True,readonly=False)
    join_date=fields.Date(string='Join Date')
    leave_date=fields.Date(string='Leave Date')
    aadhaar_card_copy=fields.Binary(string="Aadhaar Card Copy")
    pan_card_copy=fields.Binary(string="Pan Card Copy")
    police_verification_proof=fields.Binary(string="Police Verification Proof")
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')

class SecurityGuard(models.Model):
    _name='security.guard'
    _description='Security Guard'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char(string='Name')
    security_id = fields.Many2one('hr.employee', string="Security", readonly=False)
    tower_id=fields.Many2one('society.tower',string='Tower')
    mobile_number = fields.Char(related='security_id.mobile_phone', readonly=False, related_sudo=False)
    email = fields.Char(related='security_id.work_email', readonly=False, related_sudo=False)
    age = fields.Integer(string='Age', readonly=False)
    address=fields.Char(string='Address')
    aadhaar_card_copy=fields.Binary(string="Aadhaar Card Copy")
    pan_card_copy=fields.Binary(string="Pan Card Copy")
    police_verification_proof=fields.Binary(string="Police Verification Proof")
    working_hours_id = fields.Many2one(related='security_id.resource_calendar_id',
        string='Working Hours',store=True,readonly=False)
    join_date=fields.Date(string='Join Date')
    leave_date=fields.Date(string='Leave Date')

    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')
    security_history_ids=fields.One2many('security.history','security_guard_id')
    security_documents_ids=fields.One2many('security.guard.document','security_guard_id')




    def action_new_security(self):
        for record in self:
            self.env['security.history'].create({
                'security_guard_id': record.id,
                'tower_id': record.tower_id.id,
                'mobile_number': record.mobile_number,
                'email': record.email,
                'age': record.age,
                'join_date': record.join_date,
                'leave_date': fields.Date.today(),
                'aadhaar_card_copy':record.aadhaar_card_copy,
                'pan_card_copy':record.pan_card_copy,
                'police_verification_proof':record.police_verification_proof,
            })

            record.write({
                'state': 'inactive',
                'leave_date': fields.Date.today(),
            })

            # Remove old document records
            # record.security_documents_ids.unlink()

            # Clear form for next guard
            record.write({
                'security_id': False,
                'age': 0,
                'address': False,
                'aadhaar_card_copy': False,
                'pan_card_copy': False,
                'police_verification_proof': False,
                'join_date': False,
                'leave_date': False,
                'state': 'active',
            })

    @api.constrains('mobile_number')
    def check_mobile_number(self):
        for registration in self:
            if not registration.mobile_number:
                print('.................................',registration.mobile_number)
                raise ValidationError('enter mobile number')
            if registration.mobile_number:
                regex=r'^\d{10}$'
                if not re.match(regex,registration.mobile_number):
                    raise ValidationError('enter 10 digit mobile number')

    @api.constrains('email')
    def check_email(self):
        for registration in self:
            if registration.email:
                regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}$'
                if not re.match(regex, registration.email):
                    raise ValidationError('enter valid email address')


    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.email:
                user = self.env['res.users'].create({
                    'name': record.name,
                    'login': record.email,
                    'email': record.email,
                    'password': f'{record.name}1234',
                    'phone': record.mobile_number,
                    'group_ids': [
                        (4, self.env.ref('smart_society.group_registration_security').id)
                    ],
                })

                record.security_id.user_id = user.id

            self.env['security.guard.document'].create({
                'security_guard_id': record.id,
                'security_id':record.security_id.id,
                'aadhaar_card_copy': record.aadhaar_card_copy,
                'pan_card_copy': record.pan_card_copy,
                'police_verification_proof':record.police_verification_proof,
                'mobile_number':record.mobile_number,
            })

        return records


    def write(self, vals):
        res = super().write(vals)

        for record in self:
            print('\n\n\n......record................',record)
            if record.security_id:
                print('\n\n\nrecord.security_id........write.........',record.security_id)
                existing_doc = self.env['security.guard.document'].search([
                    ('security_guard_id', '=', record.id),
                    ('security_id', '=', record.security_id.id)
                ], limit=1)
                print('\n\n\nexisting_doc.......write.........',existing_doc)

                if not existing_doc:
                    print('existing_doc.........',existing_doc)
                    self.env['security.guard.document'].create({
                        'security_guard_id': record.id,
                        'security_id': record.security_id.id,
                        'aadhaar_card_copy': record.aadhaar_card_copy,
                        'pan_card_copy': record.pan_card_copy,
                        'police_verification_proof': record.police_verification_proof,
                    })

        return res

    @api.depends('security_id')
    def _compute_attendance_status(self):
        for record in self:

            record.attendance_status = 'absent'
            record.worked_hours = 0.0

            if not record.security_id:
                continue

            today = fields.Date.today()

            attendance = self.env['hr.attendance'].search([
                ('employee_id', '=', record.security_id.id),
                ('check_in', '>=', datetime.combine(today, time.min)),
                ('check_in', '<=', datetime.combine(today, time.max)),
            ], limit=1)

            if attendance:
                record.attendance_status = 'present'
                record.worked_hours = attendance.worked_hours






class SecurityGuardDocument(models.Model):
    _name = 'security.guard.document'

    security_guard_id = fields.Many2one('security.guard',string='Security Guard')
    security_id = fields.Many2one('hr.employee', string="Security", readonly=False)
    aadhaar_card_copy = fields.Binary(required=True,string='Aadhaar Card')
    pan_card_copy = fields.Binary(required=True,string='Pan Card')
    police_verification_proof=fields.Binary(string="Police Verification Proof")
    mobile_number = fields.Char(string='Mobile Number')



class VisitorRegistrations(models.Model):
    _name = 'visitor.registrations'

    name = fields.Char(required=True, string='Name')
    partner_id = fields.Many2one('res.partner', string='Visitor')
    mobile_number = fields.Char(required=True, string='Mobile Number')
    has_vehicle = fields.Boolean(string='Has Vehicle')
    vehicle_number = fields.Char(string='Vehicle Number')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            partner = self.env['res.partner'].create({
                'name': vals.get('name'),
            })
            vals['partner_id'] = partner.id

        return super().create(vals_list)















    # @api.model_create_multi
    # def create(self, vals_list):
    #     security=super().create(vals_list)
    #     for record in security:
    #
    #         if record.email:
    #             user=self.env['res.users'].create({
    #                 'name':record.name,
    #                 # 'partner_id'
    #                 'login':record.email,
    #                 'email':record.email,
    #                 'password':f'{record.name}1234',
    #                 'phone': record.mobile_number,
    #                 'group_ids': [(4,self.env.ref('smart_society.group_registration_security').id)],
    #             })
    #
    #             # print('\n\n\n............check_partner..........',check_partner)
    #             record.security_id.user_id = user.id
    #             self.env['security.guard.document'].create({
    #                 'security_guard_id': record.id,
    #                 'security_id': record.security_id,
    #                 'aadhaar_card_copy': record.aadhaar_card_copy,
    #                 'pan_card_copy': record.pan_card_copy,
    #
    #             })
    #
    #     return security
    # def action_new_security(self):
    #     for record in self:
    #         security_guard_id=self.env['security.history'].search([
    #             ('security_guard_id','=',record.security_id)
    #         ])
    #         if not security_guard_id:
    #             self.env['security.history'].create({
    #                 # 'security_id':record.security_id,
    #                 'tower_id':record.tower_id,
    #                 'mobile_number':record.mobile_number,
    #                 'email':record.email,
    #                 'age':record.age,
    #                 'join_date':record.join_date,
    #                 'leave_date':fields.Date.today(),
    #             })
    #         record.write({
    #             'security_id':False,
    #             'age':False,
    #             'email':False,
    #             'address':False,
    #             'join_date':False,
    #             # 'leave_date':fields.Date.today(),
    #         })






    # mobile_number = fields.Char(string='Mobile Number', readonly=False,required=True)
    # aadhaar_number=fields.Char(string='Aadhaar Number', required=True)
    # pan_number=fields.Char(string='Pan Number', required=True)
    # name=fields.Char(related='security_id.name',string='Name',readonly=False)
    # email=fields.Char(related='security_id.email',string='Email',readonly=False,required=True)
    # email=fields.Char(string='Email',readonly=False,required=True)
    # partner_id=fields.Many2one('hr.employee',required=True)
    # shift=fields.Selection([('morning','Morning Shift'),('night','Night Shift')])
    # document_type = fields.Selection([
    #     ('aadhaar', 'Aadhaar'),
    #     ('pan', 'PAN'),
    #     ('police', 'Police Verification'),
    #     ('photo', 'Photo'),
    #     ('other', 'Other')
    # ])
    # file_name = fields.Char()
# print('\n\n\n...........record..........',record)
# check_partner=self.env['res.users'].search([
#     # ('partner_id','=',record.security_id.id),
#     ('partner_id','=',record.security_id.id),
#     # ('email','=',record.email),
# ],limit=1)
# print('\n\n\n............check_partner..........',check_partner)
# if not check_partner and record.email:
# class VisitorRegistrations(models.Model):
#     _name='visitor.registrations'
#     _description='Visitor Registrations'



#
#
#     partner_id=fields.Many2one('res.partner')
#     # name=fields.Char(related='partner_id.name')
#     mobile_number = fields.Char(string='Mobile Number')
#     has_vehicle=fields.Boolean(string='Has Vehicle')
#     vehicle_number=fields.Char(string='Vehicle Number')
#     # tower_id=fields.Many2one('society.tower',compute=)
#
#
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         visitor=super().create(vals_list)
#
#         for record in visitor:
#             print('\n\n\n...........record..........',record)
#             check_partner=self.env['res.partner'].search([
#                 # ('partner_id','=',record.security_id.id),
#                 ('id','=',record.partner_id.id),
#                 # ('email','=',record.email),
#             ],limit=1)
#             print('\n\n\n............check_partner..........',check_partner)
#             if not check_partner and record.email:
#                 self.env['res.partner'].create({
#                     'name':record.name,
#                 })
#                 print('\n\n\n............check_partner..........',check_partner)
#
#         return visitor
#
#
#
#     @api.constrains('mobile_number')
#     def check_mobile_number(self):
#         for registration in self:
#             if not registration.mobile_number:
#                 print('.................................',registration.mobile_number)
#                 raise ValidationError('enter mobile number')
#             if registration.mobile_number:
#                 regex=r'^\d{10}$'
#                 if not re.match(regex,registration.mobile_number):
#                     raise ValidationError('enter 10 digit mobile number')
#
#     # @api.constrains('vehicle_number','vehicle_type')
#     @api.constrains('has_vehicle')
#     def vehicle_number_validation(self):
#         regex=r'^[A-Z]{2}[ ]?[0-9]{2}[ ]?[A-Z]{1,2}[ ]?[0-9]{4}$'
#         for record in self:
#             if record.has_vehicle and not record.vehicle_number:
#                 raise ValidationError('Enter Proper Vehicle Number')
#             else:
#                 if record.has_vehicle and not re.match(regex, record.vehicle_number):
#                     raise ValidationError('Vehicle Number Error')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # @api.constrains('resident_type')
#     # @api.depends('vehicle_count','vehicle_ids')
#     # @api.onchange('vehicle_count','vehicle_ids')
#     # def check_vehicle_count(self):
#         # for registration in self:
#             # if registration.has_vehicle:
#                 # print('\n\n\n\n.....registration.has_vehicle',registration.has_vehicle)
#                 # count=len(registration.vehicle_ids)
#                 # print('\n\n\n\n.....registration.vehicle_ids',registration.vehicle_ids)
#                 # count=registration.search_count['vehicle.registrations']
#                 # print('\n\n\n\n.....registration.vehicle_ids count......',count)






















