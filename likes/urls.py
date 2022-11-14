from django.urls import path
from . views import LikeAPICreate, LikeAPIDelete, LikeAPIMyLiked

urlpatterns = [
	path('create/<int:post_id>', LikeAPICreate.as_view()),
	path('delete/<int:like_id>', LikeAPIDelete.as_view()),
	path('mine', LikeAPIMyLiked.as_view())
]