from django.db import models

from caso.models import Caso
from stato.models import Stato
from utente.models import Utente


class Fascicolo(models.Model):
    titolo = models.CharField("titolo", max_length=100)
    descrizione = models.TextField("descrizione")
    luogo = models.CharField("luogo", max_length=100)
    data = models.DateField("data")
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
    fkUtente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    fkCaso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    fkStato = models.ForeignKey(Stato, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
