from django.db import models
from users.models import User
from posts.models import Posts
from django.utils import timezone

# Create your models here.
class Comments(models.Model):
	comment = models.CharField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now())