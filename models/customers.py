from odoo import api,fields, models
from dateutil.relativedelta import relativedelta

class Customers(models.Model):
    _name = 'customers'
    _description = "Customers"

    user_id = fields.Many2one('res.users')
    product_id = fields.Many2one('product.product')
    quantity = fields.Integer()
    order_date = fields.Datetime()
    deadline_date = fields.Datetime(compute='_compute_deadline', store=True)

    @api.depends('order_date', 'quantity')
    def _compute_deadline(self):
        for record in self:
            if(record.product_id.rent):
                record.deadline_date = record.order_date + relativedelta(months=record.quantity)
            else:
                record.deadline_date = False


    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.user_id.name} ({record.product_id.model_number})"