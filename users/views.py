import jwt, json 
import requests
from json.decoder import JSONDecodeError

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import MultipleObjectsReturned
from django.db              import transaction

from .models                import User, Expert, HashTag, SellerInfo
from products.models        import Category
from wecode_expert.settings import SECRET_KEY, ALGORITHM
from .utils                 import user_check

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

            user_data    = {'user_id': user.id}
            access_token = jwt.encode(user_data, SECRET_KEY, ALGORITHM)
            result       = {'message':'SUCCESS', 'access_token':access_token, 'profile':user.image}

            if created:
                return JsonResponse(result, status=201)
           
            return JsonResponse(result, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
        except MultipleObjectsReturned:
            return JsonResponse({'message':'MULTIPLE_OBJECT_RETURNED'}, status=400)

class ExpertView(View):
    @user_check('MUST_BE_USER')
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user.get('user_id')

            if not Category.objects.filter(id=data['category_id']).exists():
                return JsonResponse({'message':'INVALID_CATEGORY'}, status=400)
            
            if Expert.objects.filter(user_id=user).exists():
                return JsonResponse({'message':'EXISTS_EXPERT'}, status=400)
        
            category = Category.objects.get(id=data['category_id'])

            with transaction.atomic(savepoint=False):
                seller_info = SellerInfo.objects.create(
                    address      = data['seller_info']['address'],
                    phone_number = data['seller_info']['phone_number'],
                    email        = data['seller_info']['email']
                )
                expert = Expert.objects.create(
                    user_id      = user,
                    position_id  = data['position_id'],
                    seller_info  = seller_info,
                    introduction = data['introduction'],
                    image        = data['image'],
                    name         = data['name'],
                )
                category.expert.add(expert)

                hash_tags        = set(data['hash_tag'])
                hash_tag_objects = [HashTag(name = tag_name, expert = expert) for tag_name in hash_tags]
                HashTag.objects.bulk_create(hash_tag_objects)

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'INVALID_VALUE'}, status=400)