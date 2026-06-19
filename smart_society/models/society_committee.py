from odoo import models, fields, api


class Committee(models.Model):
    _name = 'society.committee'
    _description = 'Committee of society'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    society_id = fields.Many2one('society.setup')
    chairman_id = fields.Many2one('res.users', string="Chairman")
    secretary_id = fields.Many2one('res.users', string="Secretary")
    treasurer_id = fields.Many2one('res.users', string="Treasurer")
    tower_committee_ids = fields.One2many('tower.committee', 'society_committee_id',
                                          string='Tower Committee')
    society_committee_history_ids = fields.One2many('society.committee.history', 'society_committee_id',
                                                    string='Society Committee History')
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')
    society_committee_members=fields.Many2many('res.users',string='Committee Members',
                                               compute='_compute_committee_members',store=True)
    society_complaints_history_ids=fields.One2many('complaint.desk','society_committee_id',string='Complaints')

    #         committee_group = self.env.ref('smart_society.group_registration_committee')
    #         portal_group = self.env.ref('base.group_portal')
    #         internal_group = self.env.ref('base.group_user')
    @api.depends('chairman_id','secretary_id','treasurer_id')
    def _compute_committee_members(self):
        for record in self:
            print('\n\n\n........record...', record)
            member=(record.chairman_id | record.secretary_id | record.treasurer_id)
            record.society_committee_members = member

    def action_assign_committee(self):
        for record in self:
            committee_group=self.env.ref('smart_society.group_registration_committee')
            portal_group=self.env.ref('base.group_portal')
            if record.society_committee_members:
                record.society_committee_members.write({
                    'group_ids': [
                        (3, portal_group.id),
                        (4, committee_group.id),
                        # (4,internal_group.id),
                    ]
                })

    def action_new_society_committee(self):
        for record in self:
            committee_group=self.env.ref('smart_society.group_registration_committee')
            portal_group=self.env.ref('base.group_portal')
            # internal_group=self.env.ref('base.group_user')

            print('\n\n\n........record...',record)
            self.env['society.committee.history'].create({
                'name':record.name,
                'society_id':record.society_id.id,
                'chairman_id':record.chairman_id.id,
                'secretary_id':record.secretary_id.id,
                'treasurer_id':record.treasurer_id.id,
                'date_from':record.date_from,
                'date_to':fields.Date.today(),
                'society_committee_id':record.id,
            })
            members = record.society_committee_members
            if members:
                members.write({
                    'group_ids': [
                        (3, committee_group.id),
                        # (3, internal_group.id),
                        (4, portal_group.id),
                    ]
                })

            record.write({
                'chairman_id': False,
                'secretary_id': False,
                'treasurer_id': False,
                'date_from': fields.Date.today(),
                'date_to': False,
                # 'society_committee_members': False,
            })


class CommitteeHistory(models.Model):
    _name = 'society.committee.history'
    _description = 'Society Committee History'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    society_id = fields.Many2one('society.setup')
    society_committee_id = fields.Many2one('society.committee')
    chairman_id = fields.Many2one('res.users', string="Chairman")
    secretary_id = fields.Many2one('res.users', string="Secretary")
    treasurer_id = fields.Many2one('res.users', string="Treasurer")
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')


class TowerCommittee(models.Model):
    _name = 'tower.committee'
    _description = 'Tower Committees'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    tower_member_id = fields.Many2one('res.users', string='Tower Committee Member')
    tower_id = fields.Many2one('society.tower', string='Tower')
    print('\n\n...........tower_id.......',tower_id)
    society_id=fields.Many2one(related='tower_id.society_id')
    print('\n\n\n.....society_id.......',society_id)
    society_committee_id = fields.Many2one('society.committee', string="Society Committee")
    block_member_ids = fields.One2many('block.committee', 'tower_committee_id'
                                       , string='Block Committee')
    tower_committee_history_ids = fields.One2many('tower.committee.history', 'tower_committee_id',
                                                  string='Tower Committee History')
    tower_complaints_history_ids=fields.One2many('complaint.desk','tower_committee_id',string='Complaints')

    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')


    def action_assign_tower_committee(self):
        for record in self:
            committee_group=self.env.ref('smart_society.group_registration_tower_committee')
            portal_group=self.env.ref('base.group_portal')
            if record.tower_member_id:
                record.tower_member_id.write({
                    'group_ids': [
                        (3, portal_group.id),
                        (4, committee_group.id),
                        # (4,internal_group.id),
                    ]
                })

    def action_new_tower_committee(self):
        for record in self:
            committee_group = self.env.ref('smart_society.group_registration_tower_committee')
            portal_group = self.env.ref('base.group_portal')
            print('\n\n\n........record...', record)
            self.env['tower.committee.history'].create({
                'name': record.name,
                'tower_member_id': record.tower_member_id.id,
                'tower_id': record.tower_id.id,
                'society_committee_id': record.society_committee_id.id,
                'date_from': record.date_from,
                'date_to': fields.Date.today(),
                'tower_committee_id': record.id,
            })

            members = record.tower_member_id
            if members:
                members.write({
                    'group_ids': [
                        (3, committee_group.id),
                        # (3, internal_group.id),
                        (4, portal_group.id),
                    ]
                })

            record.write({
                'tower_member_id':False,
                'date_from':fields.Date.today(),
                'date_to':False,
            })


class TowerCommitteeHistory(models.Model):
    _name = 'tower.committee.history'
    _description = 'Tower Committees History'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    tower_member_id = fields.Many2one('res.users', string='Tower Committee Member')
    tower_id = fields.Many2one('society.tower', string='Tower')
    society_committee_id = fields.Many2one('society.committee', string="Society Committee")
    tower_committee_id = fields.Many2one('tower.committee', string="Tower Committee")
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')


