from django.contrib import admin

from app.models import AppData


@admin.register(AppData)
class AppDataAdmin(admin.ModelAdmin):
    pass
