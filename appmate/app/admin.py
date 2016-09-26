from django.contrib import admin

from app.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = User._fields()


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = Restaurant._fields()


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = Rate._fields()


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = Menu._fields()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = Order._fields()


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = Reservation._fields()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = Favorite._fields()
