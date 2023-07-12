from django.db import models

from utente.models import Utente


class Archivio(models.Model):
    nome = models.CharField("nome", max_length=100)
    fkUtente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
