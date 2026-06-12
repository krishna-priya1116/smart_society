from odoo import models, fields, api


class Tower(models.Model):
    _name = 'society.tower'
    _description = 'Towers in society'

    name = fields.Char(string='Tower Name', required=True)
    tower_ids = fields.One2many('society.flat', 'tower_id')
    no_of_lifts = fields.Integer(string='No of Lifts')
    stair_case = fields.Integer(string='Stair Case')
    fire_exit = fields.Integer(string='Fire Exit')
    parking_area = fields.Integer(string='Parking Area count')
    society_id = fields.Many2one('society.setup')
    vehicle_ids = fields.One2many('vehicle.registrations', 'tower_id')
    resident_id = fields.Many2one('resident.registrations')
    event_ids = fields.Many2many('event.announcement', 'tower_event_rel', 'tower_id', 'event_id', string='Events')
    # flat_count = fields.Integer(string='Flat Count')
    flat_floors = fields.Integer(string='Flat Floors')
    flat_rows_one_floor = fields.Integer(string='Flats in One Floor')
    block = fields.Selection(string='Blocks',
                             selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
                                        ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
                                        ('M', 'M'),
                                        ('N', 'N')])
    has_guesthouse = fields.Boolean(string='Has Guest House')
    guesthouse_count = fields.Integer(string='Guest House Count')
    gh_ids = fields.One2many('society.guesthouse', 'tower_id')



    @api.constrains('flat_floors', 'flat_rows_one_floor', 'has_guesthouse', 'guesthouse_count')
    def generate_flat(self):
        for record in self:
            list1 = []
            block_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

            for i in range(record.flat_rows_one_floor):
                list1.append(block_list[i])
            # record.flat_count=len(list1)
            for flat in range(record.flat_floors):
            # for flat in range(record.flat_rows_one_floor):
                print('...........flat.............', flat)
                for row in list1:
                    print('............row............', row)
                    exist_flat = self.env['society.flat'].search([
                        ('name', '=', f'{record.society_id.id}-t{record.name[-1]}-flat{flat + 101}-{row}'),
                        ('tower_id','=',record.id),
                    ])
                    # print('\n\n\n..................exist_flat..............................', exist_flat)
                    if not exist_flat:
                        print('\n\n\n...............if not exist_flat...............................', exist_flat)
                        self.env['society.flat'].create({
                            'name': f'{record.society_id}-t{record.name[-1]}-flat{flat + 101}-{row}',
                            'tower_id': record.id,
                            'floor_no': f'{flat + 1}',
                            # 'block':record.block, .tower_ids
                            'block': row,
                        })
                        print('\n\n\n record.block..................', record.block)
        for record in self:
            for gh in range(record.guesthouse_count):
                search_gh = self.env['society.guesthouse'].search([
                    ('name', '=', f't{record.name[-1]}-GuestHouse{gh + 1}'),
                    ('tower_id', '=', record.id),
                ], limit=1)
                print('\n\n\n....................search_gh........................', search_gh)
                print('\n\n\n.....................,gh...........................', gh)
                if not search_gh and record.has_guesthouse:
                    self.env['society.guesthouse'].create({
                        'name': f't{record.name[-1]}-GuestHouse{gh + 1}',
                        'tower_id': record.id,
                        'floor_number': gh+1,
                        # 'flat_type':record.
                    })
