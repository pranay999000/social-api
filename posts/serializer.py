from rest_framework import serializers
from . views import Posts
from users.serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=False)
	class Meta:
		model = Posts
		fields = [
			'title',
			'description',
			'image',
			'date',
			'id',
			'user',
		]