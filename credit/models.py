from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.IntegerField()
    withdraw = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
