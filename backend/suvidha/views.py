from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import AircraftSerializer      # add this
from .models import Aircraft                     # add this

class AircraftView(viewsets.ModelViewSet):       # add this
  serializer_class = AircraftSerializer          # add this
  queryset = Aircraft.objects.all()              # add this
