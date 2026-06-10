from odoo import models, fields,api


class ResUsers(models.Model):
    _inherit = 'res.users'

    resident_id = fields.Many2one( 'resident.registrations',string='Resident')
    security_id=fields.Many2one( 'security.guard',string='Security')
    committee_id=fields.Many2one( 'society.committee',string='Committee')
    flat_id = fields.Many2one('society.flat',string='Flat')
    tower_id = fields.Many2one('society.tower',string='Tower')
    vehicle_ids = fields.One2many('vehicle.registrations','owner_id',string='Vehicles')
    complaint_ids = fields.One2many('complaint.desk','user_id',string='Complaints')
