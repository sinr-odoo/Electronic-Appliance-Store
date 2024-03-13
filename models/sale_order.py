from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for order in self.order_line: 

            existing_record = self.env['customers'].search([('product_id', '=', order.product_id.id),
            ('user_id','=',self.partner_id.user_id.id)])

            if(existing_record):
                existing_record.write({
                    'quantity': existing_record.quantity + order.product_uom_qty,
                    'order_date': self.date_order
                })        
            else:
                self.env['customers'].create({
                    'product_id': order.product_id.id,
                    'user_id': self.partner_id.user_id.id,
                    'quantity': order.product_uom_qty,
                    'order_date': self.date_order
                })

        return super().action_confirm()