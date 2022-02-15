from ast import Return
from email import message
import imp
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.profiles_api import serializer

class HelloApiView(APIView):
    """ API View de prueba """
    
    serializer_class = serializer.HellowSerializer

    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del APIView"""

        list = [
            'Usamos metodos HTTP como funciones (get, post, patch, delete, put)',
            'Es similar a una vista tradicional de django',
            'Nos da mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeando manualmente las urls'
        ]

        return Response({'message': 'hola mundo', 'list': list})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Actualiza un objeto """
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto"""
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Borrar objeto """
        return Response({'Method': 'DELETE'})