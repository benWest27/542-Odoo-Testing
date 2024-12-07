from odoo.tests import common

class TestFleet(common.TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestFleet, cls).setUpClass()
        cls.state_1 = cls.env['fleet.vehicle.state'].create({
            'name': 'Operational',
            'sequence': 10,
        })

    def test_vehicle_state_creation(self):
        self.assertEqual(self.state_1.name, 'Operational', "The state name should be 'Operational'")
        self.assertEqual(self.state_1.sequence, 10, "The sequence should be 10")

    def test_unique_state_name(self):
        with self.assertRaises(Exception, msg="State name should be unique"):
            self.env['fleet.vehicle.state'].create({
                'name': 'Operational',  
                'sequence': 20,
        })
