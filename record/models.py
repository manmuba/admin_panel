from django.core.validators import FileExtensionValidator
from django.db import models

from client.models import Client
# Create your models here.

class Record(models.Model):
    client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    video       = models.FileField(
                        upload_to='videos_uploaded',
                        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'flv', 'mpeg', 'mpg', 'm4v', '3gp', '3g2', 'ogg', 'ogv', 'QT'])]
                    )
    time        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.email} {self.time}"
    