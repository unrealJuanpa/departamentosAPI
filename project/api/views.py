from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
import django
import datetime

# Create your views here.

class Departamento_APIView(APIView): # no detalle url
    def get(self, request, format=None, *args, **kwargs):
        try:
            dep = list(Departamento.objects.all().values())
            return Response(dep, status=status.HTTP_200_OK)
        except Exception as er:
            return Response({'message': f'ERROR: {er}'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None, *args, **kwargs):
        try:
            Departamento.objects.create(**request.data)
            return Response({'message': 'Departamento creado!'}, status=status.HTTP_200_OK)
        except Exception as er:
            return Response({'message': f'ERROR: {er}'}, status=status.HTTP_400_BAD_REQUEST)
   

class Departamento_APIView_ID(APIView):
    def get(self, request, id):
        try:
            dep = Departamento.objects.get(id=id)
            dep = DepartamentoSerializer(dep).data
            return Response(dep, status=status.HTTP_200_OK)
        except Exception as er:
            return Response({'message': f'ERROR: {er}'}, status=status.HTTP_400_BAD_REQUEST)        
        
    def put(self, request, id):
        try:
            dep = Departamento.objects.get(id=id)

            for fname in list(request.data.keys()):
                setattr(dep, fname, request.data[fname])

            dep.save()

            return Response({'message': 'Departamento modificado!'}, status=status.HTTP_200_OK)
        except Exception as er:
            return Response({'message': f'ERROR: {er}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            dep = Departamento.objects.get(id=id)
            dep.delete()
            return Response({'message': 'Departamento eliminado!'}, status=status.HTTP_200_OK)
        except Exception as er:
            return Response({'message': f'ERROR: {er}'}, status=status.HTTP_400_BAD_REQUEST)
