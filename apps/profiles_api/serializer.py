from unicodedata import name
from rest_framework import serializers

class HellowSerializer(serializers.Serializer):
    """Serializa un campo para probar nuestra APIView"""
    name = serializers.CharField(max_length=10)