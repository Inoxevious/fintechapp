from django.contrib import admin
from .models import AccountUser, LoanOfficer, Loan, Clients
# Register your models here.
@admin.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    pass


@admin.register(LoanOfficer)
class LoanOfficerAdmin(admin.ModelAdmin):
    pass
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    pass