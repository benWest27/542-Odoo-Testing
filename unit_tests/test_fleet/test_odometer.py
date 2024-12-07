# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.'
# CPSC 542 - 2 - Fleet test cases for unit test.
# Israel Garcia Figueroa 8371150
from odoo.tests import common, new_test_user
import unittest

class TestFleet(common.TransactionCase):
    #print("testing odomemter test cases")
    def setUp(self):
        super(TestFleet,self).setUp()
        # manger status for creating a new vechile
        self.manager = new_test_user(self.env, "test fleet manager",
                                groups="fleet.fleet_group_manager,base.group_partner_manager")

        # make and model of the car
        self.brand = self.env["fleet.vehicle.model.brand"].create({
            "name": "Audi",
        })
        self.model = self.env["fleet.vehicle.model"].create({
            "brand_id": self.brand.id,
            "name": "A3",
        })

        self.car_1 = self.env['fleet.vehicle'].create({
            "model_id" :self.model.id,
            "odometer_count": -1
        })
        self.car_2 = self.env['fleet.vehicle'].create({
            "model_id" :self.model.id,
            "odometer_count": "abc"
        })
        self.car_3 = self.env['fleet.vehicle'].create({
            "model_id" :self.model.id,
            "odometer_count": 1000000
        })


    # Testing negative values - test 1
    def test_negtive(self):
        try:
            self.env['fleet.vehicle.odometer'].create({
                'vehicle_id': self.car_1.id,
                'value': self.car_1.odometer_count,
            })
            assert (self.car_1.odometer_count < 0)
            print(self.car_1.odometer_count)
        except AssertionError:
            print("Negative value taken: Failed")

    #testing non numbers - test 2
    def test_numeric(self):
        try:
            # Attempt to create an odometer record
            self.env['fleet.vehicle.odometer'].create({
                'vehicle_id': self.car_2.id,
                'value': self.car_2.odometer_count,
            })

            # Check if odometer_count is a valid number (int or float)
            assert( isinstance(self.car_2.odometer_count, (int, float)))

        except AssertionError:
            print("Numeric value not taken: Failed")

    # postive test case -test 3
    def test_inBound(self):
        try:
            print("testing negative value")
            self.env['fleet.vehicle.odometer'].create({
                'vehicle_id': self.car_3.id,
                'value': self.car_3.odometer_count,
            })
            assert( isinstance(self.car_3.odometer_count, (int, float)))
        except AssertionError:
            print("value is no in bound : Failed")



