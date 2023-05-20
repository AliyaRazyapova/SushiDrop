import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', '').split()
        if not auth_header or auth_header[0].lower() != 'bearer':
            return None

        if len(auth_header) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth_header) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')

        try:
            token = auth_header[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            user = User.objects.get(email=email)
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Error decoding token')
        except User.DoesNotExist:
            raise AuthenticationFailed('No user matching this token')

    def authenticate_header(self, request):
        return 'Bearer'
