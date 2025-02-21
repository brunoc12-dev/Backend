from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserAppSerializer
from .models import UserApp


class UsuariosHolaMundo(APIView):

    permission_classes = []

    def get(self, request):

        data = {
            "mensaje": "Hola Mundo",
             "status": 200
        }

        return Response(data, status=status.HTTP_200_OK)
    

class UserAppView(APIView):
    permission_classes = []
    def post(self, request):
        data = request.data
        serializer = UserAppSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        usuarios = UserApp.objects.all()
        serializer = UserAppSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    