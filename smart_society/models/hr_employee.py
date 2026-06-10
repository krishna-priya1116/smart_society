from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_type_society = fields.Selection([
        ('security', 'Security'),
        ('manager', 'Manager'),
        ('maintenance', 'Maintenance'),
    ])

    shift = fields.Selection([
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ])

    gate_number = fields.Char(
        string='Gate Number'
    )

    society_id = fields.Many2one(
        'society.setup',
        string='Society'
    )