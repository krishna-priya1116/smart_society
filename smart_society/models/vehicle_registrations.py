from odoo import models,fields,api
import re
from odoo.exceptions import ValidationError


class VehicleRegistrations(models.Model):
    _name='vehicle.registrations'
    _description='Vehicle Registrations'

    name=fields.Char(related='vehicle_number')
    vehicle_number = fields.Char(string='Vehicle Number',required=True)
    vehicle_name = fields.Char(string='Vehicle Name')
    flat_number=fields.Many2one('society.flat',string='Flat Number')
    vehicle_type=fields.Selection(string='Vehicle Type',
                             selection=[('2wheeler','2 Wheeler'),('3wheeler','3 Wheeler'),('4wheeler','4 Wheeler'),
                                      ('other','Other')],required=True)
    color = fields.Char(string='Vehicle Color')
    resident_id=fields.Many2one('resident.registrations',string="Owner")
    tower_id=fields.Many2one('society.tower')
    parking_slot_id=fields.Many2one('parking.slot',string='Parking Slot')
    flat_id = fields.Many2one('society.flat',related='resident_id.flat_id',store=True)
    # is_inside = fields.Boolean(default=False)
    owner_id=fields.Many2one('res.users',string='Owner',default=lambda self:self.env.user)

    _sql_constraints = [('vehicle_unique','unique(vehicle_number)','Vehicle Number must be unique!')]

    @api.constrains('vehicle_number','vehicle_type')
    def vehicle_number_validation(self):
        regex=r'^[A-Z]{2}[ ]?[0-9]{2}[ ]?[A-Z]{1,2}[ ]?[0-9]{4}$'
        for record in self:
                if not record.vehicle_type=='cycle':
                    if not record.vehicle_number:
                        raise ValidationError('Enter Proper Vehicle Number')
                    else:
                        if not re.match(regex, record.vehicle_number) or not record.vehicle_number:
                            raise ValidationError('Vehicle Number Error')





