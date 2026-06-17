import random
import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ParkingManagement(models.Model):
    _name = 'parking.management'
    _description = 'Parking Management'

    name = fields.Char(string='Parking name', required=True)
    tower_id = fields.Many2one('society.tower', string='Tower', required=True)
    society_id = fields.Many2one(related='tower_id.society_id')
    parking_place = fields.Selection(string='Parking Place', selection=[
        ('basement1', 'Basement 1'), ('basement2', 'Basement 2'), ('ground', 'Ground')
    ], required=True)
    resident_parking = fields.Integer(string='Resident Parking', placeholder='0')
    visitor_parking = fields.Integer(string='Visitor Parking', placeholder='0')
    ev_parking = fields.Integer(string='Ev Parking', placeholder='0')
    other_parking = fields.Integer(string='other parking', placeholder='0')
    parking_count = fields.Integer(string="Tower's parking count", related='tower_id.parking_area')
    total_slot = fields.Integer(compute='_compute_total_slot', string='Total Slots')
    available_slot = fields.Integer(compute='_compute_available_slot', string='Available Slots')
    occupied_slot = fields.Integer(compute='_compute_available_slot', string='Occupied')
    parking_slot_ids = fields.One2many('parking.slot', 'parking_id', string='Parking Slots')

    # area=fields.Integer(string='Area(sq)')
    # tower_id=fields.Many2one('society.tower',related='tower_id.parking_area',string='Towers')
    # flat_id=fields.Many2one('society.flat')

    @api.depends('resident_parking', 'visitor_parking', 'ev_parking', 'other_parking')
    def _compute_total_slot(self):
        for park in self:
            park.total_slot = (park.resident_parking + park.visitor_parking +
                               park.ev_parking + park.other_parking)

    @api.depends('parking_slot_ids', 'parking_slot_ids.is_occupied')
    def _compute_available_slot(self):
        for park in self:
            # occupied_slot = self.env['parking.slot'].search([
            #     ('parking_id','=',park.id),
            #     ('tower_id','=',park.tower_id.id),
            #     ('is_occupied','=',True)
            # ],limit=1)

            # print('\n\n\n...............search....occupied_slot........................',occupied_slot)
            print('.......................park.total_slot', park.total_slot)
            print('......................park.parking_slot_ids', park.parking_slot_ids)
            print('\n\n......................park.occupied_slot', park.occupied_slot)
            park.occupied_slot = len(park.parking_slot_ids.filtered(lambda x: x.is_occupied))
            print('\n\n....................occupied.', park.occupied_slot)
            park.available_slot = park.total_slot - park.occupied_slot
            print('..........park.available_slot......', park.available_slot)

    @api.constrains('resident_parking', 'visitor_parking', 'ev_parking', 'other_parking')
    def generate_slot(self):
        count = 0
        for park in self:
            print('\n\n\n\n\n..............generate_slot')
            park.parking_slot_ids.unlink()
            # ------------------resident parking------------------------------------
            for i in range(park.resident_parking):
                print('....................i', i)
                exist_slot = self.env['parking.slot'].search([
                    ('parking_id', '=', park.id),
                    ('tower_id', '=', park.tower_id.id),
                    ('name', '=', f'res-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{i + 1}'),
                ])
                if not exist_slot:
                    self.env['parking.slot'].create({
                        'parking_id': park.id,
                        'tower_id': park.tower_id.id,
                        # 'name':f'res-{park.parking_place[0-5]}-t{park.tower_id}-{park.resident_parking+i+1}',
                        'name': f'res-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{i + 1}',
                        'parking_place': park.parking_place,
                        'parking_type': 'resident_parking',
                    })
                count += 1
                print('...........................count......', count)
                print('park_slot.....................')

            # -----------------------visitor parking--------------------------------------------
            for j in range(park.visitor_parking):
                exist_slot = self.env['parking.slot'].search([
                    ('parking_id', '=', park.id),
                    ('tower_id', '=', park.tower_id.id),
                    ('name', '=', f'vis-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{j + 1}'),
                ])
                if not exist_slot:
                    self.env['parking.slot'].create({
                        'parking_id': park.id,
                        'tower_id': park.tower_id.id,
                        'name': f'vis-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{j + 1}',
                        'parking_place': park.parking_place,
                        'parking_type': 'visitor_parking',
                    })
                count += 1
                print('......................visitor.....count......', count)

            # ---------------------------ev_parking---------------------------------------------
            for k in range(park.ev_parking):
                exist_slot = self.env['parking.slot'].search([
                    ('parking_id', '=', park.id),
                    ('tower_id', '=', park.tower_id.id),
                    ('name', '=', f'ev-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{k + 1}'),
                ])
                if not exist_slot:
                    self.env['parking.slot'].create({
                        'parking_id': park.id,
                        'tower_id': park.tower_id.id,
                        'name': f'ev-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{k + 1}',
                        'parking_place': park.parking_place,
                        'parking_type': 'ev_charging',
                    })
                count += 1
                print('......................ev_charging.....count......', count)

            # ---------------------------other_parking---------------------------------------------
            for l in range(park.other_parking):
                exist_slot = self.env['parking.slot'].search([
                    ('parking_id', '=', park.id),
                    ('tower_id', '=', park.tower_id.id),
                    ('name', '=', f'oth-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{l + 1}'),
                ])
                if not exist_slot:
                    self.env['parking.slot'].create({
                        'parking_id': park.id,
                        'tower_id': park.tower_id.id,
                        'name': f'oth-{park.parking_place}-{park.society_id.name}-t{park.tower_id.id}-{l + 1}',
                        'parking_place': park.parking_place,
                        'parking_type': 'other_parking',
                    })
                count += 1
                print('......................other_parking.....count......', count)


