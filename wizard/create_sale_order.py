from odoo import Command, fields, models

class CreateSaleOrder(models.TransientModel):
    _name='create.sale.order'
    _description= "Create Sale Order"

    customer_id = fields.Many2one('res.partner')
    quantity = fields.Integer()
    
    def create_sale_order(self):
        products = self._context.get("active_ids",[])

        self.env['sale.order'].create({
            'partner_id': self.customer_id.id,
            'order_line': [
                Command.create({
                    'product_id': products[0],
                    'product_uom_qty': self.quantity
                })
            ]
        })