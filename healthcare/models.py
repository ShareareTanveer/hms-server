from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
import string
from django.utils import timezone
from core.models import UserDetail
import string
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField

# Define choices for fields

BED_TYPE_CHOICES = (
    ('General', 'General'),
    ('ICU', 'ICU'),
    ('NICU', 'NICU'),
)


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PatientManager(models.Manager):
    def generate_unique_patient_id(self):
        while True:
            patient_id = get_random_string(
                length=5, allowed_chars=string.ascii_uppercase + string.digits)
            if not Patient.objects.filter(patient_id=patient_id).exists():
                return patient_id


class Patient(models.Model):
    user_details = models.OneToOneField(UserDetail, on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=5, unique=True, editable=False, null=True,blank=True)
    occupation = models.CharField(max_length=30)
    medical_history = models.TextField()
    status = models.BooleanField(default=True)
    # picture = models.ImageField(
    #     upload_to='photos/patients', blank=True, null=True,validators=[validate_image_size], default='avatar.webp')

    objects = PatientManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.patient_id = Patient.objects.generate_unique_patient_id()
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_details.user.get_full_name()


class Doctor(models.Model):
    user_details = models.OneToOneField(UserDetail, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    short_bio = RichTextField()
    spacialist = models.CharField(max_length=100)
    education_degree = RichTextField()
    status = models.BooleanField(default=True)
    # picture = models.ImageField(
    #     upload_to='photos/doctors', blank=True, null=True)
    visiting_fee = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user_details.user.email


class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    per_patient_time = models.PositiveIntegerField()
    available_days = models.ManyToManyField(Day, related_name='schedules')
    status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.doctor} Schedule"
    
    
    
    def get_time_slots(self,appointment_date=0):
        if appointment_date==0:
            full_start_time = datetime.combine(datetime.now().date(), self.start_time)
            full_end_time = datetime.combine(datetime.now().date(), self.end_time)
            full_per_patient_time = timedelta(minutes=self.per_patient_time)  # Assuming each appointment is 1 hour

            time_slots = []
            current_time = full_start_time

            while current_time + full_per_patient_time <= full_end_time:
                time_slots.append(current_time)
                current_time += full_per_patient_time

            available_time_slots = [time_slot.strftime("%H:%M") for time_slot in time_slots]
            return available_time_slots

        else:
            full_start_time = datetime.combine(appointment_date, self.start_time)
            full_end_time = datetime.combine(appointment_date, self.end_time)
            full_per_patient_time = timedelta(minutes=self.per_patient_time)  # Assuming each appointment is 1 hour

            time_slots = []
            current_time = full_start_time

            while current_time + full_per_patient_time <= full_end_time:
                time_slots.append(current_time)
                current_time += full_per_patient_time

            available_time_slots = [time_slot.strftime("%H:%M") for time_slot in time_slots]
            return available_time_slots


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    problem = models.TextField()

    time_alloted = models.TimeField()
    serial_no = models.IntegerField(null=True, blank=True)

    is_completed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        get_latest_by = 'created_at'

    
        
class Bed(models.Model):

    bed_type = models.CharField(max_length=50, choices=BED_TYPE_CHOICES)
    description = models.TextField()
    bed_capacity = models.PositiveIntegerField()
    charge = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bed_type} bed ({self.bed_capacity} capacity)"
    
    def is_available(self):
        now = timezone.now()
        assigned_count = self.bedassign_set.filter(status=True, discharge_date__gte=now).count()
        return assigned_count < self.bed_capacity

class BedAssign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    description = models.TextField()
    assigned_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.bed} - {self.assigned_date}"

    def is_available(self):
        now = timezone.now()
        try:
            latest_assign = self.bedassign_set.latest('assigned_date')
            if latest_assign.discharge_date is None:
                return False
            elif latest_assign.discharge_date > now:
                return True
            else:
                return False
        except BedAssign.DoesNotExist:
            return True


class BirthReport(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    delivery_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.person.name}'s Birth Report"


class DeathReport(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    place_of_death = models.CharField(max_length=255)
    cause_of_death = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.person.name}'s Death Report"
