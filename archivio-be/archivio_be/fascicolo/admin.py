from django.contrib import admin
from .models import Fascicolo


class FascicoloAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'descrizione', 'luogo', 'data', 'timestamp', 'fkUtente', 'fkCaso', 'fkStato')


admin.site.register(Fascicolo, FascicoloAdmin)
