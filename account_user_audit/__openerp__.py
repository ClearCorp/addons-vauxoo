# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: Hugo Francisco Adan Oliva (hugo@vauxoo.com)
############################################################################
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

{
    "name": "Add Read-Only Accounting Group",
    "version": "0.1",
    "author": "Vauxoo",
    "category": "Generic Modules",
    "description": """
This module adds the following features:
========================================

* Odoo does not come with a read-only accountant group out of the box, which
is inconvenient when you need to have an external accountant go through your
accounting records in Odoo.  This module adds a group 'Auditor Read-Only' so
it's easy to grant an external accountant access to your Odoo system.
* This group inherits the group 'Employee', thus minimum level of
create/write/delete rights will be granted for some non-accounting related
models.
""",
    "website": "http://www.vauxoo.com",
    "license": "",
    "depends": [
        "account_asset",
        "ifrs_report",
    ],
    "demo": [],
    "data": [
        "security/account_user_group.xml",
        'security/ir.model.access.csv',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "active": False
}
