from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.validators import validate_image_size


ROLES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
        ('HR', 'Human Resources'),
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
        ('ACCOUNTANT', 'Accountant'),
        ('RECEPTIONIST', 'Receptionist'),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, max_length=50)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    role = models.CharField(max_length=20, choices=ROLES, default='USER')
    picture = models.ImageField(
        upload_to='photos/users', blank=True, null=True,validators=[validate_image_size], default='avatar.webp')


    def save(self, *args, **kwargs):
        if self.role == 'ADMIN':
            self.is_staff = True
            self.is_superuser = True
        elif self.role == 'DOCTOR':
            # Define custom permissions for doctor role here
            pass
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
