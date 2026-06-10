from odoo import models,fields,api
from odoo.exceptions import ValidationError
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
    real_owner=fields.Char(string='Real Owner',required=True)
    tenant_certificate=fields.Binary(string='Tenant Certificate')
    user_id = fields.Many2one( 'res.users',string='User',readonly=False)



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
            if not check_partner and record.email or record.mobile_number:
                user=self.env['res.users'].create({
                    'name':record.name,
                    # .partner_id
                    'phone':record.mobile_number,
                    'login':record.email,
                    'email':record.email,
                    'password':f'{record.name}1234',
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

class SecurityGuard(models.Model):
    _name='security.guard'
    _description='Security Guard'

    security_id = fields.Many2one('hr.employee', string="Security", readonly=False)
    # partner_id=fields.Many2one('hr.employee',required=True)
    tower_id=fields.Many2one('society.tower',string='Tower')
    mobile_number = fields.Char(related='security_id.mobile_phone', readonly=False, related_sudo=False)
    email = fields.Char(related='security_id.work_email', readonly=False, related_sudo=False)
    name=fields.Char(related='security_id.name',string='Name',readonly=False)
    # email=fields.Char(related='security_id.email',string='Email',readonly=False,required=True)
    # email=fields.Char(string='Email',readonly=False,required=True)
    age = fields.Integer(string='Age', required=True,readonly=False)
    # mobile_number = fields.Char(string='Mobile Number', readonly=False,required=True)
    aadhaar_number=fields.Char(string='Aadhar Number', required=True)
    pan_number=fields.Char(string='Pan Number', required=True)
    address=fields.Char(string='Address', required=True)
    shift=fields.Selection([('morning','Morning Shift'),('night','Night Shift')])


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
        security=super().create(vals_list)

        for record in security:
            print('\n\n\n...........record..........',record)
            check_partner=self.env['res.users'].search([
                # ('partner_id','=',record.security_id.id),
                ('partner_id','=',record.security_id.id),
                ('email','=',record.email),
            ],limit=1)
            print('\n\n\n............check_partner..........',check_partner)
            if not check_partner and record.email:
                self.env['res.users'].create({
                    'name':record.name,
                    # 'partner_id'
                    'login':record.email,
                    'email':record.email,
                    'password':f'{record.name}1234',
                    'phone': record.mobile_number,
                    'group_ids': [(4,self.env.ref('smart_society.group_registration_security').id)],
                })
                print('\n\n\n............check_partner..........',check_partner)

        return security





class VisitorRegistrations(models.Model):
    _name='visitor.registrations'
    _description='Visitor Registrations'

    partner_id=fields.Many2one('res.partner',required=True)
    name=fields.Char(related='partner_id.name')
    mobile_number = fields.Char(string='Mobile Number', required=True)
    has_vehicle=fields.Boolean(string='Has Vehicle',default=False)
    vehicle_number=fields.Char(string='Vehicle Number', required=True)























    # @api.constrains('resident_type')
    # @api.depends('vehicle_count','vehicle_ids')
    # @api.onchange('vehicle_count','vehicle_ids')
    # def check_vehicle_count(self):
        # for registration in self:
            # if registration.has_vehicle:
                # print('\n\n\n\n.....registration.has_vehicle',registration.has_vehicle)
                # count=len(registration.vehicle_ids)
                # print('\n\n\n\n.....registration.vehicle_ids',registration.vehicle_ids)
                # count=registration.search_count['vehicle.registrations']
                # print('\n\n\n\n.....registration.vehicle_ids count......',count)






















