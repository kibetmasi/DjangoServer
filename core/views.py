from django.shortcuts import render
from rest_framework import generics
from .serializers import AppointmentSerializer
from .models import Appointment

# Create your views here.
def index(request):
    return render(request,'index.html')

class ListAppointments(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer