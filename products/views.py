from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models          import Product
from users.models     import Expert

class ProductView(View):
    def get(self , request):
        category_id = request.GET.get('category')
        sort        = request.GET.get('sort', '-created_at')
        page_size   = int(request.GET.get('page_size', 8))
        page        = int(request.GET.get('page', 1))

        limit  = page_size * page
        offset = limit - page_size
        
        q = Q() 

        if category_id:
            q = (Q(category_id=category_id))

        products = Product.objects.filter(q).select_related('expert', 'category', 'expert__position').prefetch_related('expert__hashtag_set').order_by(sort)

        product_info = [{
            'product_id'    : product.id,
            'category_name' : product.category.name,
            'title'         : product.title,
            'price'         : int(product.price),
            'content'       : product.content,
            'expert_name'   : product.expert.name,
            'expert_type'   : product.expert.position.name,
            'expert_image'  : product.expert.image,
            'hashtag'       : [hashtag.name for hashtag in product.expert.hashtag_set.all()]
        } for product in products] 

        count = len(product_info)

        return JsonResponse(
            {
            'message' : 'SUCCESS',
            'result'  : product_info[offset:limit],
            'count'   : count
        }, status=200)

class ExpertView(View):
    def get(self, request):
        category_id = request.GET.get('category')
        page_size   = int(request.GET.get('page_size', 8))
        page        = int(request.GET.get('page', 1))

        limit  = page_size * page
        offset = limit - page_size

        q = Q() 

        if category_id:
            q = (Q(categoryexpert__category_id=category_id))

        experts = Expert.objects.select_related('position').prefetch_related('hashtag_set').filter(q)

        expert_info = [{
            'expert_name'  : expert.name,
            'expert_type'  : expert.position.name,
            'expert_image' : expert.image,
            'introduction' : expert.introduction,
            'hashtag'      : [hashtag.name for hashtag in expert.hashtag_set.all()]
        } for expert in experts]
        
        count = len(expert_info)

        return JsonResponse(
            {
                'message' : 'SUCCESS',
                'result'  : expert_info[offset:limit],
                'count'   : count
        }, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message' : 'INVALID_PRODUCT'}, status=400)
        
        product = Product.objects.select_related('expert', 'expert__position', 'expert__seller_info').get(id=product_id)

        product_info = {
            'expert_name'  : product.expert.name,
            'expert_type'  : product.expert.position.name,
            'expert_image' : product.expert.image,
            'email'        : product.expert.seller_info.email,
            'address'      : product.expert.seller_info.address,
            'phone_number' : product.expert.seller_info.phone_number,
            'title'        : product.title,
            'price'        : int(product.price),
            'content'      : product.content,
            'sell_count'   : product.sell_count
        }

        return JsonResponse(
            {
                'message' : 'SUCCESS',
                'result'  : product_info
        }, status=200)