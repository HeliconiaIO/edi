# Copyright 2022 Camptocamp SA
# @author: Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# TODO: move it to a simple python package under OCA umbrella?
{
    "name": "PDF Helper",
    "version": "14.0.2.0.1",
    "category": "Tools",
    "license": "LGPL-3",
    "summary": "Provides helpers to work w/ PDFs",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["simahawk", "alexis-via"],
    "website": "https://github.com/OCA/edi",
    "depends": [
        "base",
    ],
    "external_dependencies": {"python": ["pypdf>=3.1.0,<5.0"]},
}
