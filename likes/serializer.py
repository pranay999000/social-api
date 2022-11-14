from rest_framework import serializers
from users.serializer import UserSerializer
from posts.serializer import PostSerializer
from . models import Likes

class LikeSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)
	post = PostSerializer(required=True)

	class Meta:
		model = Likes
		fields = [
			'user',
			'post',
			'id'
		]