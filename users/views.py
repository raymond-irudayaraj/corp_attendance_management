from django.shortcuts import render
from django.http import Http404
  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
  
from users.models import User
from users.serializers import UserCreateSerializer
  
class UserList(APIView):
    """
    List all the Users
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)