from django.contrib import admin
from .models import Stato


class StatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')


admin.site.register(Stato, StatoAdmin)
