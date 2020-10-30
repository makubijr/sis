from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    logo = models.ImageField(default='default.jpg', upload_to='logos')

    def __str__(self):
        return f'{self.name} Profile'

 


