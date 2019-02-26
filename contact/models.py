from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name            = models.CharField(max_length=100)
    email           = models.EmailField()
    phone           = models.CharField(max_length=14)
    message         = models.TextField()
    date            = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name