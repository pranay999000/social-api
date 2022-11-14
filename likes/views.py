from rest_framework.response import Response
from rest_framework.views import APIView
from likes.models import Likes
from likes.serializer import LikeSerializer
from posts.models import Posts
from socialApi.authentication import TokenAuthentication

# Create your views here.
class LikeAPICreate(APIView):

	def post(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			post = Posts.objects.get(id=post_id)
			if post:
				like = Likes.objects.create(user=user, post=post)
				post.likes_set.add(like)
				serializer = LikeSerializer(like)
				return Response(serializer.data)
			else:
				return Response({
					"message": "Post not found!"
				}, status=404)
		else:
			return res

class LikeAPIDelete(APIView):

	def delete(self, request, like_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			like = Likes.objects.get(id=like_id)
			if like.user.id != user.id:
				return Response({
					"message": "Cannot delete someone else's like"
				})
			if like:
				like.delete()
			return Response({
				"message": "Like deleted"
			})
		else:
			return res

class LikeAPIMyLiked(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			likes = Likes.objects.filter(user__id=user.id)
			serializer = LikeSerializer(likes, many=True)
			return Response(serializer.data)
		else:
			return res