class ParkingSlot(models.Model):
    _name = 'parking.slot'
    _description = 'Parking Slot'

    tower_id = fields.Many2one(related='parking_id.tower_id', string='Tower')
    parking_id = fields.Many2one('parking.management', string='Parking')
    flat_id = fields.Many2one('society.flat', string='Allocated Flat')
    name = fields.Char(string='Slot Name/Number', required=True)
    parking_place = fields.Selection([
        ('basement1', 'Basement 1'),
        ('basement2', 'Basement 2'),
        ('ground', 'Ground')
    ], string='Parking Place')
    parking_type = fields.Selection(string='Parking Type', selection=[
        ('resident_parking', 'Resident Parking'), ('visitor_parking', 'Visitor Parking'),
        ('other_parking', 'Other Parking'),
        ('ev_charging', 'Ev Charging'), ('other', 'Other')
    ])
    print('................................flat_id', flat_id)
    is_occupied = fields.Boolean(string='Occupied', default=False)

    @api.onchange('flat_id')
    def have_flat(self):
        for record in self:
            if record.flat_id:
                record.is_occupied = True
            elif not record.flat_id:
                record.is_occupied = False

    # @api.constrains('flat_id','is_occupied'),compute='_have_flat_id'
    # @api.depends('flat_id')
    # def _have_flat_id(self):
    #     # self.ensure_one()
    #     for record in self:
    #         if record.flat_id:
    #             print('\n\n\n.........record.flat_id................',record.flat_id)
    #             have_flat=self.env['parking.slot'].search([
    #                 ('id', '=', record.id),
    #                 ('flat_id','=',record.flat_id.id)
    #             ],limit=1)
    #             print('\n\n\n.......have_flat.......',have_flat)
    #             have_flat.write({'is_occupied':True})
    #             print('\n\n\n........have_flat.write({is_occupied:True})...',have_flat.write({'is_occupied':True}))

    #         print("\n\n\n\n.............record........",record)
    #         print("\n\n\n\n......record.flat_id......", record.flat_id)
    #         if record.flat_id:
    #             # record.is_occupied = True
    #             record.write({'is_occupied':True})
    #             print("\n\n\n\n......record.flat_id......",record.flat_id)
    # if record.flat_id:
    #     record.is_occupied = True

    # vehicle_id = fields.Many2one('vehicle.registrations',string='Allocated Vehicle')
    # active = fields.Boolean(default=True)
    # vehicle_tracking_ids = fields.One2many('vehicle.tracking', 'parking_slot_id',
    #                                        string='Vehicle Tracking')

    _sql_constraints = [('slot_unique', 'unique(name)', 'Parking Slot already exists!')]


