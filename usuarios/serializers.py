from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'puntos', 'is_admin' ]
        extra_kwargs = {'password': {'write_only': True}}
