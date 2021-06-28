import jwt

from django.http  import JsonResponse

from users.models           import User
from wecode_expert.settings import SECRET_KEY, ALGORITHM

def user_check(is_required):
    def outer(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                access_token = request.headers.get('Authorization')

                if not access_token:
                    if is_required == 'MUST_BE_USER':
                        return JsonResponse({'message':'INVALID_TOKEN'}, status=401)
                    if is_required == 'DONT_HAVE_TO_BE_USER':
                        request.user = None
                        return func(self, request, *args, **kwargs)
                
                user = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
                if not User.objects.filter(id=user.id).exists():
                    return JsonResponse({'message':'INVALID_USER'}, status=401)
                
                request.user = user
                return func(self, request, *args, **kwargs)

            except jwt.exceptions.DecodeError:
                return JsonResponse({'message':'INVALID_TOKEN'}, status=401)
        return wrapper
    return outer