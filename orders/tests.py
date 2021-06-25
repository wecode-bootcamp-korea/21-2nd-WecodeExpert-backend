import json
import jwt

from django.test     import TestCase, Client

from. models         import Order
from users.models    import Expert, Position, SellerInfo, User
from products.models import Category, Product
from my_settings     import SECRET_KEY, ALGORITHM


class OrderTest(TestCase):
    def setUp(self):
        category=Category.objects.create(
            id         = 1,
            name       ='python')
        user=User.objects.create(
            id         = 1,
            is_kakao   = 1,
            email      = 'a@naver.com',
            image      = 'kskejsldadlwe',
            is_deleted = 0,
            identifier = 1
        ) 

        self.token = jwt.encode({'user_id' :User.objects.get(id=user.id).id}, SECRET_KEY, algorithm = ALGORITHM)
        position   = Position.objects.create(
            id     = 1,
            name   ='백엔드')

        seller_Info=SellerInfo.objects.create(
            email        = 'a@naver.com',
            address      ='선릉대로427',
            phone_number = 0
        )
        expert=Expert.objects.create(
            id=1,
            introduction = '@@@@@@@@@@@@@@@@@@@@@@@',
            image        = '#################',
            created_at   = 0,
            name         ='박창현',
            position     = position,
            seller_info  = seller_Info,
            user         = user
            )

        Product.objects.create(
            id         = 1,
            title      = '파이썬 20년',
            price      = 4300,
            sell_count = 1,
            category   = category,
            expert     = expert
        )
        
    def tearDown(self):
        Category.objects.all().delete()
        Expert.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()
        Order.objects.all().delete()
   
    def test_orderview_post_invalid_product(self):
        client   = Client()
        header = {"HTTP_Authorization" : self.token}
        response = client.post('/orders',json.dumps({
            "product_id": 2,
            "price"     : 4300
            }),**header, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'INVALID_PRODUCT'})
        
    def test_orderview_post_success(self):
        client   = Client()
        header = {"HTTP_Authorization" : self.token}
        response = client.post('/orders',json.dumps({
            "product_id": 1,
            "price"     : 4300
            }),**header, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{'message':'SUCCESS'})

    def test_orderview_post_keyerror(self):
        client   = Client()
        header = {"HTTP_Authorization" : self.token}
        response = client.post('/orders',json.dumps({
            "prodct_id": 1,
            "price"     : 4300
            }),**header, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'KEY_ERROR'})