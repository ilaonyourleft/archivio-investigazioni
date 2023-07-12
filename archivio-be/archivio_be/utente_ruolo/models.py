from django.db import models

from ruolo.models import Ruolo
from utente.models import Utente


class UtenteRuolo(models.Model):
    fkUtente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    fkRuolo = models.ForeignKey(Ruolo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
