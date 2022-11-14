from django.db import models

from users.models import User

# Create your models here.
class Friends(models.Model):
	sender_id = models.ForeignKey(User, related_name='sender_user_id', on_delete=models.CASCADE)
	receiver_id = models.ForeignKey(User, related_name='receiver_user_id', on_delete=models.CASCADE)
	accepted = models.BooleanField(default=False)