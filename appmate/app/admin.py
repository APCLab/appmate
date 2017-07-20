from django.contrib import admin

from app.models import *


@admin.register(Iot)
class IotAdmin(admin.ModelAdmin):
    list_display = Iot._fields()
