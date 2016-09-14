from django.contrib import admin

from app.models import *


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = Sample._fields()


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = Demo._fields()
