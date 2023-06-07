from django.contrib import admin

# Register your models here.

from .models import Machine, Personnel

admin.site.register(Machine)
admin.site.register(Personnel)
