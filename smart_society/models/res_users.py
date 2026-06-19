from odoo import models,fields,api


class ResUsers(models.Model):
    _inherit = 'res.users'

    tower_id = fields.Many2one(
        'society.tower',
        string='Tower',
        compute='_compute_tower_id',
        store=True,readonly=False
    )
    block=fields.Char(string='block')
    society_id=fields.Many2one(related='tower_id.society_id')

    @api.depends('partner_id')
    def _compute_tower_id(self):
        for user in self:
            tower = False

            # Society committee members
            committee = self.env['society.committee'].search([
                ('society_committee_members', 'in', user.id)
            ], limit=1)
            # if not committee:
            #     committee = self.env['society.committee'].search([
            #         ('committee_name_id', 'in', user.partner_id.id)
            #     ], limit=1)

            if committee:
                tower = committee.tower_id

            # Tower committee member
            if not tower:
                tower_committee = self.env['tower.committee'].search([
                    ('tower_member_id', '=', user.id)
                ], limit=1)

                if tower_committee:
                    tower = tower_committee.tower_id

            # Block committee member
            if not tower:
                block_committee = self.env['block.committee'].search([
                    ('block_member_id', '=', user.id)
                ], limit=1)

                if block_committee:
                    tower = block_committee.tower_id

            # Security
            if not tower:
                security = self.env['security.guard'].search([
                    ('security_id', '=', user.id)
                ], limit=1)

                if security:
                    tower = security.tower_id

            # Resident
            if not tower:
                resident = self.env['resident.registrations'].search([
                    ('partner_id', '=', user.partner_id.id)
                ], limit=1)

                if resident:
                    tower = resident.tower_id

            user.tower_id = tower