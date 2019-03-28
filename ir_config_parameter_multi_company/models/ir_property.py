from odoo import models, api


class IrProperty(models.Model):
    _inherit = 'ir.property'

    @api.multi
    def write(self, vals):
        res = super(IrProperty, self).write(vals)
        field = self.env.ref('base.field_ir_config_parameter__value')
        self._update_db_value_website_dependent(field)
        return res
