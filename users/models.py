from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=120, blank=False)
	email = models.EmailField(max_length=200, blank=False)
	password = models.CharField(max_length=20, blank=False)
	image = models.CharField(max_length=200)