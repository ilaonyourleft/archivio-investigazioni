from django.contrib import admin
from .models import Annotazione


class AnnotazioneAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'descrizione', 'data', 'timestamp', 'fkUtente', 'fkArchivio')


admin.site.register(Annotazione, AnnotazioneAdmin)
