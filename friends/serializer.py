from rest_framework import serializers

from users.serializer import UserSerializer
from . models import Friends

class FriendSerializer(serializers.ModelSerializer):
	receiver_id = UserSerializer(required=False)
	sender_id = UserSerializer(required=False)
	class Meta:
		model = Friends
		fields = [
			'sender_id',
			'receiver_id',
			'accepted',
			'id'
		]

	def validate(self, data):
		if data['sender_id'] == data['receiver_id']:
			return serializers.ValidationError('Cannot send request to self')
		return data