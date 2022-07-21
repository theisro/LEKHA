from django.db import models
from django.contrib.auth.models import AbstractUser
from archival.models import Archive

# class CustomUser(AbstractUser):
#     archive = models.ForeignKey(Archive, on_delete=models.CASCADE)