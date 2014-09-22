from django.contrib import admin
from diana.models import Client, Schedule


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password')


admin.site.register(Schedule)
