from django.contrib import admin
from .models import Department, Doctor, Day, Schedule, Appointment, Bed, BedAssign, BirthReport, DeathReport
from hms.admin import admin_site


@admin.register(Department, site=admin_site)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_editable = ['status']
    search_fields = ['name']
    list_per_page = 10


@admin.register(Doctor, site=admin_site)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'designation',
                    'department', 'spacialist', 'status']
    list_editable = ['designation', 'department', 'spacialist', 'status']
    search_fields = ['department', 'user_details']
    list_per_page = 10


@admin.register(Day, site=admin_site)
class DayAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Schedule, site=admin_site)
class SchedulePaymentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'start_time', 'end_time', 'status']
    list_editable = ['start_time', 'end_time', 'status']
    search_fields = ['doctor']
    list_per_page = 10


@admin.register(Appointment, site=admin_site)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'is_confirmed']
    list_editable = ['doctor', 'appointment_date', 'is_confirmed']
    search_fields = ['patient']
    list_per_page = 10


@admin.register(Bed, site=admin_site)
class BedAdmin(admin.ModelAdmin):
    list_display = ['bed_type', 'bed_capacity', 'charge', 'status']
    list_editable = ['bed_capacity', 'charge', 'status']
    search_fields = ['bed_type']
    list_per_page = 10


@admin.register(BedAssign, site=admin_site)
class BedAssignAdmin(admin.ModelAdmin):
    list_display = ['patient','bed', 'assigned_date', 'status']
    list_editable = ['bed','status']
    search_fields = ['patient']
    list_per_page = 10


@admin.register(BirthReport, site=admin_site)
class BirthReportAdmin(admin.ModelAdmin):
    list_display = ['patient','weight']
    list_editable = ['weight']
    search_fields = ['patient']
    list_per_page = 10


@admin.register(DeathReport, site=admin_site)
class DeathReportAdmin(admin.ModelAdmin):
    list_display = ['patient', 'place_of_death']
    list_editable = ['place_of_death',]
    search_fields = ['patient']
    list_per_page = 10
