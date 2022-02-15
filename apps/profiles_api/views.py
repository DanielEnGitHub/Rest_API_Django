from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ API View de prueba """
    
    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del APIView"""

        list = [
            'Usamos metodos HTTP como funciones (get, post, patch, delete, put)',
            'Es similar a una vista tradicional de django',
            'Nos da mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeando manualmente las urls'
        ]

        return Response({'message': 'hola mundo', 'list': list})