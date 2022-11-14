from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.response import Response
import jwt

from users.models import User

class TokenAuthentication(BaseAuthentication):
	model = None

	def get_model(self):
		return User

	def authenticate(self, request):
		auth = get_authorization_header(request=request).split()
		if not auth or auth[0].lower() != b'bearer':
			return (None, Response({
				"message": "No authentication token found!"
			}))
		
		if len(auth) == 1:
			msg = 'Invalid token header. No credentials provided'
			return (None, Response({
				'message': msg
			}))
		elif len(auth) > 2:
			msg = 'Invalid token header.'
			return (None, Response({
				'message': msg
			}))
		
		try:
			token = auth[1]
			if token == 'null':
				msg = 'Null token not allowed'
				return (None, Response({
					'message': msg
				}))
		except UnicodeError:
			msg = 'Invalid token header. Token string should not contain invalid characters.'
			return (None, Response({
				'message': msg
			}))

		return self.authentication_credentials(token)

	def authentication_credentials(self, token):
		msg = {'Error': "Token mismatch"}
		try:
			payload = jwt.decode(token, 'secret', algorithms="HS256")
		except:
			return (None, Response(msg, status=401))

		try:
			user = User.objects.get(id=payload['id'])
			if not user:
				return (None, Response(msg))
		except jwt.ExpiredSignatureError:
			return (None, Response(msg))
		except User.DoesNotExist:
			return (None, Response({
				'error': 'User not found'
			}, status="404"))
		
		return (user, None)

