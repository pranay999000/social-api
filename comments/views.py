from rest_framework.views import APIView
from rest_framework.response import Response
from comments.models import Comments
from posts.models import Posts
from . serializer import CommentSerializer
from socialApi.authentication import TokenAuthentication

# Create your views here.
class CommentAPICreate(APIView):

	def post(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			post = Posts.objects.get(id=post_id)
			if post:
				comment = Comments.objects.create(
					user=user,
					post=post,
					comment=request.data['comment']
				)
				if comment:
					serializer = CommentSerializer(comment)
					post.comments_set.add(comment)
					return Response(serializer.data)
				else:
					return Response({
						"message": "Unable to save comment"
					})

			else:
				return Response({
					"message": "Post not found"
				})
		else:
			return res


class CommentAPIByPostId(APIView):

	def get(self, request, post_id):
		user, res = TokenAuthentication().authenticate(request)

		if user:
			comments = Comments.objects.filter(post__id=post_id)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data)
		else:
			return res