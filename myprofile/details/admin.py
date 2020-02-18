from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.UserDetails)
admin.site.register(models.CardDetails)
admin.site.register(models.OrderDetails)