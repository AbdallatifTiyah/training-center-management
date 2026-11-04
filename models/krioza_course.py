from odoo import fields, models


class KriozaCourse(models.Model):
    _name = 'krioza.course'
    _description = 'Training Course'
    _order = 'name'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Code', help='Shore code, for example ODOO')
    description = fields.Text(string = 'Description')
    duration_hours = fields.Float(string='Max Seats', default=20)
