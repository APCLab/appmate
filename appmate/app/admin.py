from django.contrib import admin

from app.models import *


@admin.register(VoiceLog)
class VoiceLogAdmin(admin.ModelAdmin):
    list_display = VoiceLog._fields()
