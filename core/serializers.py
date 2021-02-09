from core.models import Appointment
from rest_framework import serializers

# turn the model into json 
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "user",'description','published', "timestamp",)
    
    def create(self, validated_data):
        # this will create and return a new instance of appointment
        return Appointment.objects.create(**validated_data)
