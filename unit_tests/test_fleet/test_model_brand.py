# Benjamin West
from odoo.tests import common


class TestFleet(common.TransactionCase):

    def test_create_vehicle_brand_and_model(self):
        # Create a brand
        brand = self.env["fleet.vehicle.model.brand"].create({
            "name": "Nickolas",
        })
        self.assertEqual(brand.name, "Nickolas", "The vehicle brand name should be 'Nickolas'")

        # Create a model linked to the brand
        model = self.env["fleet.vehicle.model"].create({
            "brand_id": brand.id,
            "name": "Model screq",
            "vehicle_type": "car",
        })
        self.assertEqual(model.brand_id, brand, "The vehicle model should be linked to the correct brand")
        self.assertEqual(model.name, "Model screq", "The vehicle model name should be 'Model screq'")
