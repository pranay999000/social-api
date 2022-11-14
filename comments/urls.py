from django.urls import path
from . views import CommentAPICreate, CommentAPIByPostId

urlpatterns = [
	path('create/<int:post_id>', CommentAPICreate.as_view()),
	path('<int:post_id>', CommentAPIByPostId.as_view())
]