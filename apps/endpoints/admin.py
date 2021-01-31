from django.contrib import admin
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