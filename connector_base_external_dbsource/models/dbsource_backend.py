# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models, api, _


class DbsourceBackend(models.Model):
    """Dbsource Backend"""

    _name = 'dbsource.backend'
    _description = _(__doc__)
    _inherit = 'connector.backend'

    _backend_type = 'dbsource'

    @api.model
    def _select_versions(self):
        """ Available versions

        Can be inherited to add custom versions.
        """
        return [('10', 'Version 1.0'),]

    version = fields.Selection(
        selection='_select_versions',
        string='Version',
        required=True,
    )

    dbsource_id = fields.Many2one(
        'base.external.dbsource',
        string='DB Source')

    default_lang_id = fields.Many2one(
        'res.lang',
        string='Default Language',
    )
