# Copyright 2018 Gontzal Gomez - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.tests import common


class TestProjectIdea(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestProjectIdea, cls).setUpClass()
        cls.product = cls.env['product.product'].create({
            'name': 'Test Product',
        })
        cls.project = cls.env['project.project'].create({
            'name': 'Test Project',
        })
        cls.material_obj = cls.env['project.idea.resource.material']

    def test_project_idea_material_onchange(self):
        material = self.material_obj.create({
            'project_id': self.project.id,
            'product_id': self.product.id,
        })
        self.assertFalse(material.product_name)
        material.onchange_product_id()
        self.assertEquals(material.product_name,
                          material.product_id.name)
