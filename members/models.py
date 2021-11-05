from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    sensorID = models.IntegerField()
    installDate = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=72)
    lastVist = models.DateField(auto_now_add=False)
    lastRadonTest = models.DateField(auto_now_add=False)
    radonRequest = models.CharField(max_length=8)
    sensorRequest = models.CharField(max_length=8)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
