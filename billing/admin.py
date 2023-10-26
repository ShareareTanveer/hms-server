from django.contrib import admin
from hms.admin import admin_site
from .models import Bill, Account, Invoice, AccountPayment, Service, Package, PatientAdmission


@admin.register(Bill, site=admin_site)
class BillAdmin(admin.ModelAdmin):
    list_display = ['admission', 'doctor', 'amount']
    list_editable = ['doctor']
    search_fields = ['admission']
    list_per_page = 10


@admin.register(Account, site=admin_site)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_type', 'status']
    list_editable = ['account_type', 'status']
    search_fields = ['account_name']
    list_per_page = 10


@admin.register(Invoice, site=admin_site)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['account', 'patient', 'doctor', 'price', 'status']
    list_editable = ['price', 'status']
    search_fields = ['account']
    list_per_page = 10


@admin.register(AccountPayment, site=admin_site)
class AccountPaymentAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'status']
    list_editable = ['amount', 'status']
    search_fields = ['account']
    list_per_page = 10


@admin.register(Service, site=admin_site)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'quantity', 'rate', 'status']
    list_editable = ['quantity', 'rate', 'status']
    search_fields = ['service_name']
    list_per_page = 10


@admin.register(Package, site=admin_site)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'service', 'discount', 'status']
    list_editable = ['discount', 'status']
    search_fields = ['package_name']
    list_per_page = 10


@admin.register(PatientAdmission, site=admin_site)
class PatientAdmissionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor',
                    'admission_date', 'discharge_date', 'status']
    list_editable = ['admission_date', 'discharge_date', 'status']
    search_fields = ['patient']
    list_per_page = 10
