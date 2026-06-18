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