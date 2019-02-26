from django.db import models

# Create your models here.
class Team(models.Model):
    name            = models.CharField(max_length=250)
    title           = models.CharField(max_length=250)
    pic             = models.ImageField(blank=True, null=True, upload_to='team/')
    bio             = models.TextField()
    facebook        = models.URLField(blank=True, null=True, max_length=300)
    twitter         = models.URLField(blank=True, null=True, max_length=300)
    instagram       = models.URLField(blank=True, null=True, max_length=300)
    linkedin        = models.URLField(blank=True, null=True, max_length=300)

    def __str__(self):
        return self.name