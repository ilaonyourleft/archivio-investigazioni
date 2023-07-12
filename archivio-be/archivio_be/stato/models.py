from django.db import models


class Stato(models.Model):
    nome = models.CharField("nome", max_length=100)
    tipo = models.CharField("tipo", max_length=100)

    def __str__(self):
        return f"{self.nome}, {self.tipo}"
