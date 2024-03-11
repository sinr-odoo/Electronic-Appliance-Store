from odoo import api, fields, models

class ProductProductRent(models.Model):
    _inherit= 'product.product'

    rent = fields.Boolean()
    sale_price = fields.Integer(compute="_compute_sale_price", inverse='_inverse_sale_price')
    per_month_price = fields.Integer()
    rent_period = fields.Selection(selection= [
        ('6','6 Months'),
        ('12', '1 Year'),
        ('24', '2 years')
    ],default='6')

    @api.depends('per_month_price','rent_period','rent')
    def _compute_sale_price(self):
        for record in self:
            record.sale_price = record.per_month_price * int(record.rent_period)

    def _inverse_sale_price(self):
        for record in self:
            record.list_price = record.sale_price