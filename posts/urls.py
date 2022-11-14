from django.urls import path
from . views import PostAPICreate, PostAPIAll, PostAPIById, PostAPIMyPosts, PostAPIUpdate, PostAPIDelete

urlpatterns = [
	path('create', PostAPICreate.as_view()),
	path('', PostAPIAll.as_view()),
	path('<int:post_id>', PostAPIById.as_view()),
	path('mine', PostAPIMyPosts.as_view()),
	path('update/<int:post_id>', PostAPIUpdate.as_view()),
	path('delete/<int:post_id>', PostAPIDelete.as_view())
]