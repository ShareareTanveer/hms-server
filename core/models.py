from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from authentication.validators import validate_image_size

# Create your models here.
SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

 
class UserDetail(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_details')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)

class AppSettings(models.Model):
    application_title = models.CharField(max_length=255)
    address = models.TextField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    favicon = models.ImageField(
        upload_to='appsettings/', blank=True, null=True)
    logo = models.ImageField(upload_to='appsettings/', blank=True, null=True)
    language = models.CharField(max_length=10)
    time_zone = models.CharField(
        max_length=50, default=timezone.get_default_timezone_name())
    website_align = models.CharField(max_length=10)
    footer_text = models.TextField()

    def __str__(self):
        return self.application_title


class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user_details = models.OneToOneField(UserDetail, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
