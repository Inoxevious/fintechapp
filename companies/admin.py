from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from .models import Country,Organization,Department,Role,LoanApplication
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
<<<<<<< HEAD

@admin.register(Loan_History)
class OrganizationAdmin(admin.ModelAdmin):
    pass

=======
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
@admin.register(LoanApplication)
class OrganizationAdmin(admin.ModelAdmin):
    pass
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass