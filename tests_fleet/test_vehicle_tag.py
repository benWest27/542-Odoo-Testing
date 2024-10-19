from odoo.tests import common, new_test_user

class TestFleet(common.TransactionCase):

    def test_create_vehicle_tag(self):
        
        # Ensure no tag with the same name exists
        existing_tag = self.env["fleet.vehicle.tag"].search([("name", "=", "Electric")])
        self.assertFalse(existing_tag, "The tag 'Electric' already exists. Please use a different test tag name.")

        # Create a tag
        tag_1 = self.env["fleet.vehicle.tag"].create({
            "name": "Electric",
            "color": 2,
        })
        self.assertEqual(tag_1.name, "Electric", "The vehicle tag name should be 'Electric'")
        self.assertEqual(tag_1.color, 2, "The vehicle tag color should be 2")

        # Attempt to create a duplicate tag
        with self.assertRaises(Exception, msg="Tag name should be unique"):
            self.env["fleet.vehicle.tag"].create({
                "name": "Electric",
                "color": 3,
            })
