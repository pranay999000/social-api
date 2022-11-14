from datetime import datetime
from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now())