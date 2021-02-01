from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Loan_History)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanApplication)
class OrganizationAdmin(admin.ModelAdmin):
    pass
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass