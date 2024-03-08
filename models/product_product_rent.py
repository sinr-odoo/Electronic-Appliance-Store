from odoo import api, fields, models

class ProductProductRent(models.Model):
    _inherit= 'product.product'

    available = fields.Boolean(string = 'Available')
    date_of_availability = fields.Date(string = "Date of Availability")
    accesories = fields.Char(string = 'Accesories')
    height = fields.Float(string = 'Height')
    width = fields.Float(string = 'Width')
    length = fields.Float(string = 'Length')
    weight = fields.Float(string = 'Weight')
    customer_ids = fields.Many2many('res.users')
    vendor_ids = fields.Many2many('res.partner')
    list_price = fields.Integer(compute="_compute_sale_price")
    per_month_price = fields.Integer(required=True)
    rent_period = fields.Selection(selection= [
        ('6','6 Months'),
        ('12', '1 Year'),
        ('24', '2 years')
    ],default='6')

    @api.depends('cost_price','rent_period')
    def _compute_sale_price(self):
        for record in self:
            record.sale_price = record.per_month_price * ord(record.rent_period)