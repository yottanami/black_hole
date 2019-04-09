from django.db import models

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.IntegerField(min_digits=4)
    withdraw = models.IntegerField(min_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
