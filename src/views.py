from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import UserText
from .serializers import PostSerializer

class UserTextViewSet(viewsets.ModelViewSet):
    queryset = UserText.objects.all()
    serializer_class = PostSerializer