from odoo import models,fields,api


class SocietySetup(models.Model):
    _name='society.setup'
    _description='Society Setup Model'

    name=fields.Char(string='Society Name' , required=True)
    society_reg_number=fields.Char(string='Society Registration Number')
    society_address=fields.Char(string='Society Address')
    street=fields.Char(string='Street')
    street2=fields.Char(string='Street2')
    city=fields.Char(string='City')
    # city_id = fields.Many2one('res.city', string='City ID')
    state_id=fields.Many2one('res.country.state',string='State')
    country_id = fields.Many2one('res.country', string='Country',required=True)
    zip=fields.Char(string='zip')
    # pincode=fields.Char(string='Pincode')
    society_ids=fields.One2many('society.tower','society_id',string='Tower')
    tower_count=fields.Integer(string='Tower Count')
    has_gym=fields.Boolean(string='Has Gym')
    location_gym=fields.Char(string=' Gym Location')
    gym_capacity=fields.Integer(string='Gym Capacity',required=True)
    has_clubhouse=fields.Boolean(string='Has Clubhouse')
    location_cb=fields.Char(string='Clubhouse Location')
    # has_guesthouse=fields.Boolean(string='Guest Room')
    # guesthouse_count=fields.Integer(string='Guest House Count')
    gym_booking_charge=fields.Float(string='Gym Booking Charge per day')
    cbh_booking_charge=fields.Float(string='Clubhouse Booking Charge')
    # gym_slot_ids=fields.One2many('gym.slots','society_id',string='Gym Slots')
    # gh_ids=fields.One2many('society.guesthouse','society_id',string='Towers')

    @api.constrains('tower_count')
    def generate_tower(self):
        for record in self:
            for i in range(record.tower_count):
                existing_tower = self.env['society.tower'].search([
                    ('society_id', '=', record.name),
                    ('name', '=', f'{record.id}-tower-{i + 1}')
                ], limit=1)

                if not existing_tower:
                    self.env['society.tower'].create({
                        'name': f'{record.name}-tower-{i + 1}',
                        'society_id': record.id,
                    })

    # @api.constrains('tower_count')
    # def generate_tower(self):
    #     for record in self:
    #         for tower in range(record.tower_count):
    #             tower=self.env['society.tower'].search([
    #                 ('society_id','=',record.id),
    #                 ('name', '=', f'{record.id}-tower-{tower + 1}')
    #             ])
    #             if not tower:
    #                 self.env['society.tower'].create({
    #                 'name':f'{record.id}-tower-{tower+1}',
    #                 'society_id':record.id,
    #                 })

    # @api.constrains('gym_capacity')
    # def create_gym_slot(self):
    #     for record in self:
    #         print('..............record........',record)
    #         list1=['morning','afternoon','evening','night']
    #         for shift in range(len(list1)):
    #             print('.........shift....',shift)
    #             first_letter=(list1[shift][0]).upper()
    #             print('\n\n\n\n........first_letter.....',first_letter)
    #             print('\n\n\n....record.gym_capacity....',record.gym_capacity)
    #             for slot in range(record.gym_capacity):
    #                 # print('\n\n...slot.....',slot)
    #                 exist_slot=self.env['gym.slots'].search([
    #                     ('name','=',f'{first_letter}-slot{slot + 1}'),
    #                     ('society_id', '=', record.id),
    #
    #                 ])
    #                 # ('name','=',f'res-{park.parking_place}-t{park.tower_id.id}-{i + 1}'),
    #                 if not exist_slot:
    #                     print('\n\n\n......not.exist_slot..', exist_slot)
    #                     g_slots=self.env['gym.slots'].create({
    #                         'name':f'{first_letter}-slot{slot + 1}',
    #                         'society_id':record.id,
    #                         'shift':list1[shift],
    #                     })
    #                     print('.....g_slots......',g_slots)


# class GymSlots(models.Model):
#     _name='gym.slots'
#     _description='Gym Slots Model'
# 
#     society_id=fields.Many2one('society.setup',string='Society')
#     name=fields.Char(string='Gym Slots Name')
#     shift=fields.Selection(selection=[('morning','Morning'),('afternoon','Afternoon'),('evening','Evening'),('night','Night')])
#     gym_booking_charge=fields.Float(related='society_id.gym_booking_charge',string='Gym Booking Charge')
#     is_occupied=fields.Boolean(string='Is Occupied')
#     resident_id=fields.Many2one('resident.registrations',string='Resident ID')
#
#     @api.onchange('resident_id')
#     def is_occupied_resident(self):
#         for record in self:
#             if record.resident_id:
#                 record.is_occupied=True
#             elif not record.resident_id:
#                 record.is_occupied=False






class GuestHouse(models.Model):
    _name='society.guesthouse'
    _description='Guest House Model'

    name=fields.Char(string='Guest House Name')
    floor_number=fields.Integer(string='Floor Number' ,default=0)
    # gh_booking_charge=fields.Float(string='Booking Price per day')
    flat_type=fields.Selection(string='Flat Type',
                                   selection=[('1bhk','1 BHK'),('2bhk','2 BHK'),
                                   ('3bhk','3 BHK')])
    gh_status=fields.Selection(string='Flat Status',
                                 selection=[('occupied','Occupied'),('vacant','Vacant'),
                                            ('under_maintenance','Under Maintenance')])
    # society_id=fields.Many2one('society.setup',string='Society')
    tower_id=fields.Many2one('society.tower',string='GuestHouse Location')
    price_per_person=fields.Float(string='Price Person per day')
    is_occupied=fields.Boolean(string='Is Occupied')




    # @api.depends('price_per_person','person_count','days')
    # def calculate_person_price(self):
    #     for record in self:
    #         record.total_price = (record.person_count * record.price_per_person)*record.days
    #











    # related = 'flat_id.society_id',

    # @api.constrains('flat_id')
    # def check_flat(self):
    #     for record in self:
    #         pass



    # @api.model
    # def create(self, vals_list):
    #     guest_house=super().create(vals_list)
    #     print('\n\n\n.........guest_house........',guest_house)
    #     for house in guest_house:
    #         print('\n........house.........',house)
    #         search_house=self.env['society.flat'].search([
    #             ('flat_status','=','guest_house')
    #         ],limit=1)
    #         print('..................search_house...............',search_house)




# class Committee(models.Model):
#     _name='society.committee'
#     _description='Committees in society'
#
#     name=fields.Char(string='Committee name')
#     committee_name=fields.Many2many('res.partner',string='Committee members',required=True)
#     chairman_name=fields.Many2one('res.partner',string='Chairman')
#     secretary_name=fields.Many2one('res.partner',string='Secretary')
#     society_id=fields.Many2one('society.setup',string='Society')
#
