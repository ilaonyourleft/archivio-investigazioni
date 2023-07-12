from django.db import models

from stato.models import Stato
from utente.models import Utente


class Caso(models.Model):
    nome = models.CharField("nome", max_length=100)
    descrizione = models.TextField("descrizione")
    dataInizio = models.DateField("data_inizio")
    dataFine = models.DateField("data_fine")
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
    fkUtente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    fkStato = models.ForeignKey(Stato, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

