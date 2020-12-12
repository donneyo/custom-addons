from collections import namedtuple
import json
import time

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare
from odoo.addons.procurement.models import procurement
from odoo.exceptions import UserError

class Stock(models.Model):
    _name = "stock"

    product_id = fields.Many2one('product.product', ondelete='set null', string="Product", index=True)
    collected_id = fields.Char (string="Collected By", index=True)
    quantity_id = fields.Integer('Quatity', index=True)
    quantity_left_id = fields.Integer('Quatity Left', index=True)
    collected_date = fields.Datetime( 'Date collected',  index=True)
    date_returned = fields.Datetime( 'Date returned',  index=True)