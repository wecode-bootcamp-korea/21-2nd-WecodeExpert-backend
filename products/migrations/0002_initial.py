# Generated by Django 3.2.4 on 2021-06-23 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.expert'),
        ),
        migrations.AddField(
            model_name='categoryexpert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AddField(
            model_name='categoryexpert',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.expert'),
        ),
        migrations.AddField(
            model_name='category',
            name='expert',
            field=models.ManyToManyField(through='products.CategoryExpert', to='users.Expert'),
        ),
    ]