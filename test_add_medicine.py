from odoo.tests import common, tagged

@tagged('-standard', 'om_hospital')
class TestOmHospital(common.TransactionCase):
    def test_add_medicine(self):
        # Attempts to add medicine
        try:
            self.appointment = self.env['appointment.prescription.lines']
            appointment = self.appointment.create({
                'name': 'Diphenhydramine',
                'qty': '90',
            })
            self.assertEqual(appointment.name, 'Diphenhydramine', "Should be bene")
        except Exception as problem:
            print(problem)
        else:
            print("prescription is good")
