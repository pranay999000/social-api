from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from friends.models import Friends
from friends.serializer import FriendSerializer
from socialApi.authentication import TokenAuthentication
from users.serializer import UserSerializer
from . models import User
import jwt


key = 'secret'

class UserAPICreate(APIView):

	def post(self, request):
		if User.objects.filter(email = request.data['email']).exists():
			return Response({
				'success': False,
				'message': "Email already exists!"
			})

		else:
			user = User.objects.create(
				name=request.data['name'],
				email=request.data['email'],
				password=request.data['password'],
				image=request.data['image']
			)

			serialize = UserSerializer(user)
			encoded = jwt.encode(serialize.data, key, algorithm='HS256')

			return Response({
				'token': encoded,
				'data': serialize.data
			})



class UserAPILogin(APIView):

	def post(self, request):
		user = User.objects.get(email = request.data['email'], password = request.data['password'])
		if user:
			serialize = UserSerializer(user)
			encoded = jwt.encode(serialize.data, key, algorithm='HS256')

			return Response({
				'token': encoded,
				'data': serialize.data
			}, status=200)
		else:
			return Response({
				'message': 'Unauthorized',
			}, status=401)



class UserAPIAll(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			users = User.objects.all()
			serializer = UserSerializer(users, many=True)
			return Response(serializer.data)
		else:
			return res



class UserAPIById(APIView):

	def get(self, request, id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			try:
				user = User.objects.get(id=id)
				friends = Friends.objects.filter((Q(sender_id__id = id) | Q(receiver_id__id = id)) & Q(accepted=True))
				
				serializerFriends = FriendSerializer(friends, many=True)
				serializer = UserSerializer(user)

				user_response = serializer.data
				friends = [x['receiver_id'] if x['sender_id']['id'] == id else x['sender_id'] for x in serializerFriends.data]

				user_response['friends'] = friends

				return Response(user_response)
			except User.DoesNotExist:
				return Response({
					'message': 'User not found'
				}, status=404)
		else:
			return res
