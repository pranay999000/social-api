from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Posts
from posts.serializer import PostSerializer
from socialApi.authentication import TokenAuthentication
from likes.serializer import LikeSerializer
from comments.serializer import CommentSerializer

# Create your views here.
class PostAPICreate(APIView):

	def post(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			new_post = Posts.objects.create(
				title=request.data['title'],
				description=request.data['description'],
				image=request.data['image'],
				user=user
			)

			serializer = PostSerializer(new_post)
			return Response(serializer.data)
		else:
			return res

class PostAPIAll(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			posts = Posts.objects.all().order_by('-date')
			likes = dict()
			comments = dict()
			for p in posts:
				likes[p.id] = likes.get(p.id, []) + LikeSerializer(p.likes_set.all(), many=True).data
				comments[p.id] = comments.get(p.id, []) + CommentSerializer(p.comments_set.all(), many=True).data

			serializer = PostSerializer(posts, many=True)
			posts_data = serializer.data

			post_response = list()
			for s in posts_data:
				s['likes'] = likes[s['id']] if s['id'] in likes else []
				s['comments'] = comments[s['id']] if s['id'] in comments else []
				post_response.append(s)
				
			return Response(post_response)
		else:
			return res

class PostAPIById(APIView):

	def get(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			post = Posts.objects.get(id=post_id)
			serializer = PostSerializer(post)
			return Response(serializer.data)
		else:
			return res

class PostAPIMyPosts(APIView):

	def get(self, request):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			my_posts = Posts.objects.filter(user__id=user.id).order_by('-date')
			serializer = PostSerializer(my_posts, many=True)
			return Response(serializer.data)
		else:
			return res

class PostAPIUpdate(APIView):

	def patch(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			post = Posts.objects.get(id=post_id)
			if post.user.id == user.id:
				if post:
					serializer = PostSerializer(post, data=request.data, partial=True)
					if serializer.is_valid():
						serializer.save()
						return Response(serializer.data)
					else:
						return Response({
							"message": "Invalid request"
						}, status=400)
				else:
					return Response({
						'message': "Post not found"
					}, status=404)
			else:
				return Response({
					"message": "Cannot update someone else's post"
				})
		else:
			return res

class PostAPIDelete(APIView):

	def delete(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			post = Posts.objects.get(id=post_id)
			if post.user.id == user.id:
				post.delete()
				return Response({
					"message": "Post deleted"
				})
			else:
				return Response({
					"message": "Cannot delete someone else's post"
				})
		else:
			return res