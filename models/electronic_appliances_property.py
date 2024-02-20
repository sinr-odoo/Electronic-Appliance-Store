from odoo import fields, models


class AppliancesPoperty(models.Model):
    _name = "electronic.appliance.properties"
    _description = "Electronic Appliances Properties"

    name = fields.Char(string = 'Product Name', required = True)
    brand = fields.Char(string = 'Brand', required = True)
    model_number = fields.Char(string = 'Model Number')
    description = fields.Text(string = 'Description')
    condition = fields.Selection(string = 'Condition', selection = [
        ('new', 'New'),
        ('refurbished', 'Refurbished')
    ])
    cost_price = fields.Integer(string = 'Cost Price')
    sale_price = fields.Integer(string = 'Sale Price')
    available = fields.Boolean(string = 'Available')
    date_of_availability = fields.Date(string = "Date of Availability")
    accesories = fields.Char(string = 'Accesories')
    height = fields.Float(string = 'Height')
    width = fields.Float(string = 'Width')
    length = fields.Float(string = 'Length')
    weight = fields.Float(string = 'Weight')
    warranty_info = fields.Char(string = 'Warranty Information')
    customer_id = fields.Many2many('users.details', string="customers")