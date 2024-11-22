from odoo.tests import common, tagged

@tagged('-standard', 'om_hospital')
class TestOmHospital(common.TransactionCase):
    def test_add_medicine(self):
        # Attempts to add medicine to a patient
        '''
        self.appointment = self.env['appointment.prescription.lines']
        appointment = self.appointment.create({
            'name': 'Diphenhydramine',
            'qty': '90'
        })

        self.assertEquals(appointment.name, 'Diphenhydramin', "Should be bene")
        '''
        self.appointment = self.env['hospital.appointment']
        appointment = self.appointment.create({
            'name': 'Franklin',
            'patient_id': 4,
            'age': 12,
            'doctor_id': 1,

        })

        self.assertEquals(appointment.age, 'Franklin', "Frankyboi")
