from django.db import models
from client.models import Client

# Create your models here.

class Live(models.Model):
    client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    time        = models.DateTimeField(auto_now_add=True)
    is_live     = models.BooleanField(default=True)

    def __str__(self):
        return self.client.email
    