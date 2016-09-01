from django.contrib import admin

from app.models import Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'msg',
        'date',
        'timestamp',
        'img',
        'checked',
        'email',
        'index')
