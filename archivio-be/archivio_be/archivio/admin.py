from django.contrib import admin
from .models import Archivio


class ArchivioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fkUtente')


admin.site.register(Archivio, ArchivioAdmin)
