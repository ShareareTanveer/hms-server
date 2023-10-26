from django.contrib import admin
from hms.admin import admin_site
from .models import Patient, PatientDocument, PatientCseStudy

@admin.register(Patient, site=admin_site)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'patient_id', 'status']
    list_editable = ['status']
    search_fields = ['patient_id']
    list_per_page = 10


@admin.register(PatientDocument, site=admin_site)
class PatientDocumentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'prescription']
    list_editable = []
    search_fields = ['patient']
    list_per_page = 10


@admin.register(PatientCseStudy, site=admin_site)
class PatientCseStudyAdmin(admin.ModelAdmin):
    list_display = ['patient','status']
    list_editable = ['status']
    search_fields = ['patient']
    list_per_page = 10
