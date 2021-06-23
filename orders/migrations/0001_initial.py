# Generated by Django 3.2.4 on 2021-06-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]