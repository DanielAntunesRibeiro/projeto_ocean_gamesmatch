from msvcrt import LK_LOCK
from re import L
from unittest.util import _MAX_LENGTH
from django.db import models

class perfil(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.PositiveIntegerField.primary_key()
    game1 = models.CharField(max_length=255)
    pontuacao1 = models.PositiveIntegerField()
    game2 = models.CharField(max_length=255, blank=True, null=True)
    pontuacao2 = models.PositiveIntegerField(blank=True, null=True)
    dat_nasc = models.DateField()
    nickname = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    cep = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    zone = models.CharField(max_length=100)