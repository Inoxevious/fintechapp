from django.contrib import admin
from .models import Country,Organization,Department,Role,LoanApplication
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Organization)
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