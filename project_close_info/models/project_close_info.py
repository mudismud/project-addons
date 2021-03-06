# Copyright 2018 Gontzal Gomez - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProjectCloseInfo(models.Model):
    _inherit = 'project.project'

    tech_close = fields.Boolean(string='Technical Closing')
    tech_date = fields.Date(string='Technical Closing Date')
    tech_user = fields.Many2one(
        string='Technical Closing User', comodel_name='res.users')
    tech_file = fields.Binary(string='Technical Closing File')
    economic_close = fields.Boolean(string='Economic Closing')
    economic_date = fields.Date(string='Economic Close Date')
    economic_user = fields.Many2one(
        string='Economic Closing User', comodel_name='res.users')
    economic_file = fields.Binary(string='Economic Closing File')
