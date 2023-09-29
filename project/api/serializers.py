from rest_framework import serializers
from api.models import *


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = []

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        exclude = []