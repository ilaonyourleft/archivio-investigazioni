from django.contrib import admin
from .models import Caso


class CasoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descrizione', 'dataInizio', 'dataFine', 'timestamp', 'fkUtente', 'fkStato')


admin.site.register(Caso, CasoAdmin)
