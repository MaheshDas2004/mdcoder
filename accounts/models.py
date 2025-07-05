from django.db import models

# Create your models here.
class DarexUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    college = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email