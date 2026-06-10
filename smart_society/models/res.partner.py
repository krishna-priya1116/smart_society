from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_resident = fields.Boolean(string='Resident')
    is_committee = fields.Boolean(string='Committee')
    is_security = fields.Boolean(string='Security')
    aadhaar_number = fields.Char(string='Aadhaar Number')
    flat_id = fields.Many2one('society.flat',string='Flat')
    vehicle_count = fields.Integer(string='Vehicle Count')