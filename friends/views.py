from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from socialApi.authentication import TokenAuthentication
from users.models import User
from . models import Friends
from . serializer import FriendSerializer

# Create your views here.
class FriendsAPISendRequest(APIView):

	def post(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			try:
				check_req = Friends.objects.filter(
					sender_id__id=user.id,
					receiver_id__id=request.data['receiver_id']
				)
				if len(check_req) > 0:
					return Response({
						'message': "Request has already been sent to this user"
					}, status=400)

				receiver = User.objects.get(id = request.data['receiver_id'])

				if receiver:
					request = Friends.objects.create(
						sender_id=user,
						receiver_id=receiver
					)

					serializer = FriendSerializer(request)
					return Response(serializer.data)
				else:
					return Response({
						'message': "User not found!s"
					})
			except Exception as e:
				print(e)
				return Response({
					'message': "Invalid request"
				}, status=400)

		else:
			return res

class FriendsAPISentRequests(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			try:
				requests = Friends.objects.filter(Q(sender_id__id=user.id) & Q(accepted=False))
				serializer = FriendSerializer(requests, many=True)
				return Response(serializer.data)
			except Exception as e:
				print(e)
				return Response({
					'message': "Invalid request"
				}, status=400)
		else:
			return res

class FriendsAPIReceivedRequests(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			try:
				requests = Friends.objects.filter(Q(receiver_id__id=user.id) & Q(accepted=False))
				serializer = FriendSerializer(requests, many=True)
				return Response(serializer.data)
			except Exception as e:
				print(e)
				return Response({
					'message': 'Invalid request'
				}, status=400)
		else:
			return res

class FriendsAPIAccept(APIView):

	def put(self, request, sender_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			req = Friends.objects.get(sender_id__id=sender_id, receiver_id__id=user.id)
			if req:
				req.accepted = True
				req.save()
				serializer = FriendSerializer(req)
				return Response(serializer.data)
			else:
				return Response({
					'message': "Request not found"
				})
		else:
			return res

class FriendsAPI(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			requests = Friends.objects.filter(
				(Q(sender_id__id=user.id) | Q(receiver_id__id=user.id)) & 
				Q(accepted=True)
			)
			serializer = FriendSerializer(requests, many=True)
			response = list()

			for f in serializer.data:
				if f['sender_id']['id'] == user.id:
					response.append(f['receiver_id'])
				else:
					response.append(f['sender_id'])

			return Response(response)
		else:
			return res