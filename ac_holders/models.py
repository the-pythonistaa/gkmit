from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    amount = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