class BlockCommittee(models.Model):
    _name = 'block.committee'
    _description = 'Block Committees'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    block_member_id = fields.Many2one('res.users', string='Block Committee Member')
    tower_committee_id = fields.Many2one('tower.committee', string='Tower Committee')
    tower_id = fields.Many2one(related='tower_committee_id.tower_id', string='Tower', store=True)
    block = fields.Selection(string='Blocks',
                             selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
                                        ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
                                        ('M', 'M'),
                                        ('N', 'N')])
    block_committee_history_ids = fields.One2many('block.committee.history', 'block_committee_id',
                                                 string='Block Committee History')

    block_complaints_history_ids=fields.One2many('complaint.desk','block_committee_id',string='Complaints')
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')



    def action_assign_block_committee(self):
        for record in self:
            committee_group=self.env.ref('smart_society.group_registration_block_committee')
            portal_group=self.env.ref('base.group_portal')
            if record.block_member_id:
                record.block_member_id.write({
                    'group_ids': [
                        (3, portal_group.id),
                        (4, committee_group.id),
                        # (4,internal_group.id),
                    ]
                })

    def action_new_block_committee(self):
        for record in self:
            committee_group=self.env.ref('smart_society.group_registration_block_committee')
            portal_group=self.env.ref('base.group_portal')
            print('\n\n\n........record...', record)
            self.env['block.committee.history'].create({
                'name':record.name,
                'block_member_id':record.block_member_id.id,
                'tower_committee_id':record.tower_committee_id.id,
                'tower_id':record.tower_id.id,
                'block':record.block,
                'block_committee_id':record.id,
                'date_from':record.date_from,
                'date_to':fields.Date.today(),
            })

            members = record.block_member_id
            if members:
                members.write({
                    'group_ids': [
                        (3, committee_group.id),
                        # (3, internal_group.id),
                        (4, portal_group.id),
                    ]
                })
            record.write({
                'block_member_id':False,
                'date_from':fields.Date.today(),
                'date_to':False,
            })


class BlockCommitteeHistory(models.Model):
    _name = 'block.committee.history'
    _description = 'Block Committees History'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    block_member_id = fields.Many2one('res.users', string='Block Committee Member')
    tower_committee_id = fields.Many2one('tower.committee', string='Tower Committee')
    tower_id = fields.Many2one(related='tower_committee_id.tower_id', string='Tower', store=True)
    block_committee_id = fields.Many2one('block.committee', string='Block Committee')
    block = fields.Selection(string='Blocks',
                             selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
                                        ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
                                        ('M', 'M'),('N', 'N')])

    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')









# class Committee(models.Model):
#     _name = 'society.committee'
#     _description = 'Committees in society'
#
#     name = fields.Char(string='Committee Name')
#     committee_name_id = fields.Many2many('res.partner',string='Committee Members',required=True)
#     chairman_id = fields.Many2one('res.partner',string='Chairman')
#     secretary_id = fields.Many2one('res.partner',string='Secretary')
#     tower_id = fields.Many2one('society.tower',string='Tower')
#     society_id=fields.Many2one(related='tower_id.society_id')
#
#
#     def _create_or_update_committee_users(self):
#         committee_group = self.env.ref('smart_society.group_registration_committee')
#         portal_group = self.env.ref('base.group_portal')
#         internal_group = self.env.ref('base.group_user')

# for record in self:
#     partner_ids = []
#     if record.chairman_id:
#         partner_ids.append(record.chairman_id.id)
#     if record.secretary_id:
#         partner_ids.append(record.secretary_id.id)
#     if not record.committee_name_id:
#         record.committee_name_id=[(6,0,list(set(partner_ids)))]
#
#     partners = self.env['res.partner'].browse(
#         list(set(partner_ids))
#     )


# record.committee_name_id=list(set(partner_ids))
# record.write({
#     'committee_name_id': [(6, 0, list(set(partner_ids)))]
# })
# print('\n\n\n\n...................................partners',partners)
# for partner in partners:
#     user = self.env['res.users'].search([
#         ('partner_id', '=', partner.id)
#     ], limit=1)
#     if user.has_group('base.group_portal'):
#         print('\n\n\n if user .....has group..............',user.has_group('base.group_portal'))
#         print('\n\n\n..............user.....',user)
#
#         user.write({
#             ' s':[
#                 (3,portal_group.id),
#                 (4,internal_group.id),
#                 (4,committee_group.id),
#             ]
#         })
#         print('\n\n\n if user .....has group........group_portal......',user.has_group('base.group_portal'))
#     print('\n\n\n if user .....has group.........smart_society.group_registration_committee.....', user.has_group('smart_society.group_registration_committee'))
#     print('\n\n\n if user .....has group.......group_user.......', user.has_group('base.group_user'))
# if not user:
#     self.env['res.users'].create({
#         'name': partner.name,
#         'login': partner.email,
#         'email': partner.email,
#         'partner_id': partner.id,
#         'password': f'{partner.name.replace(" ", "")}1234',
#         'group_ids': [
#             (4, committee_group.id),
#             # (4, self.env.ref('base.group_portal').id),
#         ],
#     })
# print('......................user.....',self.env['res.users'].search([]))
#
# @api.model_create_multi
# def create(self, vals_list):
#     records = super().create(vals_list)
#     records._create_or_update_committee_users()
#     return records
#
# def write(self, vals):
#     res = super().write(vals)
#     self._create_or_update_committee_users()
#     return res
