from django.db import models

class Category(models.Model):
    name   = models.CharField(max_length=45)
    expert = models.ManyToManyField('users.Expert', through='CategoryExpert')

    class Meta:
        db_table = 'categories'

class CategoryExpert(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    expert   = models.ForeignKey('users.Expert', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_experts'

class Product(models.Model):
    title      = models.CharField(max_length=45)
    price      = models.DecimalField(max_digits=8, decimal_places=2)
    content    = models.TextField()
    sell_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category   = models.ForeignKey('Category', on_delete=models.CASCADE)
    expert     = models.ForeignKey('users.Expert', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Review(models.Model):
    content     = models.CharField(max_length=200)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'