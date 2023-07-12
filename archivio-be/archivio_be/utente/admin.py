from django.contrib import admin
from .models import Utente


class UtenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'username', 'password', 'flagAttivo', 'timestamp')


admin.site.register(Utente, UtenteAdmin)
