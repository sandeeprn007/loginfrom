from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #additional fields 
    user_img=models.ImageField(blank=True)
    user_url=models.URLField(blank=True)

class Userpost(models.Model):
    Title = models.CharField(max_length=200)
    Subtitle = models.CharField(max_length=200)
    Subj = models.CharField(max_length=200)
    img = models.ImageField(upload_to="userimg/",blank=True)  
    Created_By = models.CharField(max_length=200)
    