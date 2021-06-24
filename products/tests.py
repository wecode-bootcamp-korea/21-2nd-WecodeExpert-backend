from django.test     import TestCase, Client

from .models         import Category, CategoryExpert, Product
from users.models    import HashTag, SellerInfo, Position, User, Expert 

class ProductTest(TestCase):
    def setUp(self):
        Category.objects.create(
            id = 1,
            name = 'python'
        )

        SellerInfo.objects.create(
            id = 1,
            email = 'python@gmail.com',
            address = 'python-1234',
            phone_number = '010-1234-5678'
        )

        Position.objects.create(
            id = 1,
            name = 'backend'
        )
        
        User.objects.create(
            id = 1,
            is_kakao = 1,
            email = 'python@gmail.com',
            image = 'python.url',
            is_deleted = 0,
            identifier = 12345,
        )

        Expert.objects.create(
            id = 1,
            name = 'python',
            introduction = 'python-django',
            image = 'python.url',
            seller_info = SellerInfo.objects.get(id=1),
            user = User.objects.get(id=1),
            position = Position.objects.get(id=1)
        )

        CategoryExpert.objects.create(
            id = 1,
            category = Category.objects.get(id=1),
            expert = Expert.objects.get(id=1)
        )

        Product.objects.create(
            id = 1,
            title = 'python',
            price = 10000,
            content = 'django-python',
            sell_count = 0,
            category = Category.objects.get(id=1),
            expert = Expert.objects.get(id=1)
        )

        HashTag.objects.create(
            id = 1,
            name = '#python',
            expert = Expert.objects.get(id=1)
        )

    def tearDown(self):
        Category.objects.all().delete()
        SellerInfo.objects.all().delete()
        Position.objects.all().delete()
        User.objects.all().delete()
        Expert.objects.all().delete()
        CategoryExpert.objects.all().delete()
        Product.objects.all().delete()
        HashTag.objects.all().delete()

    def test_productview_get(self):
        client = Client()
        response = client.get('/products')

        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS',
                'result' : [
                    {
                        'product_id'    : 1,
                        'category_name' : 'python',
                        'title'         : 'python',
                        'price'         : 10000,
                        'content'       : 'django-python',
                        'expert_name'   : 'python',
                        'expert_type'   : 'backend',
                        'expert_image'  : 'python.url',
                        'hashtag'       : ['#python']
                    }
                ],
                'count' : 1
            })
        self.assertEqual(response.status_code, 200)

class ExpertTest(TestCase):
    def setUp(self):
        Position.objects.create(
            id = 1,
            name = 'backend'
        )
        
        User.objects.create(
            id = 1,
            is_kakao = 1,
            email = 'python@gmail.com',
            image = 'python.url',
            is_deleted = 0,
            identifier = 12345,
        )

        SellerInfo.objects.create(
            id = 1,
            email = 'python@gmail.com',
            address = 'python-1234',
            phone_number = '010-1234-5678'
        )

        Expert.objects.create(
            id = 1,
            name = 'python',
            introduction = 'python-django',
            image = 'python.url',
            seller_info = SellerInfo.objects.get(id=1),
            user = User.objects.get(id=1),
            position = Position.objects.get(id=1)
        )

        HashTag.objects.create(
            id = 1,
            name = '#python',
            expert = Expert.objects.get(id=1)
        )

    def tearDown(self):
        Position.objects.all().delete()
        User.objects.all().delete()
        SellerInfo.objects.all().delete()
        Expert.objects.all().delete()
        HashTag.objects.all().delete()

    def test_expertview_get(self):
        client = Client()
        response = client.get('/products/expert')

        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS',
                'result' : [
                    {
                        'expert_name'  : 'python',
                        'expert_type'  : 'backend',
                        'expert_image' : 'python.url',
                        'introduction' : 'python-django',
                        'hashtag'      : ['#python']
                    }
                ]
            })
        self.assertEqual(response.status_code, 200)

class DetailTest(TestCase):
    def setUp(self):
        Category.objects.create(
            id = 1,
            name = 'python'
        )

        SellerInfo.objects.create(
            id = 1,
            email = 'python.sell@gmail.com',
            address = 'python-1234',
            phone_number = '010-1234-5678'
        )

        Position.objects.create(
            id = 1,
            name = 'backend'
        )
        
        User.objects.create(
            id = 1,
            is_kakao = 1,
            email = 'python@gmail.com',
            image = 'python.url',
            is_deleted = 0,
            identifier = 12345,
        )

        Expert.objects.create(
            id = 1,
            name = 'python',
            introduction = 'python-django',
            image = 'python.url',
            seller_info = SellerInfo.objects.get(id=1),
            user = User.objects.get(id=1),
            position = Position.objects.get(id=1)
        )

        CategoryExpert.objects.create(
            id = 1,
            category = Category.objects.get(id=1),
            expert = Expert.objects.get(id=1)
        )

        Product.objects.create(
            id = 1,
            title = 'python',
            price = 10000,
            content = 'django-python',
            sell_count = 0,
            category = Category.objects.get(id=1),
            expert = Expert.objects.get(id=1)
        )

        HashTag.objects.create(
            id = 1,
            name = '#python',
            expert = Expert.objects.get(id=1)
        )

    def tearDown(self):
        Category.objects.all().delete()
        SellerInfo.objects.all().delete()
        Position.objects.all().delete()
        User.objects.all().delete()
        Expert.objects.all().delete()
        CategoryExpert.objects.all().delete()
        Product.objects.all().delete()
        HashTag.objects.all().delete()

    def test_detailview_get(self):
        client = Client()
        response = client.get('/products/1')

        self.assertEqual(response.json(),
            {   
                'message' : 'SUCCESS',
                'result' : {
                    'expert_name'  : 'python',
                    'expert_type'  : 'backend',
                    'expert_image' : 'python.url',
                    'email'        : 'python.sell@gmail.com',
                    'address'      : 'python-1234',
                    'phone_number' : '010-1234-5678',
                    'title'        : 'python',
                    'price'        : 10000,
                    'content'      : 'django-python',
                    'sell_count'   : 0
                }
            })
        self.assertEqual(response.status_code, 200)

        def test_detailview_invalid_product(self):
            client = Client()
            response = client.get('/products/0')

            self.assertEqual(response.json(), {'message' : 'INVALID_PRODUCT'})
            self.assertEqual(response.status_code, 400)
