from django.contrib import admin
from hms.admin import admin_site
from .models import AppSettings, Notice,UserDetail

@admin.register(AppSettings, site=admin_site)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ['application_title', 'email_address', 'phone_number']
    list_editable = ['email_address']
    search_fields = ['application_title']
    list_per_page = 10


@admin.register(Notice, site=admin_site)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'status']
    list_editable = ['start_date', 'end_date', 'status']
    search_fields = ['title']
    list_per_page = 10

@admin.register(UserDetail, site=admin_site)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address', 'sex']

