from datetime import timedelta, datetime
from odoo import api,fields,models
from odoo.exceptions import ValidationError


class GuesthouseBooking(models.Model):
    _name = 'guesthouse.booking'
    _description = 'Guesthouse Booking'

    # name = fields.Char(string='Name')
    guest_house_id=fields.Many2one('society.guesthouse',string='Guest House',required=True)
    tower_id=fields.Many2one(related='guest_house_id.tower_id',store=True,readonly=False)
    member_count=fields.Integer(string='Member Count',required=True)
    total_charge=fields.Float(string='Total Charge',compute="_compute_days_booked",store=True)
    price_per_person=fields.Float(related='guest_house_id.price_per_person',string='Per Day Charge',store=True,readonly=True)
    # price_per_person
    check_in_date=fields.Datetime(string='CheckIn Date',required=True)
    check_out_date=fields.Datetime(string='CheckOut Date')
    # is_occupied=fields.Boolean(string='Is Occupied',compute='_compute_is_occupied')
    is_occupied=fields.Boolean(string='Is Occupied')
    days_booked=fields.Integer(string='Days Booked',required=True,default=1)
    booking_members_ids=fields.One2many('guesthouse.booking.members',
                                     'guesthouse_booking_id',string='Booked Members')
    members_history_ids=fields.One2many('guesthouse.members.history',
                                        'guesthouse_booking_id',string='Members History')

    # @api.onchange('days_booked', 'check_in_date', 'check_out_date', 'member_count')
    # def _compute_days_booked(self):
    #     for record in self:
    #         record.total_charge = (
    #                 record.days_booked *
    #                 record.member_count *
    #                 record.price_per_person
    #         )

    @api.depends('days_booked', 'member_count', 'price_per_person')
    def _compute_days_booked(self):
        for record in self:
            record.total_charge = (
                    record.days_booked *
                    record.member_count *
                    record.price_per_person
            )

    @api.onchange('check_in_date')
    def check_in_occupied(self):
        for record in self:
            if record.check_in_date:
                record.is_occupied=True

    def action_checkout(self):
        for record in self:
            record.write(
                {'check_out_date':datetime.today()}
            )
            print('\n\n\n............record.check_out_date...........',record.check_out_date)
            for booking_id in record.booking_members_ids:
                print('.........booking_id........',booking_id)
                print('..........member_name.......',booking_id.member_name)
                print('.........member_age........',booking_id.member_age)
                print('...........booking_id......',booking_id.member_mobile)
                print('...........emergency_number......',booking_id.emergency_number)
                print('.................record........',record.id)
                print('..............record.guest_house_id.......',record.guest_house_id)
                print('..............record.guest_house_id.id.......',record.guest_house_id.id)
                history=self.env['guesthouse.members.history'].create({
                    # 'gh_booking_member_id': booking_id,
                    'guesthouse_booking_id': record.id,
                    'guest_house_id':record.guest_house_id.id,
                    'member_name': booking_id.member_name,
                    'member_age': booking_id.member_age,
                    'member_mobile': booking_id.member_mobile,
                    'member_id_proof': booking_id.member_id_proof,
                    'emergency_number': booking_id.emergency_number,
                    'check_in_date':record.check_in_date,
                    'check_out_date':record.check_out_date,
                })
                print('\n\n\n..........history',history)
            record.write(
                {'check_out_date':False,
                 'check_in_date': datetime.today(),
                 'is_occupied':False,
                 'member_count':0}
            )
            record.booking_members_ids.unlink()


                # if history:
                #     record.is_occupied=False
                #     record.check_in_date=False
                #     record.check_out_date=False
                    # print('..............for booking_id in record.booking_members_ids...........')
                    # print('..................booking_id........',booking_id)
                    # print('...............booking_id.member_name...........', booking_id.member_name)
                    # print('.............booking_id.member_age.............', booking_id.member_age)
                    # print('................booking_id.member_mobile..........', booking_id.member_mobile)
                # self.env['guesthouse.members.history'].create({
                #
                # })

    @api.constrains('member_count','booking_members_ids')
    def check_members(self):
        for record in self:
            if record.member_count:
                count=len(record.booking_members_ids)
                if record.member_count<count or record.member_count>count:
                    print('............member count...........',count)
                    raise ValidationError('the member count and member added is different ')

