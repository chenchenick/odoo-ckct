from odoo import fields, models
from datetime import datetime, timedelta

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Real estate property model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=datetime.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection= [('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West') ],
        help = "Shows Garden Orientation"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required=True,
        copy=False,
        default='New',
        string = 'State',
        selection= [('New', 'New'), ('Offer Received', 'Offer Received'), ('Offer Accepted', 'Offer Accepted'), ('Sold', 'Sold'), ('Canceled', 'Canceled') ],
        help = "Property state of selling"
    )
   