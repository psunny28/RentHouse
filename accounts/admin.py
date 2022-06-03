from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin


class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_number', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_landlord',
            'is_realtor',
            'is_admin',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display    =   ('id', 'first_name', 'last_name', 'email', "date_joined", 'last_login', 'is_staff', 'is_active')
    list_display_links  =   ('first_name', 'email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    ordering    =   ('-date_joined',)


class ProfileAdmin(admin.ModelAdmin):
    def thumbmail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50;">'.format(object.profile_picture.url))
        thumbmail.short_description =   'Profile Picture'
    list_display    =   ('user', 'gender', 'city', "state", 'thumbmail')

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
