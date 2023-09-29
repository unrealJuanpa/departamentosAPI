from django.db import models
from model_utils.models import *

# Create your models here.
class Departamento(TimeStampedModel, SoftDeletableModel):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    fundacion = models.DateField()

class Municipio(TimeStampedModel, SoftDeletableModel):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    habitantes = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)
    

