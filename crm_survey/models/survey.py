# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    lead_id = fields.Many2one(
        comodel_name='crm.lead', domain="[('partner_id', '=', partner_id)]",
        string='Lead')
