from rest_framework import serializers
from users.serializer import UserSerializer
from posts.serializer import PostSerializer
from . models import Comments

class CommentSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)
	post = PostSerializer(required=True)

	class Meta:
		model = Comments
		fields = [
			'comment',
			'date',
			'user',
			'post',
			'id',
		]