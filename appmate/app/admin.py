from django.contrib import admin

from app.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = User._fields()


@admin.register(ConcertInfo)
class ConcertInfoAdmin(admin.ModelAdmin):
    list_display = ConcertInfo._fields()


@admin.register(ConcertBid)
class ConcertBidAdmin(admin.ModelAdmin):
    list_display = ConcertBid._fields()


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = Ticket._fields()
