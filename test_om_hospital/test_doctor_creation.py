from odoo.tests.common import TransactionCase

class TestOmHospital(TransactionCase):

    def setUp(self):
        super(TestOmHospital, self).setUp()
        self.doctor = self.env['hospital.doctor'].create({
            'doctor_name': 'Dr. John Doe',
            'age': 45,
            'gender': 'male'
        })

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.doctor_name, 'Dr. John Doe', "Doctor name should be 'Dr. John Doe'")
        self.assertEqual(self.doctor.age, 45, "Doctor age should be 45")
        self.assertEqual(self.doctor.gender, 'male', "Doctor gender should be 'male'")
