from django.contrib import admin

from app.models import Sample, SAMPLE_FIELDS


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = SAMPLE_FIELDS
