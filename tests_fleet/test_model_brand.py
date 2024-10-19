from odoo.tests import common


class TestFleet(common.TransactionCase):

    def test_create_vehicle_brand_and_model(self):
        # Create a brand
        brand = self.env["fleet.vehicle.model.brand"].create({
            "name": "Tesla",
        })
        self.assertEqual(brand.name, "Tesla", "The vehicle brand name should be 'Tesla'")

        # Create a model linked to the brand
        model = self.env["fleet.vehicle.model"].create({
            "brand_id": brand.id,
            "name": "Model S",
            "vehicle_type": "car",
        })
        self.assertEqual(model.brand_id, brand, "The vehicle model should be linked to the correct brand")
        self.assertEqual(model.name, "Model S", "The vehicle model name should be 'Model S'")
