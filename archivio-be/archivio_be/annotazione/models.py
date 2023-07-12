from django.db import models

from archivio.models import Archivio
from utente.models import Utente


class Annotazione(models.Model):
    titolo = models.CharField("titolo", max_length=100)
    descrizione = models.TextField("descrizione")
    data = models.DateField("data")
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
    fkUtente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    fkArchivio = models.ForeignKey(Archivio, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
