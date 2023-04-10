from .models import Menu
from .serializers import MenuSerializer
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@permission_classes([IsAuthenticated])
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
