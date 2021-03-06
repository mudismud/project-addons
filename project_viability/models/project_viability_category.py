# Copyright 2018 Gontzal Gomez - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProjectViabilityCategory(models.Model):
    _name = 'project.viability.category'
    _description = 'Viability Category'
    _order = 'code, name'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', translate=True, required=True)

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique!'),
    ]

    @api.multi
    def name_get(self):
        """ name_get() -> [(id, name), ...]

        Returns a textual representation for the records in ``self``.
        By default this is the value of the ``display_name`` field.

        :return: list of pairs ``(id, text_repr)`` for each records
        :rtype: list(tuple)
        """
        result = []
        for record in self:
            result.append((record.id,
                           '[{}] {}'.format(record.code, record.name)))
        return result
