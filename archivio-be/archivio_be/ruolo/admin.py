from django.contrib import admin
from .models import Ruolo


class RuoloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ruolo, RuoloAdmin)
