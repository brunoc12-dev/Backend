from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsuariosHolaMundo(APIView):

    permission_classes = []

    def get(self, request):

        data = {
            "mensaje": "Hola Mundo",
             "status": 200
        }

        return Response(data, status=status.HTTP_200_OK)