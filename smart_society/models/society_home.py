from odoo import api, fields, models, exceptions


class SocietyHome(models.Model):
    _name = 'society.home'
    _description = 'Society Home Page'

    user_id = fields.Many2one('res.users')
    security_id = fields.Many2one('security.guard')
    committee_name_id = fields.Many2one('society.committee')
    secretary_name_id = fields.Many2one('society.secretary')

    # events,notice,complaints
    def get_dashboard_data(self):
        pass








