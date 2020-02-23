from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.CharField(max_length=15)
    age = models.IntegerField()
    vehicle = models.FileField()

    def __str__(self):
        return self.driver






