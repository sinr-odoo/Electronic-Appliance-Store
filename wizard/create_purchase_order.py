from odoo import Command, fields, models

class CreatePurchaseOrder(models.TransientModel):
    _name= "create.purchase.order"
    _description= "Create Purchase Order"

    vendor_id = fields.Many2one('res.partner')
    quantity = fields.Integer()

    def create_purchase_order(self):
        products = self._context.get("active_ids",[])

        self.env['purchase.order'].create({
            'partner_id': self.vendor_id.id,
            'order_line': [
                Command.create({
                    'product_id': products[0],
                    'product_qty': self.quantity
                })
            ]
        })