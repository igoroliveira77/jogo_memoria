from django.db import models

class Carta(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='cartas/')

    def __str__(self):
        return self.nome
