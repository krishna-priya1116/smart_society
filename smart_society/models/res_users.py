from odoo import models, fields,api


# class ResUsers(models.Model):
#     _inherit = 'res.users'
#
#     resident_id = fields.Many2one( 'resident.registrations',string='Resident')
#     security_id=fields.Many2one( 'security.guard',string='Security')
#     committee_id=fields.Many2one( 'society.committee',string='Committee')
#     flat_id = fields.Many2one('society.flat',string='Flat')
#     tower_id = fields.Many2one('society.tower',string='Tower')
#     vehicle_ids = fields.One2many('vehicle.registrations','owner_id',string='Vehicles')
#     complaint_ids = fields.One2many('complaint.desk','user_id',string='Complaints')


from odoo import models, fields, api
from odoo.api import readonly


class ResUsers(models.Model):
    _inherit = 'res.users'

    tower_id = fields.Many2one(
        'society.tower',
        string='Tower',
        compute='_compute_tower_id',
        store=True,readonly=False
    )

    society_id=fields.Many2one(related='tower_id.society_id')

    @api.depends('partner_id')
    def _compute_tower_id(self):
        for user in self:
            tower = False

            # Committee user
            committee = self.env['society.committee'].search([
                '|',
                ('chairman_id', '=', user.partner_id.id),
                ('secretary_id', '=', user.partner_id.id),
            ], limit=1)

            if not committee:
                committee = self.env['society.committee'].search([
                    ('committee_name_id', 'in', user.partner_id.id)
                ], limit=1)

            if committee:
                tower = committee.tower_id

            # Security user
            if not tower:
                security = self.env['security.guard'].search([
                    ('security_id', '=', user.partner_id.id)
                ], limit=1)

                if security:
                    tower = security.tower_id

            if not tower:
                resident=self.env['resident.registrations'].search([
                    ('partner_id','=',user.partner_id.id)
                ],limit=1)
                if resident:
                    tower=resident.tower_id

            user.tower_id = tower
