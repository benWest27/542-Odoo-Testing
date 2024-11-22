# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Evan Inman
from odoo.tests import common, new_test_user
from odoo import fields


class TestFleet(common.TransactionCase):

    def test_state_addition(self):
        manager = new_test_user(self.env, "test fleet manager",
                                groups="fleet.fleet_group_manager,base.group_partner_manager")
        user = new_test_user(self.env, "test base user", groups="base.group_user")

        self.FleetTesterBase = self.env["fleet.vehicle.state"].create({
            "name": "Test State"
        })
        try:
            self.FleetTesterBase = self.env[{"fleet.vehicle.state"}].create({
                "name": "test state"
            })
        except:
            print("Should pass 1")
        try:
            self.FleetTesterBase = self.env[{"fleet.vehicle.state"}].create({
                "name": "Test State 2"
            })
        except:
            print("Should pass 2")
        try:
            self.FleetTesterBase = self.env[{"fleet.vehicle.state"}].create({
                "name": "Test State"
            })
        except:
            print("Should fail")
