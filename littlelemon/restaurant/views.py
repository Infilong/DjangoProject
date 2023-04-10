from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html', {})

# generics are classes that provide pre-built views to handle common cases like listing, creating, updating and deleting objects.
# They often require you to complete some of the implementation details yourself,
# such as defining the queryset and serializer_class attributes.


@permission_classes([IsAuthenticated])
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# viewsets are classes that provide a more complete set of views for a given model or queryset.
# They include all of the CRUD (Create, Retrieve, Update, Delete) operations
# as well as other commonly used actions like filtering and pagination
@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
