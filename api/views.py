from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


# import JsonResponse
from django.http import JsonResponse

from .models import TodoList
from .serializers import TodoListSerializer


# Create your views here.


class TodoTasksAPI(ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]


class TodoTasksViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
