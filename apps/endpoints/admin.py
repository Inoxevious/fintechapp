from django.contrib import admin
<<<<<<< HEAD
from .models import * 
# Register your models here.
@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    pass

@admin.register(MLAlgorithm)
class MLAlgorithmAdmin(admin.ModelAdmin):
    pass

@admin.register(MLAlgorithmStatus)
class MLAlgorithmStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(MLRequest)
class MLRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(ABTest)
class ABTestAdmin(admin.ModelAdmin):
    pass
=======

# Register your models here.
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
