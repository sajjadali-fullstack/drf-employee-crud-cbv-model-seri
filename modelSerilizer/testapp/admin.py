from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'emp_sal', 'emp_add')
    search_fields = ('emp_id', 'emp_name', 'emp_sal', 'emp_add')
    ordering = ('id',)

# Register your models here.

admin.site.register(Employee, EmployeeAdmin)