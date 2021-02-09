from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Appointment(models.Model):
    # users, time
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=10)
    description=models.CharField(max_length=20)
    published=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # appointment_date=models.DateTimeField()
    def __str__(self):
        return f"Appointment for {self.user} on {self.timestamp}"
    
    class Meta:
        ordering=['-timestamp'] #latest appointment appears first create new branch off master and push to it


    
