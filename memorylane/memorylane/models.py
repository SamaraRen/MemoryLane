from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

'''class UserProfile(models.Model):
    username = models.CharField(max_length=5000) 
    friends = models.CharField(max_length=5000)
    propic = models.CharField(max_length=1000)
    date_created = models.DateField()
    bio = models.TextField()
    livesin = models.TextField()
    about = models.TextField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name
'''
class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length=5000) 
    friends = models.ManyToManyField("self")
    propic = models.CharField(max_length=1000)
    date_created = models.DateField()
    bio = models.TextField()
    livesin = models.TextField()
    about = models.TextField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Location(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 60)

class Memory(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    image = models.FileField(upload_to="memorylane/static/images")
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_created = models.DateField()

    def __str__(self):
    	return self.name

