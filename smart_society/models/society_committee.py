from odoo import models, fields, api


class Committee(models.Model):
    _name = 'society.committee'
    _description = 'Committees in society'

    name = fields.Char(string='Committee Name')
    committee_name_id = fields.Many2many('res.partner',string='Committee Members',required=True)
    chairman_id = fields.Many2one('res.partner',string='Chairman')
    secretary_id = fields.Many2one('res.partner',string='Secretary')
    tower_id = fields.Many2one('society.tower',string='Tower')
    society_id=fields.Many2one(related='tower_id.society_id')


    def _create_or_update_committee_users(self):
        committee_group = self.env.ref('smart_society.group_registration_committee')
        portal_group = self.env.ref('base.group_portal')
        internal_group = self.env.ref('base.group_user')

        for record in self:
            partner_ids = []
            if record.chairman_id:
                partner_ids.append(record.chairman_id.id)
            if record.secretary_id:
                partner_ids.append(record.secretary_id.id)
            if not record.committee_name_id:
                record.committee_name_id=[(6,0,list(set(partner_ids)))]

            partners = self.env['res.partner'].browse(
                list(set(partner_ids))
            )


            # record.committee_name_id=list(set(partner_ids))
            # record.write({
            #     'committee_name_id': [(6, 0, list(set(partner_ids)))]
            # })
            print('\n\n\n\n...................................partners',partners)
            for partner in partners:
                user = self.env['res.users'].search([
                    ('partner_id', '=', partner.id)
                ], limit=1)
                if user.has_group('base.group_portal'):
                    print('\n\n\n if user .....has group..............',user.has_group('base.group_portal'))
                    print('\n\n\n..............user.....',user)

                    user.write({
                        'group_ids':[
                            (3,portal_group.id),
                            (4,internal_group.id),
                            (4,committee_group.id),
                        ]
                    })
                    print('\n\n\n if user .....has group........group_portal......',user.has_group('base.group_portal'))
                print('\n\n\n if user .....has group.........smart_society.group_registration_committee.....', user.has_group('smart_society.group_registration_committee'))
                print('\n\n\n if user .....has group.......group_user.......', user.has_group('base.group_user'))
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
                print('......................user.....',self.env['res.users'].search([]))

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._create_or_update_committee_users()
        return records

    def write(self, vals):
        res = super().write(vals)
        self._create_or_update_committee_users()
        return res







# class Committee(models.Model):
#     _name='society.committee'
#     _description='Committees in society'
#
#     name=fields.Char(string='Committee name')
#     committee_name_id=fields.Many2many('res.partner',string='Committee members',required=True)
#     chairman_id=fields.Many2one('res.partner',string='Chairman')
#     secretary_id=fields.Many2one('res.partner',string='Secretary')
#     tower_id=fields.Many2one('society.tower',string='Tower')
#     # society_id=fields.Many2one('society.setup',string='Society')
#
#     @api.onchange('committee_name_id','chairman_id','secretary_id')
#     def committee_rules(self):
#         for record in self:
#
#             if record.chairman_id:
#                 print('\n\n\n.......record.chairman_name.....',record.chairman_id)
#                 committee=self.env['res.users'].search([
#                     ('partner_id','=',record.chairman_id.id),
#
#                 ])
#                 print('\n\n\n.......committee.....',committee)
#
#                 committee.write({
#                     'group_ids': [(4,self.env.ref('smart_society.group_registration_committee').id)],
#                 })
#             if record.secretary_id:
#                 print('\n\n\n.......record.secretary_name.....',record.secretary_id)
#                 committee=self.env['res.users'].search([
#                     ('partner_id','=',record.secretary_id.id),
#
#                 ])
#                 print('\n\n\n.......committee.....',committee)
#
#                 committee.write({
#                     'group_ids': [(4, self.env.ref('smart_society.group_registration_committee').id)],
#                 })
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         resident=super().create(vals_list)
#         for record in resident:
#             check_partner = self.env['res.users'].search([
#                 ('partner_id', 'in', record.committee_name_id.ids),
#             ])
#             check_partner.write({
#                 'group_ids': [(4, self.env.ref('smart_society.group_registration_committee').id)],
#                     # 'group_ids': [(4, self.env.ref('smart_society.group_registration_user').id)],
#                 })
#             print('\n\n\n............check_partner..........', check_partner)
#             check_partner1 = self.env['res.users'].search([
#                 ('partner_id', '=', record.chairman_id.id),
#             ])
#             check_partner1.write({
#                 'group_ids': [(4, self.env.ref('smart_society.group_registration_committee').id)],
#                     # 'group_ids': [(4, self.env.ref('smart_society.group_registration_user').id)],
#                 })
#             print('\n\n\n............check_partner1..........', check_partner1)
#             check_partner2 = self.env['res.users'].search([
#                 ('partner_id', '=', record.secretary_id.id),
#             ])
#             check_partner2.write({
#                 'group_ids': [(4, self.env.ref('smart_society.group_registration_committee').id)],
#                     # 'group_ids': [(4, self.env.ref('smart_society.group_registration_user').id)],
#                 })
#             print('\n\n\n............check_partner2..........', check_partner2)
#         return resident
