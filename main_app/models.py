from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=140)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.user.username

class Post(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  photo = ImageField(blank=True, manual_crop="")

  class Meta:
    ordering = ['-id']

  def __str__(self):
    return self.user.username