class VehicleTracking(models.Model):
    _name = 'vehicle.tracking'
    _description = 'Person and Vehicle Tracking'

    # parking_id=fields.Many2one('parking.management',string='Parking')
    # name=fields.Char(string='Vehicle Tracking')
    person_type = fields.Selection(string='Person type',
                                   selection=[('resident', 'Resident'), ('visitor', 'Visitor'), ('other', 'Other')],
                                   required=True)
    resident_id = fields.Many2one('resident.registrations', string='Resident')
    visitor_id = fields.Many2one('visitor.registrations', string='Visitor')
    # , required = True
    # tower_id=fields.Many2one('society.tower',string='Tower')'resident.registrations',
    # flat_id=fields.Many2one('society.flat',string='Flat')'resident.registrations',

    flat_id = fields.Many2one(related='resident_id.flat_id', string='Flat')
    tower_id = fields.Many2one(related='flat_id.tower_id', string='Tower')

    visitor_phone = fields.Char(related='visitor_id.mobile_number',string='Phone number',readonly=False)
    has_vehicle = fields.Boolean(string='Has Vehicle', default=False)
    vehicle_id = fields.Many2one('vehicle.registrations', string='Vehicle')
    vehicle_number = fields.Char(related="visitor_id.vehicle_number", string='Vehicle number')
    entry_time = fields.Datetime(string='Entry Time', required=True, default=fields.Datetime.now)
    exit_time = fields.Datetime(string='Exit Time')
    # parking_type = fields.Selection(string='Parking Type', selection=[
    #     ('resident', 'Resident'), ('visitor', 'Visitor'), ('other', 'Other')])
    parking_slot_id = fields.Many2one('parking.slot', string='Parking Slot')
    is_occupied = fields.Boolean(string='Is Occupied', default=False)
    security_id = fields.Many2one('security.guard', string='Security',
                                  default=lambda self: self.env['security.guard'].search(
                                      [('security_id', '=', self.env.user.id)], limit=1))
    # , compute = '_compute_current_security'
    # not assinging
    visiting_flat = fields.Many2one('society.flat', string='Visiting Flat')
    # visiting_tower=fields.Many2one('society.tower',string='Visiting Tower')
    visiting_tower = fields.Many2one(related='visiting_flat.tower_id', string='Visiting Tower')
    parking_type = fields.Selection(string='Parking Type', selection=[
        ('resident_parking', 'Resident Parking'), ('visitor_parking', 'Visitor Parking'),
        ('other_parking', 'Other Parking'),
        ('ev_charging', 'Ev Charging'), ('other', 'Other')
    ])
    visit_purpose = fields.Char(string='Visit Purpose')

    #
    # def _compute_current_security(self):
    #     for record in self:
    #         guard=self.env['security.guard'].search([
    #             ('security_id','=',self.env.user.id)
    #         ],limit=1)
    #         print('..............guard',guard)

    @api.constrains('person_type', 'resident_id', 'flat_id', 'tower_id', 'parking_slot_id', 'entry_time', 'exit_time')
    def track_according_type(self):
        for record in self:

            if record.parking_slot_id:
                # record.is_occupied=True
                print('\n\n\n.....record.parking_slot_id.id..................', record.parking_slot_id.id)
                slot_occupied = self.env['parking.slot'].search([
                    # ('parking_type', '=', 'visitor_parking'),
                    ('parking_type', '=', record.parking_type),
                    ('id', '=', record.parking_slot_id.id),
                ], limit=1)

                # ('parking_type','=','visitor_parking'),
                # ('parking_id','=',record.parking_slot_id.id),
                print('\n\n\n\n.....................slot_occupied', slot_occupied)
                print('\n\n\n\n.....................slot_occupied', slot_occupied.parking_id)
                if record.entry_time and not record.exit_time:
                    print(slot_occupied.write({'is_occupied': True}))
                elif record.entry_time and record.exit_time:
                    print(slot_occupied.write({'is_occupied': False}))
                elif record.flat_id:
                    print(slot_occupied.write({'is_occupied': True}))

    @api.onchange('person_type')
    def _onchange_person_type(self):
        if self.person_type == 'resident':
            self.parking_type = 'resident_parking'

        elif self.person_type == 'visitor':
            self.parking_type = 'visitor_parking'


    @api.constrains('person_type')
    def assign_parking_type(self):
        for record in self:
            if record.person_type != 'resident':
                if not record.visiting_tower and not record.visiting_flat:
                    raise ValidationError('Visiting tower or flat is required!')
                if not record.visit_purpose:
                    raise ValidationError('Visiting Purpose required')

            if record.person_type == 'other':
                record.parking_type = 'other_parking'
                if not record.visit_purpose:
                    raise ValidationError('Visiting Purpose required')

        # if record.parking_slot_id:
        #     # record.is_occupied=True
        #     print('\n\n\n.....record.parking_slot_id.id..................',record.parking_slot_id.id)
        #     slot_occupied=self.env['parking.slot'].search([
        #         ('parking_type','=','visitor_parking'),
        #         ('id','=',record.parking_slot_id.id),
        #     ],limit=1)
        #
        #     # ('parking_type','=','visitor_parking'),
        #     # ('parking_id','=',record.parking_slot_id.id),
        #     print('\n\n\n\n.....................slot_occupied',slot_occupied)
        #     print('\n\n\n\n.....................slot_occupied',slot_occupied.parking_id)
        #     if record.entry_time and not record.exit_time:
        #         print(slot_occupied.write({'is_occupied':True}))
        #     elif record.entry_time and record.exit_time:
        #         print(slot_occupied.write({'is_occupied':False}))

# class VehicleAllocation(models.Model):
#     _name='vehicle.allocation'
#     _description='Vehicle Allocation'
#
#     resident_id=fields.Many2one('res.partner',string='Resident')
#     vehicle_ids=fields.Many2many(related='resident_id.vehicle_ids',string='Vehicles')
#     parking_slot=fields.Many2one('parking.slot',string='Parking Slot')
#
#
#     def allocate_vehicle(self):
#         for vehicle in self.vehicle_ids:
#             self.env['vehicle.registrations'].search({
#
#             })
# resident_id=fields.Many2one('resident.registration',string='Resident')
# visitor_id=fields.Many2one('visitor.registration',string='Visitor')
# parking_count=fields.Integer(string='Parking Count',related='tower_id.parking_area')
# tower_id=fields.Many2one('society.tower')


# record.flat_id=record.resident_id.flat_id
# record.tower_id=record.flat_id.tower_id
# print('\n\n\n\n\n\n.........record.resident_id.........',record.resident_id)
# print('\n\n.........record.flat_id..........',record.flat_id)
# print('\n\n........record.resident_id.flat_id........',record.resident_id.flat_id)
# print('\n\n.........record.tower_id..........',record.tower_id)
# print('\n\n........record.resident_id.tower_id.........',tower_id)
# record.flat_id=record.resident_id.flat_id
# record.tower_id=tower_id
