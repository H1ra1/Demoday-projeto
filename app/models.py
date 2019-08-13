from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=100, default='')
    nome_usuario = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=255, default='')
    celular = models.CharField(max_lentgh=14, default='')
    senha = models.CharField(max_length=10, default='')
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome_completo