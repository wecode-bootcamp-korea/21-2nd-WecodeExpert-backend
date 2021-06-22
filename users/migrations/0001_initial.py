# Generated by Django 3.2.4 on 2021-06-23 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'experts',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'positions',
            },
        ),
        migrations.CreateModel(
            name='SellerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'seller_infoes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_kakao', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('like', models.ManyToManyField(through='users.Like', to='products.Product')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_like', to='users.user'),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.expert')),
            ],
            options={
                'db_table': 'hash_tags',
            },
        ),
        migrations.AddField(
            model_name='expert',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.position'),
        ),
        migrations.AddField(
            model_name='expert',
            name='seller_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.sellerinfo'),
        ),
        migrations.AddField(
            model_name='expert',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
