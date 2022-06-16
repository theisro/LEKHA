from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Artist(models.Model):
    '''
    The artist class is a subtype of archive. It contains all of the information pertaining to an artist, such as their name, bio and social media links.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    aword1 = models.CharField(max_length=200)
    aword2 = models.CharField(max_length=200)
    aword3 = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    insta_handle = models.CharField(max_length=200)
    fb_handle = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=200)
    private = models.BooleanField(max_length=200)


    def __str__(self):
        return self.last_name

