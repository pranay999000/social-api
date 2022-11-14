from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'name',
			'email',
			'password',
			'image',
			'id',
		]

		extra_kwargs = {
			'password': { 'write_only': True }
		}
	
	def validate(self, data):
		if not data['name'] or data['name'].strip() == '':
			return serializers.ValidationError('Name field is required!')
		if not data['email'] or data['email'].strip() == '':
			return serializers.ValidationError('Email field is required!')
		if not data['password'] or data['password'].strip() == '':
			return serializers.ValidationError('Password field is required!')
		return data