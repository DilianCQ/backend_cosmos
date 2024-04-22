from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Buscar el usuario por correo electrónico
        usuario = Usuario.objects.filter(email=email).first()

        if usuario is not None and usuario.verificar_contrasena(password):
            # Si las credenciales son válidas, puedes hacer alguna acción adicional si es necesario
            return Response({'detail': 'Autenticación exitosa'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'])
    def loginadmin(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = Usuario.objects.filter(email=email).first()
        if usuario is not None and usuario.verificar_contrasena(password) and usuario.is_admin:
            if usuario.is_admin:
                return Response({'detail': 'Autenticación exitosa'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No es admin'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
        
        
    @action(detail=False, methods=['post'])
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = Usuario.objects.create(email=email, password=password)        
        return Response({'detail': 'Creación exitosa'}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def generatepoint(self, request):
        email = request.data.get('email')
        puntos = request.data.get('puntos')

        # Buscar el usuario por correo electrónico
        usuario = Usuario.objects.filter(email=email).first()

        if usuario:
            usuario.puntos=usuario.puntos+puntos
            usuario.save()
            return Response({'detail': 'Asignación exitosa'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
    
    @action(detail=False, methods=['post'])
    def getbyemail(self, request):
        email = request.data.get('email')

        # Buscar el usuario por correo electrónico
        usuario = Usuario.objects.filter(email=email).first()

        if usuario:
            return Response({'puntos': usuario.puntos}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        