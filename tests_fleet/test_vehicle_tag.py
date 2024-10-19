from odoo.tests import common


class TestFleet(common.TransactionCase):

    def test_create_vehicle_tag(self):
        
        # Ensure no tag with the same name exists
        existing_tag = self.env["fleet.vehicle.tag"].search([("name", "=", "test Electric")])
        self.assertFalse(len(existing_tag) > 0, "The tag 'test Electric' already exists. Please use a different test tag name.")

        # Create a tag
        tag_1 = self.env["fleet.vehicle.tag"].create({
            "name": "test Electric",
            "color": 2,
        })
        self.assertEqual(tag_1.name, "test Electric", "The vehicle tag name should be 'test Electric'")
        self.assertEqual(tag_1.color, 2, "The vehicle tag color should be 2")

