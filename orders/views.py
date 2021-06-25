import json

from django.db       import transaction
from django.views    import View
from django.http     import JsonResponse

from. models         import Order
from users.utils     import user_check
from users.models    import User
from products.models import Product

class OrderView(View):
    @user_check('MUST_BE_USER') 
    def post(self, request):
        try:
            data = json.loads(request.body) 
            user = User.objects.get(id=request.user.get('user_id'))
        
            if not Product.objects.filter(id=data['product_id']).exists():
                return JsonResponse({'message':'INVALID_PRODUCT'}, status=400)

            product = Product.objects.get(id=data['product_id'])
            with transaction.atomic():
                order = Order.objects.create(user=user, product=product, price=data['price'])
                order.product.sell_count +=1
                product.save()
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)