from odoo.tests import common

class TestFleet(common.TransactionCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestFleet, cls).setUpClass()
        cls.service_type_1 = cls.env['fleet.service.type'].create({
            'name': 'Oil Change',
            'category': 'service',
        })

    def test_service_type_creation(self):
        self.assertEqual(self.service_type_1.name, 'Oil Change', "The service type name should be 'Oil Change'")
        self.assertEqual(self.service_type_1.category, 'service', "The category should be 'service'")

    def test_invalid_category(self):
        with self.assertRaises(Exception, msg="Category should be either 'contract' or 'service'"):
            self.env['fleet.service.type'].create({
                'name': 'Invalid Service',
                'category': 'invalid_category',
            })
