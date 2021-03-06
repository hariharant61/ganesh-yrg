from django.db import models

class UserProfile(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=250)
  email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
  mobile = models.CharField(max_length=30)
  password = models.CharField(max_length=30)

class Location(models.Model):
  lat = models.CharField(max_length=30)
  long = models.CharField(max_length=30)
  address = models.CharField(max_length=200)
  description = models.CharField(max_length=50)
  status = models.CharField(max_length=30)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  def __str__(self):
    return self.address
