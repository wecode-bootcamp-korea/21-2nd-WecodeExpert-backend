from django.db import models

class User(models.Model):
    is_kakao   = models.BooleanField(default=True)
    email      = models.EmailField()
    image      = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    identifier = models.CharField(max_length=45)
    like       = models.ManyToManyField('products.Product', through='Like')

    class Meta:
        db_table = 'users'

class Expert(models.Model):
    name         = models.CharField(max_length=45)
    introduction = models.CharField(max_length=200)
    image        = models.CharField(max_length=200)
    created_at   = models.DateTimeField(auto_now_add=True)
    seller_info  = models.OneToOneField('SellerInfo', on_delete=models.CASCADE)
    user         = models.OneToOneField('User', on_delete=models.CASCADE)
    position     = models.ForeignKey('Position', on_delete=models.CASCADE)

    class Meta:
        db_table = 'experts'

class SellerInfo(models.Model):
    email        = models.EmailField()
    address      = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'seller_infoes'

class HashTag(models.Model):
    name   = models.CharField(max_length=45)
    expert = models.ForeignKey('Expert', on_delete=models.CASCADE)

    class Meta:
        db_table = 'hash_tags'

class Position(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'positions'

class Like(models.Model):
    user    = models.ForeignKey('User', on_delete=models.CASCADE, related_name='origin_like')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'

