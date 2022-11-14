from django.urls import path
from . views import FriendsAPISendRequest, FriendsAPISentRequests, FriendsAPIReceivedRequests, FriendsAPIAccept, FriendsAPI

urlpatterns = [
	path('send', FriendsAPISendRequest.as_view()),
	path('sent', FriendsAPISentRequests.as_view()),
	path('received', FriendsAPIReceivedRequests.as_view()),
	path('accept/<int:sender_id>', FriendsAPIAccept.as_view()),
	path('', FriendsAPI.as_view())
]