class GuesthouseBookingMembers(models.Model):
    _name = 'guesthouse.booking.members'
    _description = 'Guesthouse Booking Members'

    guesthouse_booking_id = fields.Many2one('guesthouse.booking', string='Guest House')
    guest_house_id = fields.Many2one('society.guesthouse', string='Guest House')
    tower_id=fields.Many2one(related='guesthouse_booking_id.tower_id',store=True,readonly=False)
    # guest_house_id=fields.Many2one('society.guesthouse',string='Guest House')
    # tower_id=fields.Many2one(related='guest_house_id.tower_id')
    # guesthouse_booking_id = fields.Many2one('guesthouse.booking', string='Guest House')
    member_name = fields.Char(string='Member Name', required=True)
    member_age = fields.Integer(string='Member Age', required=True)
    member_mobile = fields.Char(string='Member Mobile')
    member_id_proof = fields.Char(string='Member ID Proof', required=True)
    emergency_number = fields.Char(string='Emergency Number')


class GuesthouseMemberHistory(models.Model):
    _name = 'guesthouse.members.history'
    _description = 'Guesthouse Members History'

    guesthouse_booking_id = fields.Many2one('guesthouse.booking', string='Guest House')
    # guest_house_id=fields.Many2one('society.guesthouse',string='Guest House',required=True)
    guest_house_id = fields.Many2one('society.guesthouse', string='Guest House')
    tower_id=fields.Many2one(related='guesthouse_booking_id.tower_id',store=True,readonly=False)
    check_in_date = fields.Datetime(string='Check In Date')
    check_out_date = fields.Datetime(string='Check Out Date')
    # gh_booking_member_id = fields.Many2one('guesthouse.booking.members', string='Guest House')
    member_name = fields.Char(string='Member Name', required=True)
    member_age = fields.Integer(string='Member Age', required=True)
    member_mobile = fields.Char(string='Member Mobile')
    member_id_proof = fields.Char(string='Member ID Proof', required=True)
    emergency_number = fields.Char(string='Emergency Number')



