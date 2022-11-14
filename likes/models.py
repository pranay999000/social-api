from django.db import models
from users.models import User
from posts.models import Posts

# Create your models here.
class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)