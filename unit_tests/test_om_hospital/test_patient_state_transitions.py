# Benjamin West
from odoo.tests import common, tagged

@tagged('-standard', 'om_hospital')
class TestOmHospital(common.TransactionCase):
    def test_patient_state_transitions(self):
        """
        Test the state transitions for a patient
        """

        self.patient = self.env['hospital.patient']

        patient = self.patient.create({
            'name': 'John Doe',
            'gender': 'male',
            'age': 30,
        })

        # Test state transitions
        patient.action_confirm()
        self.assertEqual(patient.state, 'confirm', "Patient state should be 'confirm'")

        patient.action_done()
        self.assertEqual(patient.state, 'done', "Patient state should be 'done'")

        patient.action_draft()
        self.assertEqual(patient.state, 'draft', "Patient state should be 'draft'")

        patient.action_cancel()
        self.assertEqual(patient.state, 'cancel', "Patient state should be 'cancel'")
