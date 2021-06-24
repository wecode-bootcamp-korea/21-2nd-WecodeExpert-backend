import jwt
import requests

from django.http.response import JsonResponse
from django.views import View
from django.core.exceptions import MultipleObjectsReturned

from .models import User
from wecode_expert.settings import SECRET_KEY, ALGORITHM

class SocialUserView(View):
    def post(self, request):
        try:
            URL                = 'https://kapi.kakao.com/v2/user/me'
            kakao_access_token = request.headers.get('Authorization')

            if not kakao_access_token:
                return JsonResponse({'message':'INVALID_TOKEN'}, status=401)

            headers   = {'Authorization': f'Bearer {kakao_access_token}'}
            response  = requests.post(URL, headers=headers)
            json_data = response.json()

            identifier = json_data.get('id')
            email      = json_data['kakao_account'].get('email')
            image      = json_data['kakao_account']['profile'].get('profile_image_url')
            
            if not identifier or not email or not image:
                return JsonResponse({'message':'INVALID_PROFILE'}, status=400)

            user, created = User.objects.get_or_create(
                identifier = identifier, 
                defaults = {
                    'email' : email,
                    'image' : image 
                }
            )

            user_data = {'user_id': user.id}
            access_token = jwt.encode(user_data, SECRET_KEY, ALGORITHM)
            result = {'message':'SUCCESS', 'access_token':access_token, 'profile':user.image}

            if created:
                return JsonResponse(result, status=201)
           
            return JsonResponse(result, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
        except MultipleObjectsReturned:
            return JsonResponse({'message':'MULTIPLE_OBJECT_RETURNED'}, status=400)