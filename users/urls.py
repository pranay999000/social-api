from django.urls import path, include
from . views import UserAPICreate, UserAPIAll, UserAPIById, UserAPILogin

urlpatterns = [
	path('create', UserAPICreate.as_view()),
	path('', UserAPIAll.as_view()),
	path('<int:id>', UserAPIById.as_view()),
	path('login', UserAPILogin.as_view())
]
