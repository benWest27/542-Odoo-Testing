# Benjamin West
from odoo.tests import common, tagged

@tagged('-standard', 'om_hospital')
class TestOmHospital(common.TransactionCase):
    def test_patient_create(self):
        """
        Test creating a new patient record with valid data
        """
        self.patient = self.env['hospital.patient']

        patient = self.patient.create({
            'name': 'John Doe',
            'gender': 'male',
            'age': 30,
            'note': 'Test patient creation',
        })

        # Verify the patient record was created successfully
        self.assertEqual(patient.name, 'John Doe', "Patient name should be 'John Doe'")
        self.assertEqual(patient.gender, 'male', "Gender should be 'male'")
        self.assertEqual(patient.age, 30, "Age should be 30")
        self.assertEqual(patient.note, 'Test patient creation', "The patient note should be 'Test patient creation'")
