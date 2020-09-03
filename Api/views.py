from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CartoonSerializer
from .models import Cartoon

class CartoonViewSet(viewsets.ModelViewSet):
    queryset = Cartoon.objects.all().order_by('name')
    serializer_class = CartoonSerializer

