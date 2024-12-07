# Evan Inman

from odoo.tests import common, tagged

@tagged('-standard', 'om_hospital')
class TestOmHospital(common.TransactionCase):
    def test_cancel_appointment(self):
        # Adds in a patient, then a doctor, and finally an appointment using those test pieces
        try:
            self.patient = self.env['hospital.patient']
            patient = self.patient.create({
                'name': 'test patient',
                'age': 23,
                'gender': 'male',
            })
            self.doctor = self.env['hospital.doctor']
            doctor = self.doctor.create({
                'doctor_name': 'test doctor',
                'age': 30,
                'gender': 'female',
            })
            self.appointment = self.env['hospital.appointment']
            appointment = self.appointment.create({
                'name': 'test appointment',
                'patient_id': patient.id,
                'age': 23,
                'doctor_id': doctor.id,
                'gender': 'male',
                'state': 'draft'
            })
            # Calls the appointment cancel function
            appointment.action_cancel()

            self.assertEqual(appointment.state, 'cancel', "Could not cancel.")
        except Exception as problem:
            print(problem)
        else:
            print(appointment.state)

