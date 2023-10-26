from django.db import models
from healthcare.models import Doctor, Patient


class PatientDocument(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    prescription = models.FileField(
        upload_to='documents/prescriptions', blank=True, null=True)
    medical_report = models.FileField(
        upload_to='documents/medical_reports', blank=True, null=True)
    consent_form = models.FileField(
        upload_to='documents/consent_forms', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Patient Documents'

    def __str__(self):
        return self.patient.user_details.user.get_full_name() + ' - Documents'



class PatientCseStudy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_allergies = models.CharField(max_length=100, blank=True, null=True)
    tendency_bleed = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    high_blood_pressure = models.BooleanField(default=False)
    diabetic = models.BooleanField(default=False)
    surgery = models.BooleanField(default=False)
    accident = models.BooleanField(default=False)
    others = models.CharField(max_length=100, blank=True, null=True)
    family_medical_history = models.TextField(blank=True, null=True)
    current_medication = models.TextField(blank=True, null=True)
    female_pregnancy = models.BooleanField(default=False)
    breast_feeding = models.BooleanField(default=False)
    health_insurance = models.BooleanField(default=False)
    low_income = models.BooleanField(default=False)
    reference = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"PatientCseStudy for {self.patient}"