class GymBooking(models.Model):
    _name = 'gym.booking'
    _description = 'Gym Booking'

    name = fields.Char(string='Name')
    # resident_id=fields.Many2one('resident.registrations',string='Resident')
    resident_id=fields.Many2one('res.users',string='Resident')
    # flat_id=fields.Many2one(related='resident_id.flat_id',string='Flat',store=True,readonly=True)
    tower_id=fields.Many2one(related='resident_id.tower_id',string="Tower",store=True,readonly=True)
    society_id=fields.Many2one('society.setup')
    shift=fields.Selection(selection=[('morning','Morning'),('afternoon','Afternoon'),('evening','Evening'),('night','Night')])
    booked_date=fields.Datetime(string='Starting Date')
    gym_for_days=fields.Boolean(string='Gym For Days')
    gym_for_months=fields.Boolean(string='Gym For months')
    days=fields.Integer(string=' how many Days')
    months=fields.Integer(string='how many Months')
    gym_booking_charge=fields.Float(related='society_id.gym_booking_charge',string='Gym Booking Charge/day',store=True,readonly=True)
    total_amount=fields.Float(string='Total Charge' ,compute="_compute_booking_charge")
    is_occupied=fields.Boolean(string='Is Occupied')
    # slots=fields.Many2one('gym.slots',string='Slots')

    @api.depends('days', 'months', 'gym_for_days', 'gym_for_months', 'gym_booking_charge')
    def _compute_booking_charge(self):
        for record in self:
            if self.env.user.tower_id:
                print('\n\n\n....................self.env.user.tower_id.....................',self.env.user.tower_id)
                record.tower_id=self.env.user.tower_id
            record.name=record.id
            record.society_id=record.tower_id.society_id
            amount = 0.0
            if record.gym_for_days:
                amount = record.gym_booking_charge * record.days
            elif record.gym_for_months:
                record.days = 30
                amount = record.gym_booking_charge * record.days
            print('\n\\n\n')
            record.total_amount = amount

    # @api.depends('days','months')
    # def _compute_booking_charge(self):
    #     for record in self:
    #         print('\n\n\n.......record.tower_id.society_id....',record.tower_id.society_id)
    #         record.society_id=record.tower_id.society_id
    #         print('\n\n\n.......record.society_id....',record.society_id)
    #
    #         if record.gym_for_days:
    #             print('..........booking_charge_id........',record.gym_booking_charge)
    #             record.total_amount=record.gym_booking_charge*record.days
    #         elif record.gym_for_months:
    #             print('..........booking_charge_id........',record.gym_booking_charge)
    #             record.days=30
    #             record.total_amount=record.gym_booking_charge*record.days
    #
    # @api.depends('booked_date','days','months')
    # def _compute_booking_occupied(self):
    #     for record in self:
    #         if record.days:
    #             expires =record.days
    #             print('\n\n\n....expires......',expires)
    #             valid_days=record.booked_date+timedelta(days=expires)
    #             print('\n\n\n..valid_days..expires......',expires)
    #             print('\n\n\n...valid_days......',valid_days)
    #             print('\n\n\n....booked_date......',record.booked_date)




class ClubhouseBooking(models.Model):
    _name = 'clubhouse.booking'
    _description = 'Clubhouse Booking'

    name=fields.Char(string='Name')
    resident_id=fields.Many2many('res.users',string='Resident ID')
    tower_id=fields.Many2one(related='resident_id.tower_id')
    society_id=fields.Many2one('society.setup')
    cbh_booking_charge_id=fields.Float(related='society_id.cbh_booking_charge',string='Clubhouse Booking Charge',store=True,readonly=True)
    total_charge=fields.Float(string='Total charge',compute="_compute_cbh_booking_charge")
    # price_per_person=fields.Float(related='society_id.cbh_booking_charge')

    # @api.depends('society_id.cbh_booking_charge','resident_id')
    # def _compute_cbh_booking_charge(self):
    #     for record in self:
    #         record.society_id=record.tower_id.society_id
    #         resident_list = []
    #         if record.resident_id:
    #             resident_list.append(record.resident_id)
    #         print('.....len(resident_list).....',len(resident_list))
    #         print('....cbh_booking_charge_id....',record.cbh_booking_charge_id)
    #         record.total_charge=len(resident_list)*record.cbh_booking_charge_id

    @api.depends('society_id', 'resident_id')
    def _compute_cbh_booking_charge(self):
        for record in self:
            record.society_id = record.tower_id.society_id
            if self.env.user.tower_id:
                print('\n\n\n....................self.env.user.tower_id.....................',self.env.user.tower_id)
                record.tower_id=self.env.user.tower_id
            resident_count = len(record.resident_id)
            record.total_charge = resident_count * record.cbh_booking_charge_id









    # @api.model
    # def write(self, vals):
    #     # Save history before writing changes
    #     for record in self:
    #         print('\n\n\n..........record.......',record)
    #         self.env['guesthouse.members.history'].create({
    #             'guesthouse_booking_id': record.guesthouse_booking_id,
    #             'member_name': record.member_name,
    #             'member_age': record.member_age,
    #             'member_mobile': record.member_mobile,
    #             'member_id_proof': record.member_id_proof,
    #             'emergency_number': record.emergency_number,
    #         })
    #         print('\n\n\n.........after create.......',record)
    #     return super('guesthouse.booking.members', self).write(vals)

