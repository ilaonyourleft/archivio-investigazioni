from django.db import models


class Utente(models.Model):
    nome = models.CharField("nome", max_length=100)
    cognome = models.CharField("cognome", max_length=100)
    username = models.CharField("username", max_length=100, null=True)
    password = models.CharField("password", max_length=100, null=True)
    flagAttivo = models.BooleanField("flag_attivo", default=False)
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.flagAttivo}"
