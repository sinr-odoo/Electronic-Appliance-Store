from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit= 'product.product'

    brand = fields.Char(string = 'Brand', default=None)
    model_number = fields.Char(string = 'Model Number')
    condition = fields.Selection(string = 'Condition', selection = [
        ('new', 'New'),
        ('refurbished', 'Refurbished')
    ])
    available = fields.Boolean(string = 'Available')
    date_of_availability = fields.Date(string = "Date of Availability")
    accesories = fields.Char(string = 'Accesories')
    height = fields.Float(string = 'Height')
    width = fields.Float(string = 'Width')
    length = fields.Float(string = 'Length')
    weight = fields.Float(string = 'Weight')
    warranty_info = fields.Char(string = 'Warranty Information')
    customer_ids = fields.One2many('customers', 'product_id')
    vendor_ids = fields.Many2many('res.partner')

    @api.depends("product_tmpl_id.write_date")
    def _compute_write_date(self):
        for record in self:
            record.write_date = record.write_date or self.env.cr.now()