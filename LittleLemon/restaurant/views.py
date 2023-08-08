from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated class
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your view functions here
def index(request):
    return render(request, 'restaurant/index.html', {})

def home_view(request):
    return render(request, 'restaurant/home.html', {})

def about_view(request):
    return render(request, 'restaurant/about.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission to this view

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission to this view

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission to this viewset
