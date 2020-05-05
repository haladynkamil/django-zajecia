from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    fields = ['first_name', 'second_name', 'postal_code', 'street','city', 'nip']

admin.site.register(Client, ClientAdmin)

# Register your models here.
