from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
from django.db.models import Max


class Quarto(models.Model):
    descricao = models.CharField(max_length=255)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    valor = models.FloatField(null=True)

    # data_inicio = models.CharField(max_length=255, null=True)
    # data_fim = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['id']


class Reserva(models.Model):
    inicio = models.CharField(max_length=255, null=True)
    fim = models.CharField(max_length=255, null=True)
    cliente = models.CharField(max_length=255)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name='Quarto')
    descricao_quarto = models.CharField(max_length=255, null=True)
    valor_quarto = models.FloatField()
    valor_total = models.FloatField()
    status = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['id']

# class Usuario(AbstractUser):
#     username = models.CharField(max_length=255, null=False, verbose_name='Username', unique=True)
#     email = models.EmailField(max_length=255, null=True, verbose_name='Email')
#     password = models.CharField(max_length=255, null=False)
#
#     objects = UserManager()
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
#
#     class Meta:
#         ordering = ['id']
#
#     def save(self, *args, **kwargs):
#         if (self.id == None):
#             self.is_active = True
#             self.is_superuser = True
#             self.is_staff = True
#             self.set_password(self.password)
#             super(Usuario, self).save()
#
#     def __str__(self):
#         return self.nome
