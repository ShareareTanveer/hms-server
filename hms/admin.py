from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from authentication.models import User
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
# Register your models here.


class CustomAdminSite(admin.AdminSite):
    site_header = 'Hotel Management Admin Panel'
    site_title = 'Hotel Management Admin Panel'
    index_title = 'Admin Panel'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('my-custom-page/', self.admin_view(self.my_custom_view))
        ]
        return custom_urls + urls

    def my_custom_view(self, request):
        return HttpResponse('Hello, world!')

admin_site = CustomAdminSite(name='myadmin')


class CustomUserAdmin(UserAdmin):

    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password','role')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name', 'last_name','role'),
        }),
    )


admin_site.register(User, CustomUserAdmin)
admin_site.register(Group, GroupAdmin)
