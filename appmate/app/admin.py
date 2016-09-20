from django.contrib import admin

from app.models import *


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = Track._fields()


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = Vehicle._fields()


@admin.register(QueueList)
class QueueListAdmin(admin.ModelAdmin):
    list_display = QueueList._fields()


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = Evaluation._fields()


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = Customer._fields()


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = Driver._fields()
