from django.contrib import admin
from .models import Supervisor, Agent, Department
import admin_thumbnails

# Register your models here.
class SupervisorAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'name', 'Employee_ID', 'designation', 'city',)
    list_display_links  =   ('name', 'Employee_ID',)

@admin_thumbnails.thumbnail('photo',)
class AgentAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'name', 'email', 'phone', 'designation', 'Employee_ID', 'supervisor_name', 'is_mvp', 'hire_date')
    list_display_links  =   ('name', 'email',)
    list_filter =   ('is_mvp', 'supervisor_name', 'email')
    search_fields   =   ('phone', 'Employee_ID',)
    list_per_page   =   25

class DepartmentAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'name')

admin.site.register(Agent, AgentAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Department, DepartmentAdmin)
