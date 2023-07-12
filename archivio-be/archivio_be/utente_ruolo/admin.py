from django.contrib import admin
from .models import UtenteRuolo


class UtenteRuoloAdmin(admin.ModelAdmin):
    list_display = ('fkUtente', 'fkRuolo', 'timestamp')


admin.site.register(UtenteRuolo, UtenteRuoloAdmin)
