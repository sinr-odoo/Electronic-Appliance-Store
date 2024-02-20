from odoo import fields, models

class Users(models.Model):
    _name = "users.details"
    _description = "users"

    first_name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name",required=True)
    address = fields.Text(required=True)

    product_id = fields.Many2many('electronic.appliance.properties',string="Products")