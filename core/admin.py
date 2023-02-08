from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Professor)
admin.site.register(models.Section)
admin.site.register(models.Subject)
admin.site.register(models.Schedule)