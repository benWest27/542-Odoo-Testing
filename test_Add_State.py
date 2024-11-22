# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Evan Inman
from jinja2.runtime import to_string
from odoo.tests import common
#from odoo import fields


class TestFleet(common.TransactionCase):

    def test_state_addition(self):

        try:
            self.FleetTesterBase = self.env["fleet.vehicle.state"].create({
                "name": "Test State",
            })
        except Exception as erritor:
            print("Something strange has happened: " + to_string(erritor))
        try:
            self.FleetTesterBase2 = self.env["fleet.vehicle.state"].create({
                "name": "test state",
            })
        except Exception as error:
            print("First, this should pass: " + to_string(error))
        try:
            self.FleetTesterBase3 = self.env["fleet.vehicle.state"].create({
                "name": "Test State 2",
            })
        except Exception as error2:
            print("Second, this, too, should pass: " + to_string(error2))
        try:
            self.FleetTesterBase4 = self.env["fleet.vehicle.state"].create({
                "name": "Test State",
            })
        except Exception as error3:
            print("Third, this should fail: " + to_string(error3))
