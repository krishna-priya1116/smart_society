from odoo import models,fields,api
from odoo.exceptions import ValidationError


class Flat(models.Model):
    _name='society.flat'
    _description='Society Flats'

    name=fields.Char(string='Flat',required=True)
    tower_id=fields.Many2one('society.tower',required=True)
    # parking_slot_ids=fields.Many2many('parking.slot','flat_id',string='Parking Slots')
    flat_type=fields.Selection(string='Flat Type',
                                   selection=[('1bhk','1 BHK'),('2bhk','2 BHK'),
                                   ('3bhk','3 BHK')])
    block=fields.Selection(string='Blocks',
                               selection=[('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),])

    flat_member_ids=fields.One2many('resident.registrations','flat_id',string='Members')
    floor_no=fields.Integer(string='Floor Number',required=True)
    area=fields.Float(string='Area(sq ft)')
    facing_direction=fields.Selection(string='Facing Direction',
                                      selection=[('north','North'),('south','South'),
                                                 ('east','East'),('west','West')])
    flat_status=fields.Selection(string='Flat Status',default='vacant',
                                 selection=[('occupied','Occupied'),('vacant','Vacant'),
                                            ('under_maintenance','Under Maintenance')])
    no_of_rooms=fields.Integer(string='Number of Rooms')
    balcony_count=fields.Integer(string='Number of Balcony')
    bathroom_count=fields.Integer(string='Number of Bathroom')
    vehicle_ids=fields.One2many('vehicle.registrations',compute='_compute_vehicle_check',string='Vehicle ID')
    parking_slot_ids=fields.One2many('parking.slot','flat_id',string='Parking Slot',readonly=True)




    # @api.constrains('flat_status')
    def vehicle_slots(self):
        for flat in self:
            vehicle=self.env['vehicle.registrations'].search([
                ('flat_id','=',flat.id),
                ('vehicle_ids.id','=',flat.vehicle_ids.id),
            ])
            print('\n\n\n...............vehicle......',vehicle)


    @api.depends('flat_member_ids.vehicle_ids')
    def _compute_vehicle_check(self):
        for flat in self:
            print('......flat......',flat)
            print('.......flat.vehicle_ids.....',flat.vehicle_ids)
            print('......flat.flat_member_ids......',flat.flat_member_ids)
            flat.vehicle_ids=flat.flat_member_ids.mapped('vehicle_ids')


    @api.constrains('flat_status')
    def check_resident_type(self):
        for registration in self:
            if registration.flat_status == 'vacant':
                if registration.flat_member_ids:
                    registration.flat_member_ids.unlink()

    @api.depends('flat_member_ids')
    def check_flat_member_ids(self):
        for registration in self:
            if not registration.flat_member_ids:
                registration.flat_status='vacant'
            else:
                registration.flat_status='occupied'



    # parking_area=fields.Float(string='Parking Area',required=True)
    # parking_management_id=fields.Many2one('parking.management',string='Parking Management')
    # parking_slot_id=fields.Many2many('parking.slot')
    # vehicle_ids=fields.One2many(related='flat_member_ids.vehicle_ids',string='Vehicle ID')
    # parking_slot_id = fields.Many2one(related='parking.slot.parking_id',store=True)
    # , related = 'vehicle_ids.vehicle_type'
    # parking_slot_id=fields.Many2one('parking.slot')
    # parking_slot_ids = fields.One2many('parking.slot','flat_id',string='Parking Slots')
    # parking_slot_id=fields.Many2one('parking.slot',string='Parking Slot')
    # parking_slot_id = fields.Many2one('parking.slot', string='Parking Slot',store=True)
